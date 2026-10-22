*This activity has been created as part of the 42 curriculum by jebouffa.*

## Description
This project sets up a small infrastructure composed of WordPress, MariaDB, and NGINX with TLS using Docker Compose inside a Virtual Machine.

## Project Description & Architecture
The stack consists of three isolated services running in dedicated Debian containers:
- **NGINX**: Serves as the unique entrypoint, listening strictly on port 443 with TLS v1.2/v1.3.
- **WordPress + PHP-FPM**: Handles application processing and communicates with MariaDB.
- **MariaDB**: Stores database records persistently.

## Technical Comparisons
- **Virtual Machines vs Docker**: Docker containers share the host Linux kernel, resulting in lightweight, resource-efficient virtualization with fast startup times compared to full hardware emulation in Virtual Machines.
- **Secrets vs Environment Variables**: Docker Secrets are mounted securely in memory (`/run/secrets/`) rather than exposed as process environment variables, avoiding sensitive leak exposure in Git or process inspection.
- **Docker Network vs Host Network**: A dedicated bridge network isolates inter-container communication, whereas host networking bypasses port isolation and exposes services directly to the host interface.
- **Docker Volumes vs Bind Mounts**: Named volumes are managed completely by Docker's storage engine (`data-root`), ensuring portable and strict persistence isolated from host path modifications.

## Instructions
Execute `make` at the repository root to start the entire infrastructure.

# Resources

* Inception subject
* Official Docker and Docker Compose documentation
* AI
* Pair learning with 42 school peers

## AI usage

AI was used as a learning and clarification tool throughout the project. I first manipulated the system myself, then asked questions about what I did not understand. I used AI to understand each concept and command step by step, then applied and verified it myself. The goal was to understand what I was doing rather than asking AI to do the project for me.
