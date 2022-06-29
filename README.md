## Introduction:

The Django REST blog project task.

## How to setup the project:

Clone the repository:

```bash
git clone https: // github.com / MehdiAria / rest - task
```

Create a virtual environment and activated it:

```bash
python -m venv venv
source venv/bin/activate
```

Install requirements:

```bash
pip install -r requirements.txt
```

Database:

```bash
python manage.py makemigrations
python manage.py migrate
```

Create a superuser:

```bash
python manage.py createsuperuser
```

Run the server:

```bash
python manage.py runserver
```

## Endpoints:

### Swagger:

```bash
http://127.0.0.1:8000/swagger/
```

### Post list API:

```bash
http://127.0.0.1:8000/api/posts
```

### Create a rate/vote:

```bash
POST http://127.0.0.1:8000/api/posts/rate
```
