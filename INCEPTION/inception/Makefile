NAME = inception
COMPOSE = docker compose --env-file srcs/.env -f srcs/docker-compose.yml
DATA_DIR = /home/jebouffa/data

all: prepare
	$(COMPOSE) up -d --build

prepare:
	@mkdir -p $(DATA_DIR)

build: prepare
	$(COMPOSE) build

up: prepare
	$(COMPOSE) up -d

down:
	$(COMPOSE) down

clean:
	$(COMPOSE) down --volumes

fclean: clean
	@docker system prune -af
	@sudo rm -rf $(DATA_DIR)/*

re: fclean all

.PHONY: all prepare build up down clean fclean re
