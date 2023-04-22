# mysql

Installs MySQL on Debian/Ubuntu, and configures it so that user `root`
can connect with a password (by default the operating system user
`root` is allowed to connect as MySQL user `root` without a
password).

Package `python3-pymysql` is also installed to allow usage of the
Ansible `community.mysql` module.

## Parameters

- `mysql_root_password`: The password of the mysql `root` user.
  Usually you will store this in the vault.

- `mysql_config`: A dictionary of configuration variables, like this:
  ```
  - role: mysql
    mysql_config:
      disable-log-bin: null
      bind-address: 0.0.0.0
  ```
  The above will result in the following being added to
  `/etc/mysql/mysql.conf.d/mysqld.cnf`:

      disable-log-bin
      bind-address = 0.0.0.0

  Those items that have the value `null` are merely added to the file
  without a trailing `= [value]`.

- `mysql_allowed_client_ips`. The default is an empty string. If not an
  empty string, a ferm rule is added to allow mysql clients to connect
  to port 3306.  It should be a space-separated string of ip addresses.

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
