#!/bin/bash
set -e

DB_PASSWORD=$(cat /run/secrets/db_password)
WP_ADMIN_PASSWORD=$(cat /run/secrets/wp_admin_password)
WP_USER_PASSWORD=$(cat /run/secrets/wp_user_password)

mkdir -p /var/www/html

for attempt in $(seq 1 30); do
    if mariadb-admin ping -h mariadb -u "$DB_USER" --password="$DB_PASSWORD" --silent; then
        break
    fi
    sleep 2
done

if [ ! -f /var/www/html/wp-load.php ]; then
    wp core download --path=/var/www/html --allow-root
fi

if ! wp core is-installed --path=/var/www/html --allow-root 2>/dev/null; then
    wp config create \
        --dbname="$DB_NAME" \
        --dbuser="$DB_USER" \
        --dbpass="$DB_PASSWORD" \
        --dbhost=mariadb \
        --path=/var/www/html \
        --allow-root

    wp core install \
        --url="https://${DOMAIN_NAME}" \
        --title="$WP_TITLE" \
        --admin_user="$WP_ADMIN_USER" \
        --admin_password="$WP_ADMIN_PASSWORD" \
        --admin_email="$WP_ADMIN_EMAIL" \
        --path=/var/www/html \
        --allow-root

    wp user create "$WP_USER" "$WP_USER_EMAIL" \
        --user_pass="$WP_USER_PASSWORD" \
        --role=author \
        --path=/var/www/html \
        --allow-root
fi

chown -R www-data:www-data /var/www/html
exec php-fpm8.2 -F
