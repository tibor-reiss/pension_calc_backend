# pension_calc_backend

## Project setup
```
poetry install
poetry run python manage.py makemigrations
poetry run python manage.py migrate
poetry run python manage.py createsuperuser
```

### Deployment
```
poetry run python manage.py runserver
```

### Testing
```
poetry run pytest
```
