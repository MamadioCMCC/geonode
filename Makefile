up:
	# bring up the services
	docker-compose up -d

build:
	docker pull python:2.7.9
	docker build -t camptocamp/geonode_django:latest .
	docker build -t camptocamp/geonode_django:`date +%Y%m%d%H%M%S` .

sync: up
	# set up the database tables
	docker-compose exec django django-admin.py makemigrations --noinput
	docker-compose exec django django-admin.py migrate account --noinput
	docker-compose exec django django-admin.py migrate --noinput
	docker-compose exec django django-admin.py loaddata sample_admin

wait:
	sleep 5

logs:
	docker-compose logs --follow

down:
	docker-compose down

pull:
	docker-compose pull

smoketest: up
	docker-compose exec django python manage.py test geonode.tests.smoke --nocapture --detailed-errors --verbosity=1 --failfast

unittest: up
	docker-compose exec django python manage.py test geonode.people.tests geonode.base.tests geonode.layers.tests geonode.maps.tests geonode.proxy.tests geonode.security.tests geonode.social.tests geonode.catalogue.tests geonode.documents.tests geonode.api.tests geonode.groups.tests geonode.services.tests geonode.geoserver.tests geonode.upload.tests geonode.tasks.tests --noinput --failfast

test: smoketest unittest

clear:
	docker volume rm labsgeonode_elasticsearch_data labsgeonode_geoserver_data labsgeonode_geoserver_datadir labsgeonode_postgresql_data labsgeonode_rabbitmq_data

reset: down clear up wait sync

#~ hardreset: pull build reset
hardreset: build reset
