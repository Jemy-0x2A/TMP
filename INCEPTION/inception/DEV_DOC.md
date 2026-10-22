# Developer Documentation

## Development Prerequisites
- Linux OS with Docker Engine and Docker Compose V2 installed.
- Docker daemon configured with `"data-root": "/home/jebouffa/data/docker"` in `/etc/docker/daemon.json`.
- Secrets created inside the `./secrets/` directory (`db_root_password.txt`, `db_password.txt`, `wp_admin_password.txt`, `wp_user_password.txt`).

## Environment Variables
The environment variables are stored in `srcs/.env`:
- `DOMAIN_NAME`: Domain configuration (`jebouffa.42.fr`)
- `DB_NAME`, `DB_USER`: MariaDB configuration parameters
- `WP_TITLE`, `WP_ADMIN_USER`, `WP_ADMIN_EMAIL`, `WP_USER`, `WP_USER_EMAIL`: WordPress parameters

## Container & Volume Inspection
- List running containers: `docker ps`
- Inspect network: `docker network inspect srcs_inception`
- Inspect volumes: `docker volume ls`
- Persistent data root path: `/home/jebouffa/data/`
