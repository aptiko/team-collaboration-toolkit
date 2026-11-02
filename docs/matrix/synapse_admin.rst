=============
synapse_admin
=============

``grnet.matrix.synapse_admin`` installs a selected prebuilt release of
`Synapse Admin <https://github.com/Awesome-Technologies/synapse-admin>`_, the
web administration interface for Synapse. It serves the application at the
root of a dedicated hostname using Apache or nginx and configures
``config.json`` to restrict the interface to your homeserver.

The role includes ``aptiko.general.website`` as a dependency. Run
``aptiko.general.webserver`` explicitly before this role. HTTPS uses Let's
Encrypt by default; DNS must point to the server and ports 80 and 443 must
be reachable for certificate issuance.

API access and authentication
=============================

The administrator's browser must be able to reach both ``/_matrix`` and
``/_synapse/admin`` at ``synapse_admin_homeserver_url``. The :doc:`synapse`
role proxies the admin API when ``synapse_expose_admin_api: true`` is set.
Set this in inventory and rerun the Synapse role, then point
``synapse_admin_homeserver_url`` to your usual Synapse HTTPS URL.
The setting defaults to ``false``. Installing only this static interface
does not expose the API or grant administrator rights.
The ``restrictBaseUrl`` setting controls the interface's homeserver selection;
it is not an access control for the API.

Use an existing Synapse administrator account to log in. Upstream has an
`open MAS compatibility issue
<https://github.com/Awesome-Technologies/synapse-admin/issues/429>`_;
normal login with delegated authentication may not grant admin API access.
The :doc:`synapse` role enables MAS by default, so verify your chosen release's
authentication support before deploying this interface for a MAS installation.
This role does not create accounts or manage MAS privileges. An HTTPS
interface needs an HTTPS homeserver URL to avoid browser mixed-content blocking.

Example
=======

For an existing Synapse installation, retain its inventory settings (including
its version, database credentials and MAS settings) and run both roles::

  - hosts: matrix
    become: true
    vars:
      webserver_type: nginx
      website_letsencrypt_admin: admin@example.org
      synapse_fqdn: matrix.example.org
      synapse_expose_admin_api: true
      synapse_admin_version: "0.11.4"
      synapse_admin_fqdn: matrix-admin.example.org
      synapse_admin_homeserver_url: https://matrix.example.org
    roles:
      - aptiko.general.webserver
      - grnet.matrix.synapse
      - grnet.matrix.synapse_admin

Parameters
==========

.. data:: synapse_admin_version

   Required. Quoted release version without a leading ``v``, for example
   ``"0.11.4"``. The role downloads the upstream release archive into
   ``/var/www/<synapse_admin_fqdn>/synapse-admin-<version>``. Change this
   value and rerun the role to switch releases; old release directories
   are retained.

.. data:: synapse_admin_fqdn

   Required. Hostname for the administration interface, different from the
   homeserver hostname and from other websites on this host.

.. data:: synapse_admin_homeserver_url

   Required. Absolute HTTP(S) URL exposing the homeserver's client and admin
   APIs to the administrator's browser.
   For example, ``https://matrix.example.org`` when the Synapse role uses
   ``synapse_fqdn: matrix.example.org`` and ``synapse_expose_admin_api: true``.
   Supply the base URL without ``/_matrix`` or ``/_synapse/admin``. Requests
   come directly from the browser, so this must be a browser-reachable address.

.. data:: synapse_admin_ssl

   TLS mode passed to ``aptiko.general.website``. Default ``"letsencrypt"``;
   also accepts ``"self-signed"``, ``"custom"`` and ``"off"``. Custom TLS
   requires ``website_cert`` and ``website_private_key``.

.. data:: webserver_type

   Required. ``"nginx"`` or ``"apache"``.

.. data:: website_letsencrypt_admin

   Required for Let's Encrypt. Email address used for certificate registration.
