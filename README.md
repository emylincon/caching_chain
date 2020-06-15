# caching hash retrieval server
* Move folder to /var/www/html after running install.sh
```bash
sudo mv web /var/www/html
```

* edit /etc/apache2/sites-available/000-default.conf
```bash
sudo nano /etc/apache2/sites-available/000-default.conf
```

* add the following
```text
<VirtualHost *:80>
    # The ServerName directive sets the request scheme, hostname and port that
    # the server uses to identify itself. This is used when creating
    # redirection URLs. In the context of virtual hosts, the ServerName
    # specifies what hostname must appear in the request's Host: header to
    # match this virtual host. For the default virtual host (this file) this
    # value is not decisive as it is used as a last resort host regardless.
    # However, you must set it for any further virtual host explicitly.
    #ServerName www.example.com
    
    ServerAdmin webmaster@localhost
    #DocumentRoot /var/www/html
    
    WSGIScriptAlias / /var/www/html/caching_chain/app.wsgi
    <Directory /var/www/html/caching_chain>
    Order allow,deny
    Allow from all
    </Directory>
    
    # Available loglevels: trace8, ..., trace1, debug, info, notice, warn,
    # error, crit, alert, emerg.
    # It is also possible to configure the loglevel for particular

```