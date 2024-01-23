# site.pp

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Create Hello World page
file { '/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!',
}

# Configure Nginx
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => template('nginx/default.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Enable site by creating a symbolic link
file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
  notify => Service['nginx'],
}

# Define Nginx service
service { 'nginx':
  ensure  => running,
  enable  => true,
}

# nginx/default.erb

server {
    listen 80;
    server_name localhost;

    location / {
        return 301 https://www.youtube.com/watch?v=dQw4w9WgXcQ;
    }

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=dQw4w9WgXcQ;
    }

    location / {
        root /var/www/html;
        index index.html;
    }
}
