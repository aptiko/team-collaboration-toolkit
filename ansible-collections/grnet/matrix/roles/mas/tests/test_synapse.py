"""Render the actual Synapse templates without installing services."""

from pathlib import Path
import unittest

from ansible.plugins.filter.core import FilterModule
from jinja2 import Environment, FileSystemLoader, StrictUndefined
import yaml


class SynapseTests(unittest.TestCase):
    def setUp(self):
        role = Path(__file__).resolve().parents[2] / 'synapse'
        self.env = Environment(loader=FileSystemLoader(role / 'templates'), undefined=StrictUndefined)
        self.env.filters.update(FilterModule().filters())
        self.settings = yaml.safe_load((role / 'defaults/main.yml').read_text())
        self.settings.update(
            ansible_managed='test', synapse_server_name='example.org',
            synapse_public_baseurl='https://matrix.example.org/',
            synapse_database_password='test', synapse_mas_enabled=True,
            mas_synapse_secret='test-secret',
        )

    def test_delegates_authentication(self):
        config = yaml.safe_load(self.env.get_template('synapse.yaml.j2').render(self.settings))
        self.assertEqual(config.get('matrix_authentication_service'), {
            'enabled': True, 'endpoint': 'http://127.0.0.1:8080/', 'secret': 'test-secret',
        })

    def test_registration_belongs_to_mas(self):
        config = yaml.safe_load(self.env.get_template('synapse.yaml.j2').render(self.settings))
        self.assertNotIn('registration_shared_secret_path', config)

    def test_compatibility_routes_precede_synapse(self):
        for server in ('apache', 'nginx'):
            with self.subTest(server=server):
                proxy = self.env.get_template(f'synapse.{server}.conf.j2').render(self.settings)
                self.assertIn('(login|logout|refresh)', proxy)
                self.assertLess(proxy.index('127.0.0.1:8080'), proxy.index('127.0.0.1:8008'))

    def test_default_keeps_synapse_authentication(self):
        self.settings['synapse_mas_enabled'] = False
        del self.settings['mas_synapse_secret']
        config = yaml.safe_load(self.env.get_template('synapse.yaml.j2').render(self.settings))
        self.assertNotIn('matrix_authentication_service', config)
        self.assertIn('registration_shared_secret_path', config)
        for server in ('apache', 'nginx'):
            proxy = self.env.get_template(f'synapse.{server}.conf.j2').render(self.settings)
            self.assertNotIn('8080', proxy)
