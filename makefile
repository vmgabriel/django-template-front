run:
	python manage.py runserver 0.0.0.0:8000


shell:
	python manage.py shell


prepare:
	make migrate
	mkdir static
	python manage.py collectstatic


migrate:
	python manage.py makemigrations
	python manage.py migrate


sass:
	python manage.py sass static/scss static/css --watch


heroku-local:
	heroku local


heroku-prod:
	heroku create
