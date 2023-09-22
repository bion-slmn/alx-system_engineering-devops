# kill another program

exec {'kill this prg':
    command => '/usr/bin/pkill killmenow',
    onlyif  => '/usr/bin/pgrep killmenow',
}
