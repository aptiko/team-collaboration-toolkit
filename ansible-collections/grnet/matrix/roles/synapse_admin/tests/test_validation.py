"""Run with python -m unittest discover -s roles/synapse_admin/tests from the collection."""

import os
from pathlib import Path
import subprocess
import tempfile
import unittest

import yaml


class ValidationTests(unittest.TestCase):
    def test_settings(self):
        cases = [
            ({}, True),
            ({"synapse_admin_fqdn": "matrix.example.org"}, False),
            ({"synapse_admin_fqdn": "MATRIX.example.org."}, False),
            ({"synapse_admin_homeserver_url": "https://chat.example.org:8448/matrix"}, False),
            ({"synapse_fqdn": "CHAT.example.org."}, False),
            ({"synapse_admin_homeserver_url": "matrix.example.org"}, False),
            ({"synapse_admin_version": "../../bad"}, False),
            ({"synapse_admin_fqdn": "chat.example.org/extra"}, False),
        ]
        for overrides, success in cases:
            with self.subTest(overrides=overrides), tempfile.TemporaryDirectory() as tmp:
                settings = {
                    "synapse_admin_version": "0.11.4",
                    "synapse_admin_fqdn": "chat.example.org",
                    "synapse_admin_homeserver_url": "https://matrix.example.org/",
                }
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
