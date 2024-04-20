DEBUG = False

USERNAME = 'root'
PASSWORD = 'your_key'
SERVER = 'localhost'
DB = 'name_database'

SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = True
