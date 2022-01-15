build:
	docker build --force-rm ${options} -t burogu-apuri:latest .
compose-start:
	docker-compose up --remove-orphans ${options}