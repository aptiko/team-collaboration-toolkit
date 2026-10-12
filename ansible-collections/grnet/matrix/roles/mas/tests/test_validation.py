"""Run with python -m unittest discover -s roles/mas/tests from the collection."""

import os
from pathlib import Path
import subprocess
import tempfile
import unittest

import yaml


class ValidationTests(unittest.TestCase):
    def test_invalid_version(self):
        self.check_settings({"mas_version": "../../bad"}, False)

    def test_declarative_settings(self):
        for overrides, success in [
            ({}, True),
            ({"mas_fqdn": "MATRIX.example.org."}, False),
            ({"mas_fqdn": "auth.example.org/extra"}, False),
            ({"mas_database_name": "synapse"}, False),
            ({"mas_synapse_secret": "short"}, False),
            ({"mas_enable_registration": True}, False),
            ({"mas_enable_registration": True, "mas_registration_requires_email": False}, True),
            ({"mas_enable_registration": True, "mas_email": {
                "transport": "smtp", "from": "auth@example.org",
            }}, True),
        ]:
            with self.subTest(overrides=overrides):
                self.check_settings(overrides, success)

    def check_settings(self, overrides, success):
        with tempfile.TemporaryDirectory() as tmp:
            settings = yaml.safe_load((
                Path(__file__).resolve().parents[1] / "defaults/main.yml"
            ).read_text())
            settings.update(
                mas_version="1.26.0", mas_fqdn="auth.example.org",
                synapse_server_name="example.org", synapse_fqdn="matrix.example.org",
                mas_database_password="test", mas_synapse_secret="x" * 64,
                ansible_facts={"architecture": "x86_64"},
            )
            settings.update(overrides)
            playbook = Path(tmp) / "validate.yml"
            playbook.write_text(yaml.safe_dump([{
                "hosts": "localhost",
                "gather_facts": False,
                "vars": settings,
                "tasks": [{"ansible.builtin.import_tasks": str(
                    Path(__file__).resolve().parents[1] / "tasks/validate.yml"
                )}],
            }]))
            result = subprocess.run(
                ["ansible-playbook", "-i", "localhost,", "-c", "local", str(playbook)],
                env={**os.environ, "ANSIBLE_LOCAL_TEMP": tmp},
                capture_output=True, text=True,
            )
            self.assertEqual(result.returncode == 0, success, result.stdout + result.stderr)
