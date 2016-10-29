# Test Rappi - Django - Angular 2

### Requerimientos

* Python 3.5.x
* Django 1.10.x
* Django Rest Framework
* Psycopg2
* Django csvImporter
* Angular CLI

### Installation

### Python 3.5.x

Entrar a https://www.python.org/downloads y descargar la versión 3.5.x que se ajuste a su sistema operativo.

### Django 1.10.x

De acuerdo a la documentación en: https://www.djangoproject.com/download/

```sh
$ pip install Django==1.10.2
```
### Django Rest Framework

De acuerdo a la documentación en: http://www.django-rest-framework.org/#installation

```sh
$ pip install pip install djangorestframework
```
### Psycopg2

```sh
$ pip install psycopg2
```

### Django csvImporter

De acuerdo a la documentación en: https://django-csv-importer.readthedocs.io/en/latest/#

```sh
$ pip install csvImporter
```

### Angular CLI

```sh
$ npm install -g angular-cli
```
Instalar las dependencias del proyecto Angular2

```sh
$ cd horarios/static/horario-app/
$ sudo npm install
```
El proyecto Angular2 está referenciado en la versión build, en caso de hacer un cambio en el proyecto Angular2 y reflejarlo en el projecto de Django ejecutar:

```sh
$ cd horarios/static/horario-app/
$ ng build
```

### Configuración del proyecto

Editar el archivo test_rappi/settings.py:
```sh
$ vim test_rappi/settings.py
```
y ajustar los parámetros de conexión a la base de datos en el parámetro DATABASES

### NOTA:
Se necesitan aplicar los siguientes parches al módulo csvImporter para que funcione con Python3:
https://github.com/anthony-tresontani/csv_importer/pull/4/commits

https://github.com/anthony-tresontani/csv_importer/pull/5/commits

Importar base de datos principal (admin)
```sh
$ python ./manage.py migrate
```

Importar la base de datos horario
```sh
$ python ./manage.py migrate horarios --database=scheduler_db
```

Ejecutar el server para cargar la aplicación
```sh
$ python ./manage.py runserver
```