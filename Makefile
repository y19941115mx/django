docker-compose exec victor_imooc /usr/local/bin/python manage.py makemigrations
docker-compose exec victor_imooc /usr/local/bin/python manage.py migrate
docker-compose exec victor_imooc /usr/local/bin/python manage.py runserver