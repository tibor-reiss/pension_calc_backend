# pension_calc_backend
For the frontend, see pension_calc_frontend (https://github.com/tibor-reiss/pension_calc_frontend)

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
