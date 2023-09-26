# installing ngnix with the latest
class{'nginx':
    manage_repo    => 'true',
    package_source => 'nginx-mainline',
}

file {'/etc/nginx/html/index.html':
        ensure  => 'present',
        content => 'Hello World!',
}

nginx::resource::server {'default_server':
        listen port    => '80',
        listen_options => ['default_server'],
        server_name    => '_',
        www_root       => '/etc/nginx/html/index.html';
        index_files    => ['index.html', 'index.htm'],
}

nginx::resource::location{'redirect_me':
        location            => '/redirect_me',
        location_cfg_append => {
        'return' => '301 https://www.youtube.com/watch?v=QH2-TGUlwu4',
}
}
