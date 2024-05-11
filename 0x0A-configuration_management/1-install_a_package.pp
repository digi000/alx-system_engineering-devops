#Using Puppet, install flask from pip3
class { 'flask':
    package { 'python3-flask 2.1.0':
        ensure   => 'installed',
        provider => 'pip3',
    }
    require => Package['pip3'],
}
