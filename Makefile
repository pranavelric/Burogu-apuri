build:
	docker build --force-rm ${options} -t burogu-apuri:latest .
compose-start:
	docker-compose up --remove-orphans ${options}

compose-stop:
	docker-compose down --remove-orphans ${options}

compose-manage-py:
	docker-compose run --rm $(options) website python manage.py $(cmd)