#!/bin/bash
set -e

mkdir -p /run/mysqld
chown mysql:mysql /run/mysqld
chown -R mysql:mysql /var/lib/mysql

if [ ! -d /var/lib/mysql/mysql ]; then
    mariadb-install-db --user=mysql --datadir=/var/lib/mysql

    mariadbd --user=mysql --bootstrap <<SQL
ALTER USER 'root'@'localhost' IDENTIFIED BY '$(cat /run/secrets/db_root_password)';
CREATE DATABASE IF NOT EXISTS \`${DB_NAME}\`;
CREATE USER IF NOT EXISTS '${DB_USER}'@'%' IDENTIFIED BY '$(cat /run/secrets/db_password)';
GRANT ALL PRIVILEGES ON \`${DB_NAME}\`.* TO '${DB_USER}'@'%';
FLUSH PRIVILEGES;
SQL
fi

exec mariadbd --user=mysql --console
