#Using Puppet, install flask from pip3
package { 'Flask 2.1.0':
    ensure   => 'installed',
    provider => 'pip3',
}
