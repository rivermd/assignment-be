from dotenv import load_dotenv
import os

load_dotenv()

class Config(object):
    SECRET_KEY = 'drivera-secret-key'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URL = 'postgresql://{dyannarivera}:{11doctor}@{jseijas-pgsrv}/{drivera_prod_db}'.format(
    dbuser=os.getenv('DBUSER'),
    dbpass=os.getenv('DBPASS'),
    dbhost=os.getenv('DBHOST') + ".postgres.database.azure.com",
    dbname=os.getenv('DBNAME')
    )

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URL = 'postgresql://{dyannarivera}:{11doctor}@{jseijas-pgsrv}/{drivera_dev_db}'.format(
    dbuser=os.getenv('DBUSER'),
    dbpass=os.getenv('DBPASS'),
    dbhost=os.getenv('DBHOST'),
    dbname=os.getenv('DBNAME')
    )
    DEBUG = True

class GithubCIConfig(Config):
    SQLALCHEMY_DATABASE_URL = 'sqlite:///test.db'
    DEBUG = True