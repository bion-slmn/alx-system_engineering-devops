# installing ngnix with the latest

package { 'nginx':
  ensure => 'installed',
}

file { 'adding header content to server':
  path    => '/etc/nginx/sites-available/default',
  ensure  => 'present',
}

exec {'execute the command':
  command => '/bin/sed -i "6i \\\tadd_header X-Served-By $(hostname);" /etc/nginx/sites-available/default',
}

service { 'nginx':
  ensure    => 'running',
  enable    => true,
}
