export DOCKER_DEFAULT_PLATFORM=linux/amd64

up:
	sudo docker compose up -d

down:
	sudo docker compose down --remove-orphans