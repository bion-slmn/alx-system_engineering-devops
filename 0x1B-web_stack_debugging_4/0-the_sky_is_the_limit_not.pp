# this adjusts the limit of nginx file from 15 to 4096
exec {'Increase limit':
        command => "sed -i 's/15/4096/' /etc/default/nginx",
        path    => '/bin',
}

# restart nginx only when the above has changed
exec {'restart nginx':
        command => 'nginx restart',
        path    => '/etc/init.d/',
}
