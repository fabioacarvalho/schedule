# Schedule

## First Step:

Create a file called `local_settings.py` after, add your settings, for example:

```python
DEBUG = True

USERNAME = 'root'
PASSWORD = 'your_key'
SERVER = 'localhost'
DB = 'name_database'

SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = True
```

<br>

## Second Step:

1 - Install requirements:

<br>

```shell
pip install -r requirements.txt
```

<br>

2 - Migrate and Update DB:

<br>

```shell
flask db init
flask db migrate
flask db upgrade
```

<br>

3 - Run Application

<br>

```shell
python run.py
```

<br>