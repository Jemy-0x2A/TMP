FROM debian:bookworm

RUN apt-get update && apt-get install -y \
    php8.2-fpm php8.2-mysql php8.2-curl php8.2-gd \
    php8.2-mbstring php8.2-xml php8.2-zip curl mariadb-client \
    && rm -rf /var/lib/apt/lists/* \
    && sed -i 's|listen = /run/php/php8.2-fpm.sock|listen = 9000|' /etc/php/8.2/fpm/pool.d/www.conf

RUN mkdir -p /var/www/html /run/php \
    && curl -fsSL https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar -o /usr/local/bin/wp \
    && chmod +x /usr/local/bin/wp

COPY tools/init.sh /usr/local/bin/init.sh
RUN chmod +x /usr/local/bin/init.sh

EXPOSE 9000
ENTRYPOINT ["/usr/local/bin/init.sh"]
