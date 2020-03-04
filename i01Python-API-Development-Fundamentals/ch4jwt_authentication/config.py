from os import environ


class Config:
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{pwd}@{host}/{database}'.format(
        user=environ.get('DB_USER', 'root'),
        pwd=environ.get('MYSQLCONNSTR_DB_PWD', ''),
        host=environ.get('DB_HOST', 'localhost'),
        database=environ.get('DB_NAME', 'smilecook')
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = 'super-secret-key'
    JWT_ERROR_MESSAGE_KEY = 'message'
    # https://stackoverflow.com/questions/56281886/api-with-flask-jwt-extended-with-authentication-problems
    PROPAGATE_EXCEPTIONS = True