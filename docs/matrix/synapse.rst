=======
synapse
=======

``grnet.matrix.synapse`` installs a selected version of ``matrix-synapse[postgres]``
from PyPI in ``/opt/synapse/venv`` and configures a local PostgreSQL database.
The selected Synapse version must support the distribution's Python and
PostgreSQL versions.

The venv is created with ``--system-site-packages``. Dependencies including
Twisted, cryptography, Pillow and psycopg2 are installed from the distribution
repositories (Ubuntu requires Universe). Pip reuses them when their versions
satisfy Synapse's requirements and installs missing or newer dependencies
inside the venv otherwise. System packages are not modified by pip. Platforms
without compatible PyPI wheels may need additional compiler/build dependencies.

The PostgreSQL dependency also installs PostGIS and requires the
``en_US.UTF-8`` locale to exist. It expects ``postgres_password`` and a
configured ``aptiko.general.duply`` installation; set
``duply_deactivate: true`` if backups are managed separately.

Synapse listens on localhost port 8008 with registration disabled. Set up
an HTTPS reverse proxy separately, forwarding ``/_matrix`` and
``/_synapse/client`` and the ``X-Forwarded-For`` and ``X-Forwarded-Proto``
headers. Federation and client discovery must also be configured separately
when the public hostname differs from the server name.

The role manages ``/etc/opt/synapse/homeserver.yaml`` and the ``matrix-synapse``
systemd service, which runs as the ``matrix-synapse`` user. Logs go to the
systemd journal. The signing key is generated on first start and preserved
in ``/var/opt/synapse/homeserver.signing.key``; media is stored in
``/var/opt/synapse/media_store``.

Example
=======

With the passwords defined in vaulted inventory variables::

  - hosts: matrix
    become: true
    vars:
      synapse_version: "1.159.0"
      synapse_server_name: example.org
      synapse_public_baseurl: https://matrix.example.org/
      duply_deactivate: true
    roles:
      - grnet.matrix.synapse

Parameters
==========

.. data:: synapse_version

   Required, with no default. Exact PyPI release as a quoted string, for
   example ``"1.159.0"``. Change it and rerun the role to install another
   version and restart Synapse. Normal APT upgrades do not upgrade Synapse,
   but can update its system-provided Python dependencies. Pip dependencies
   are not locked. Review Synapse's upgrade notes and back up before upgrading;
   selecting an older version does not undo database migrations.

.. data:: synapse_server_name

   Required. The domain in Matrix user IDs (``@user:example.org``). Choose
   before first installation; changing it on an existing server is unsupported.

.. data:: synapse_database_password

   Required. Password for the Synapse database user. Store in Ansible Vault.

.. data:: postgres_password

   Required by ``aptiko.general.postgresql``. Password for the PostgreSQL
   administrator; store in Ansible Vault.

.. data:: synapse_public_baseurl

   Public HTTPS URL. Defaults to ``https://{{ synapse_server_name }}/``.

.. data:: synapse_report_stats

   Whether to report usage statistics to Synapse developers. Default ``false``.

.. data:: synapse_database_name
   synapse_database_user

   Both default to ``synapse``. The database uses UTF-8 encoding and ``C``
   collation, as required by Synapse.
