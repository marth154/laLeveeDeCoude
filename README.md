# laLeveeDeCoude

### Create container :
docker-compose run web django-admin startproject lldc .


### When Models are created :
docker-compose run web python manage.py makemigrations
docker-compose run web python manage.py migrate


### Start project :
docker-compose up


### Stop project :
docker-compose down
