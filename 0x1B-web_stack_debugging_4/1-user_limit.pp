# this adjusts the limit of nginx filefor hard limit
exec {'Increase hard limit':
        command => "sed -i 's/hard nofile 5/hard nofile 6000/' /etc/security/limits.conf",
        path    => '/bin',
}

# increasing soft limit
exec {'Increase soft limit':
        command => "sed -i 's/soft nofile 4/soft nofile 5000/' /etc/security/limits.conf",
        path    => '/bin',
}
