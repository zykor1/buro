#bash -e install_nginx.sh | tee install_nginx.log

# Set environment variables
APPNAME=nginx_buro       # Name of the uWSGI Custom Application
APPPORT=22800              # Assigned port for the uWSGI Custom Application
PYTHON=python2.7           # Django python version
DJANGOAPP=posicionlocal           # Django application name
DJANGOPROJECT=buro    # Django project name

mkdir -p $HOME/webapps/$APPNAME/{bin,nginx,src,tmp}

###########################################################
# nginx 1.2.3
# original: http://nginx.org/download/nginx-1.2.3.tar.gz
###########################################################
cd $HOME/webapps/$APPNAME/src
wget 'http://nginx.org/download/nginx-1.5.1.tar.gz'
tar -xzf nginx-1.5.1.tar.gz
cd nginx-1.5.1
./configure \
  --prefix=$HOME/webapps/$APPNAME/nginx \
  --sbin-path=$HOME/webapps/$APPNAME/nginx/sbin/nginx \
  --conf-path=$HOME/webapps/$APPNAME/nginx/nginx.conf \
  --error-log-path=$HOME/webapps/$APPNAME/nginx/log/nginx/error.log \
  --pid-path=$HOME/webapps/$APPNAME/nginx/run/nginx/nginx.pid  \
  --lock-path=$HOME/webapps/$APPNAME/nginx/lock/nginx.lock \
  --with-http_flv_module \
  --with-http_gzip_static_module \
  --http-log-path=$HOME/webapps/$APPNAME/nginx/log/nginx/access.log \
  --http-client-body-temp-path=$HOME/webapps/$APPNAME/nginx/tmp/nginx/client/ \
  --http-proxy-temp-path=$HOME/webapps/$APPNAME/nginx/tmp/nginx/proxy/ \
  --http-fastcgi-temp-path=$HOME/webapps/$APPNAME/nginx/tmp/nginx/fcgi/
make && make install

###########################################################
# uwsgi 1.2
# original: http://projects.unbit.it/downloads/uwsgi-1.2.tar.gz
###########################################################
cd $HOME/webapps/$APPNAME/src
wget 'http://projects.unbit.it/downloads/uwsgi-1.9.12.tar.gz'
tar -xzf uwsgi-1.9.12.tar.gz
cd uwsgi-1.9.12
$PYTHON uwsgiconfig.py --build
mv ./uwsgi $HOME/webapps/$APPNAME/bin
ln -s $HOME/webapps/$APPNAME/nginx/sbin/nginx $HOME/webapps/$APPNAME/bin

mkdir -p $HOME/webapps/$APPNAME/nginx/tmp/nginx/client

cat << EOF > $HOME/webapps/$APPNAME/nginx/nginx.conf
worker_processes  1;

events {
    worker_connections  1024;
}

http {
    access_log  ${HOME}/logs/user/access_${APPNAME}.log combined;
    error_log   ${HOME}/logs/user/error_${APPNAME}.log  crit;

    include mime.types;
    sendfile on;

    server {
        listen 127.0.0.1:${APPPORT};

        location / {
            include uwsgi_params;
            uwsgi_pass unix://${HOME}/webapps/${APPNAME}/uwsgi.sock;
        }
    }
}
EOF

cat << EOF > $HOME/webapps/$APPNAME/wsgi.py
import sys, os

sys.path = ['${HOME}/webapps/${DJANGOAPP}/${DJANGOPROJECT}/${DJANGOPROJECT}',
            '${HOME}/webapps/${DJANGOAPP}/${DJANGOPROJECT}',
            '${HOME}/webapps/${DJANGOAPP}/lib/${PYTHON}',
           ] + sys.path

os.environ['DJANGO_SETTINGS_MODULE'] = '${DJANGOPROJECT}.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
EOF

# make the start, stop, and restart scripts
cat << EOF > $HOME/webapps/$APPNAME/bin/start
#!/bin/bash

APPNAME=${APPNAME}

# Start uwsgi
\${HOME}/webapps/\${APPNAME}/bin/uwsgi \\
  --uwsgi-socket "\${HOME}/webapps/\${APPNAME}/uwsgi.sock" \\
  --master \\
  --workers 1 \\
  --max-requests 10000 \\
  --harakiri 60 \\
  --daemonize \${HOME}/webapps/\${APPNAME}/uwsgi.log \\
  --pidfile \${HOME}/webapps/\${APPNAME}/uwsgi.pid \\
  --vacuum \\
  --python-path \${HOME}/webapps/\${APPNAME} \\
  --wsgi wsgi

# Start nginx
\${HOME}/webapps/\${APPNAME}/bin/nginx
EOF

cat << EOF > $HOME/webapps/$APPNAME/bin/stop
#!/bin/bash

APPNAME=${APPNAME}

# stop uwsgi
\${HOME}/webapps/\${APPNAME}/bin/uwsgi --stop \${HOME}/webapps/\${APPNAME}/uwsgi.pid

# stop nginx
kill \$(cat \${HOME}/webapps/\${APPNAME}/nginx/run/nginx/nginx.pid)
EOF

cat << EOF > $HOME/webapps/$APPNAME/bin/restart
#!/bin/bash

APPNAME=${APPNAME}

\${HOME}/webapps/\${APPNAME}/bin/stop
sleep 5
\${HOME}/webapps/\${APPNAME}/bin/start
EOF

chmod 755 $HOME/webapps/$APPNAME/bin/{start,stop,restart}