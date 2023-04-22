# nextcloud Ansible role

Installs and configures Nextcloud.

Installs Nextcloud, MySQL, Apache and Redis on Debian/Ubuntu.

You may need to perform additional configuration using Nextcloud's web
interface. See section "Limitations" below for that.

## Parameters

### nextcloud_fqdn

The domain name for Nextcloud.

### nextcloud_admin_user

The username for the Nextcloud administrator. The default is `admin`.

### nextcloud_admin_user_password

The Nextcloud administrator password. This will usually be in the vault.

### nextcloud_download_url

By default, the latest version of Nextcloud Community will be installed. To
install another version, specify a different URL, such as
`https://download.nextcloud.com/server/releases/nextcloud-24.0.11.zip`. It must
point to a zip file.

Unless when an upgrade is specifically requested, this role downloads and
installs Nextcloud only if it is not already installed; if already installed,
the role does not upgrade it and `nextcloud_download_url` is irrelevant. To
upgrade Nextcloud, see the "Upgrading Nextcloud" section below.

### php_memory_limit

Default 512M.

### opcache_interned_strings_buffer

The default for this PHP setting is 8. However in some installations it
might need to be set to 16, and sometimes to 32. It seems to depend on
the installed apps. See the [related support forum
discussion](https://help.nextcloud.com/t/nextcloud-23-02-opcache-interned-strings-buffer/134007/4)
for more information.

### default_phone_region

A country code like "GR". There is no default. This is used for
Nextcloud's `default_phone_region` configuration parameter.

### mail_from_address, mail_domain

The email address from which email notifications from Nextcloud appear
to be sent. For example, to use `noreply@example.com`, specify
`mail_from_address=noreply` and `mail_domain=example.com`.

These settings are those that can be set in the web interface, under
Basic settings, Email server. This role will overwrite these settings
whenever Ansible is run.

It will always use localhost port 25 as the smarthost, without
authentication and without encryption. For this to work, use Ansible
role `mail-satellite`.

### mysql_client_key, mysql_client_cert, mysql_ca_cert

By default, these parameters are empty. In this case, Nextcloud connects
to MySQL without TLS. If they have values, they must be pathnames (in
the Ansible controller) from which the keys and certificates are taken
and installed in the Nextcloud server. In this case, Nextcloud is
configured to connect to MySQL with TLS.

Either all three must be empty, or all three must have a value.

## Upgrading Nextcloud

The role has the option of upgrading Nextcloud to a newer version.
This will cause some downtime and it is important to understand how it
works before trying it. Apart from some checks, this is what it does:

* It moves `/etc/cron.d/nextcloud` to `/tmp/nextcloud.cron`.
* It downloads and unzips the new Nextcloud version to
  `/tmp/nextcloud`.
* It copies the existing Nextcloud installation's `config.php` to
  `/tmp/nextcloud/config`.
* It stops the php-fpm service.
* It moves the existing Nextcloud installation directory to
  `/tmp/nextcloud.old`, then moves the data directory to
  `/tmp/nextcloud/data`, then moves `/tmp/nextcloud` to the correct
  directory (`/var/www/.../nextcloud`). These should happen instantly,
  because these moves are in the same filesystem. In fact, the playbook
  verifies that this is the case before running.
* It starts the php-fpm service. So far the downtime is minimal.
* It executes the `php occ upgrade` command. This takes several
  minutes during which Nextcloud is out of service (it shows a related
  message to users).
* It copies `/tmp/nextcloud.old/translationfiles` to the correct
  location (this contains updated Greek translations).
* It moves `/tmp/nextcloud.cron` back to its correct location.

You can upgrade Nextcloud by specifying the `upgrade_nextcloud` tag. In that
case, you also need to specify `nextcloud_download_url` to point to the version
you want to upgrade to. **This should not be more than one major release ahead
of what is already installed** (this is not checked), otherwise the upgrade
will fail.

Here is an example of how to upgrade:

    ansible-playbook site.yml --tags upgrade_nextcloud \
        -e download_url=https://download.nextcloud.com/server/releases/nextcloud-23.0.0.zip

If all goes well, at the end of the upgrade the directory
`/tmp/nextcloud.old` still contains the old installation (but without
the `data` directory). You need to remove it or move it elsewhere in
order to attempt another upgrade.

If anything goes wrong, you have to cleanup yourself (restore
`/etc/cron.d/nextcloud` and `/var/www/.../nextcloud`). This is why
it is important to understand the process clearly.

Sometimes after major upgrades the theme might break; for example, icons or
logos may be missing from the main toolbar or from other toolbars (such as the
toolbar of the markdown editor). In this case, this typically fixes the
problems:

    cd /var/www/.../nextcloud
    sudo -u www-data php occ maintenance:repair

## Limitations

### Server setup

Many things are hardwired. The current assumption is that Nextcloud,
MySQL, Redis and Apache are all going to be in the same machine.

### Setting up theming

It seems to be nontrivial to setup theming through the command line,
particularly to setup logo, background and favicon. Therefore, the role
does not touch theming; use the web interface to setup theming after
Ansible is run.

### Setting up the Mail app

It doesn't seem to be possible to setup the Mail app through the command
line or Ansible. You need to go to the web interface, logon as admin,
and go to Settings, Administration, Groupware.

## Meta

Written by Antonis Christofides.

Copyright (C) 2022-2023 GRNET

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see http://www.gnu.org/licenses/.
