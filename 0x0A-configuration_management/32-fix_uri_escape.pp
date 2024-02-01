exec { 'fix_uri_escape':
  command => 'sed -i "s|^require \"puppet/util/logging\"|require \"puppet/util/logging\"\nrequire \"uri\"|" /usr/lib/ruby/vendor_ruby/puppet/util.rb',
  path    => '/usr/bin',
  unless  => 'grep -q "require \"uri\"" /usr/lib/ruby/vendor_ruby/puppet/util.rb',
  require => Package['puppet'],
}

