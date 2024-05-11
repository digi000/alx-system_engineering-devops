#Using Puppet, install flask from pip3
class { 'flask':
    package { 'python3-flask':
        ensure   => '2.1.0',
        provider => 'pip3',
    }
    require => Package['pip3'],
}
