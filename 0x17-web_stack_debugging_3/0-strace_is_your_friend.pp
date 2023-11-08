# this manifest changes the value 'phpp' to  'php'  in the config files

exec {'updating the confi':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => '/usr/local/bin/:/bin/',
}
