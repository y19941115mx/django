run:
	docker-compose exec victor_web python manage.py makemigrations
	docker-compose exec victor_web python manage.py migrate
	docker-compose exec victor_web python manage.py createsuperuser
import:
	docker-compose exec victor_mysql mysql -h localhost -u root -proot
