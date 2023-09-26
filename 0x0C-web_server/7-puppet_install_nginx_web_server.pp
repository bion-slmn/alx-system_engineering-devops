# installing ngnix with the latest

package { 'nginx':
  ensure => 'installed',
}

file { '/etc/nginx/html':
  ensure => 'directory',
}

file { '/etc/nginx/html/index.html':
  ensure  => 'present',
  content => 'Hello World!',
}

file { '/etc/nginx/sites-available/default':
        ensure => 'present',
        content => 'server {
     listen      80 default_server;
     listen      [::]:80 default_server;
     root        /etc/nginx/html;
     index       index.html index.htm;

     location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
        }

    error_page 404 /custom_404.html;
    location = /custom_404.html {
        root /etc/nginx/html;
        internal;
        }
}',
}

service { 'nginx':
  ensure    => 'running',
  enable    => true,
}
