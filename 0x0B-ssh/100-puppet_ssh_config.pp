#  this resource configures the client to use the private key ~/.ssh/school
# and thremoves the password login

file {'/etc/ssh/ssh_config':
    ensure  => 'present',
    content => "PasswordAuthentication no\nIdentityFile ~/.ssh/school",
}
