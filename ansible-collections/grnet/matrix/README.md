# grnet.matrix

The `grnet.matrix.synapse` role installs an explicitly selected Synapse version
with pip in `/opt/synapse/venv`, reusing distribution Python packages through
`--system-site-packages`. It configures a local PostgreSQL database using
`aptiko.general.postgresql`. The `synapse_version` parameter is required.
An Apache or nginx reverse proxy is installed using `aptiko.general.webserver`
and `aptiko.general.website`, with Let's Encrypt TLS by default.

See the [role documentation](https://team-collaboration-toolkit.readthedocs.io/en/latest/matrix/synapse.html)
for prerequisites, variables and an example playbook.
