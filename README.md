Traveller Planet Visualiser
===========================

Components
----------

* `scripts/`
  * Contains misc helper scripts.
* `server/`
  * Django app.

Usage
-----

There is an admin interface at `<host>/admin/` which you can use to add new planets.
You can export then as JSON by going to `<host>/planets/<location>` to get an individual planet, or just `<host>/planets/` to get all the planets as a big JSON array.

Installation
------------

This guide assumes a Debian/Ubuntu bases server using Apache with WSGI.

### Commands

* Create a WSGI file:

```python
import os
import sys

sys.path = ['<Traveller Path>'] + sys.path
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "traveller.settings")

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
```

* Replace `<Traveller Path>` with the path to the `server/` folder.

* Add the following to a file in `/etc/apache2/sites-available/`:

```apache
<VirtualHost *:80>
  WSGIScriptAlias / <django.wsgi>

  ServerName <servername>

  Alias /static/ <django folder>/django/contrib/admin/static/

  <Directory /path>
    Order allow,deny
    Allow from all
  </Directory>

  ErrorLog /var/log/apache2/error.log
  # Possible values include: debug, info, notice, warn, error, crit,
  # alert, emerg.
  LogLevel warn
  CustomLog /var/log/apache2/access.log combined
</VirtualHost>
```

* Replace the `ServerName` with your own host.
* Replace `<django.wsgi>` with the path to your real WSGI file.
* Replace `<django folder>` with your django install folder.
* Replace the `<Directory /path>` with the path to your `/server/` folder.

* Copy the `server/traveller/settings.py.sample` to `server/traveller/settings.py` and update the database configuration at the top.

* Run the `manage.py syncdb` script in the `server/` folder.

* Run `manage.py createsuperuser` to create the default admin user.

* Restart your Apache server.
