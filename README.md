# Api Rest from the junior company [Emakers]

## Technologies utilized
* Django 2.0.7
* Python 3.5.3
* Postgres 9.6.4

## Installation

Any Operating System:

```sh
virtualenv -p /usr/bin/python3 emakers-env

source emakers-env/bin/activate

pip install -r requeriments.txt

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

access http://localhost:8000/api/
```