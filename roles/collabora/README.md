# nextcloud-collabora

Installs and configures collaboraoffice for nextcloud.

Installs Collabora Office with an Apache reverse proxy on port 443, so
that it can be used from nextcloud.

## Parameters

- `nextcloud_fqdn`: The domain name for Nextcloud.
- `collabora_fqdn`: The domain name for Collabora Office.
- `collabora_allowed_languages`: The languages allowed for spell
  checking, as a space-separated string. The default is `en_US`.
  Avoid specifying too many as it is said to affect startup performance.

## Meta

Written by Antonis Christofides.  Originally based on Reiner Nippes's
`collabora` module from https://github.com/ReinerNippes/nextcloud (though it
now contains very little from there).

© 2018 Reiner Nippes  
© 2021-2023 GRNET

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
