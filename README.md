# API Task Creator

Crear proyectos y llevar la trazalidad del mismo.
# New Features!

  - Crear usuarios
  - Crear proyectos
  - Crear tareas

You can also:
  - Generar tokens de autenticación
  - Actualizar tokens
  - Autenticarse desde el admin

### Tech

Task creator usa las siguientes tecnologías:

* [Python] 
* [Django]
* [JSON web tokens]
* [Django restframework]

### Installation

Task creator corre en [python]3.5+.

Crear un [entorno virtual](https://help.dreamhost.com/hc/es/articles/115000695551-Instalar-y-usar-virtualenv-con-Python-3)
Instalar dependencias
```sh
$ cd task_creator
$ pip install -r requirements.txt
```

Correr migraciones
```sh
$ python manage.py migrate
```

Crear superuser
```sh
$ python manage.py createsuperuser
$ Username: oscles
$ Email address: admin@example.com
$ Password: **********
$ Password (again): *********
Superuser created successfully.
```

Correr proyecto
```sh
$ python manage.py runserver
```

### Endpoints
Cuando el proyecto este corriendo puedes ir al navegador y autenticarte en esta URL http://127.0.0.1:8000/api/
```js
{
    "users": "http://127.0.0.1:8000/api/users/",
    "tasks": "http://127.0.0.1:8000/api/tasks/",
    "projects": "http://127.0.0.1:8000/api/projects/"
}
```

#### Autenticación por token
URL: http://127.0.0.1:8000/api/token/
Method: POST
Body: ```js
{
    "username": "oscles",
    "password": "0203oscles",
}
```

Response: ```js
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU5NDMxNjMzMSwianRpIjoiNjYzMDc3ZTFiYWNkNDcwNWFiOGE4YmY0YTUyNWEyNzciLCJ1c2VyX2lkIjoxfQ.dLaMBqDkamxanMQ8T5XYFsUreXe9dkCaTeJn0u1Ut58",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTk0MjQwNzMxLCJqdGkiOiJkMjBjMzA1ODdhOWQ0NWYxOTViOTMyNThmYzE4N2EzYSIsInVzZXJfaWQiOjF9.3Hd6ptFPhQg5Bbmqz1WrLU05haXv5Pn0GMztQ3hkB8U",
    "user": {
        "id": 1,
        "username": "oscles",
        "first_name": "Osnaider",
        "last_name": "Miranda C",
        "email": "om.zina@nokia.com",
        "full_name": "Osnaider Miranda C"
    }
}
```



#### listar projects
http://127.0.0.1:8000/api/users/
```js
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "username": "oscles",
            "first_name": "Osnaider",
            "last_name": "Miranda C",
            "email": "om.zina@nokia.com",
            "full_name": "Osnaider Miranda C"
        },
        {
            "id": 2,
            "username": "wilatino",
            "first_name": "Wilberto",
            "last_name": "Alvarez",
            "email": "info@livex.com",
            "full_name": "Wilberto Alvarez"
        },
    ]
}
```

#### Crear project
Method: POST
url: http://127.0.0.1:8000/api/users/
Header: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTk0MjQwNzMxLCJqdGkiOiJkMjBjMzA1ODdhOWQ0NWYxOTViOTMyNThmYzE4N2EzYSIsInVzZXJfaWQiOjF9.3Hd6ptFPhQg5Bbmqz1WrLU05haXv5Pn0GMztQ3hkB8U
Body:
```js
{
    "username": "serGio",
    "first_name": "Sergio",
    "last_name": "Mercado",
    "email": "sergio@gmail.com",
    "password": "3002532*+6325"
}
```

