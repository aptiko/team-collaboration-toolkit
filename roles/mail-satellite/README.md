# mail-satellite

Installs and configures a mail server so that it's possible to send emails
either through port 25 (listening on the local interface only) or by executing
the `sendmail` command. All email is sent using a smarthost.

It's mainly useful in two cases:

1. Forwarding cron email (otherwise the administrator would need to
   login to see if any cron email has been received locally.)
2. Being used as the smarthost of applications or services installed on
   the server. In this case such applications should be configured to
   use `localhost:25` as the smarthost. While they could be configured
   to use the smarthost directly, using `localhost:25` can be useful
   especially when the smarthost is not in our control, because whenever
   something doesn't work we can get some information from Postfix's
   logs as to what is going wrong.

## Parameters

### mailname

The default domain name that will be used for email addresses that do
not contain `@`.

### smarthost

The smart host, such as `relay.example.com`.

### smarthostport

The smarthost port, such as 25 or 587 (the default).

### masquerade_domains

Optional. This will be used as Postfix's
[masquerade_domains](http://www.postfix.org/postconf.5.html#masquerade_domains)
parameter.  For example, if `mailname` is `nextcloud.digigov.grnet.gr`,
you may want to use `masquerade_domains = grnet.gr` so that the sender
`root@nextcloud.digigov.grnet.gr` will be converted to `grnet.gr`.

### mail_aliases

A hash that maps local emails to actual addresses, for example::

    mail_aliases:
      root: antonis@example.com,panagiotis@example.com
      www-data: root

You should practically always create an alias for `root`, and very
often for `www-data` as well, and for everything that uses cron.

Note: We don't use `/etc/aliases` for this functionality; Postfix only
uses `/etc/aliases` for local delivery. We use
[virtual_alias_maps](http://www.postfix.org/postconf.5.html#virtual_alias_maps)
instead.

## Meta

Written by Antonis Christofides.

Copyright (C) 2021-2023 GRNET

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
