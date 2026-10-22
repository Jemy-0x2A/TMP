# User Documentation

## Provided Services
This infrastructure provides a WordPress website secured via HTTPS using NGINX and backed by a MariaDB database.

## Service Management
- **Start infrastructure**: `make`
- **Stop infrastructure**: `make down`
- **Clean containers and networks**: `make clean`
- **Full reset (including data volumes)**: `make fclean`

## Accessing the Application
1. Ensure your host `/etc/hosts` file routes `jebouffa.42.fr` to `127.0.0.1`.
2. Open your web browser and navigate to:
   - **Website**: `https://jebouffa.42.fr`
   - **WordPress Dashboard**: `https://jebouffa.42.fr/wp-admin`

## Credentials Management
Credentials and passwords are listed in text files inside the `./secrets/` directory on the host system.
