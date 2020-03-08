install:
	pip install -r requirements.txt

build:
	python manage.py migrate
	python manage.py createsuperuser

load_data:
	python manage.py loaddata games.json
	python manage.py loaddata directors.json
	python manage.py loaddata genres.json
	python manage.py loaddata platforms.json
	python manage.py loaddata screenshots.json

serve:
	python manage.py runserver

dump_data:
	python manage.py dumpdata resources.game > resources/fixtures/games.json --indent 4
	python manage.py dumpdata resources.director > resources/fixtures/directors.json --indent 4
	python manage.py dumpdata resources.genre > resources/fixtures/genres.json --indent 4
	python manage.py dumpdata resources.platform > resources/fixtures/platforms.json --indent 4
	python manage.py dumpdata resources.screenshot > resources/fixtures/screenshots.json --indent 4

drop_db:
	python manage.py flush

test:
	python manage.py test

clear_cache:
	python manage.py clear_cache
