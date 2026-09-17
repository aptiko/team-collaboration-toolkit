# grnet.matrix

The `grnet.matrix.synapse` role installs an explicitly selected Synapse version
with pip in `/opt/synapse/venv`, reusing distribution Python packages through
`--system-site-packages`. It configures a local PostgreSQL database using
`aptiko.general.postgresql`. The `synapse_version` parameter is required.
The playbook must explicitly run `aptiko.general.webserver` before this role.
The role configures an Apache or nginx reverse proxy using
`aptiko.general.website`, with Let's Encrypt TLS by default.

See the [role documentation](https://team-collaboration-toolkit.readthedocs.io/en/latest/matrix/synapse.html)
for prerequisites, variables and an example playbook.
