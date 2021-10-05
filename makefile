run:
	python manage.py runserver 0.0.0.0:8000


shell:
	python manage.py shell


migrate:
	python manage.py makemigrations
	python manage.py migrate


sass:
	python manage.py sass static/scss static/css --watch
