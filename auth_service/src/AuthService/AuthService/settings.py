import os


# Tornado settings
DEBUG = int(os.environ.get("DEBUG", default=0))
XSRF_COOKIES = True
COOKIE_SECRET = os.environ.get("COOKIE_SECRET")
LOGIN_URL = "/login"
STATIC_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static")

# Database connection settings
DB_ENGINE = os.environ.get("DB_ENGINE")
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")

# SQLAlchemy settings
SQLALCHEMY_DB_URL = f"{DB_ENGINE}://{DB_USER}:{DB_PASSWORD}@" \
                    f"{DB_HOST}:{DB_PORT}/{DB_NAME}"

AUTH_SERVICE_DOMAIN = os.environ.get("AUTH_SERVICE_DOMAIN")
PRIVATE_KEY = os.environ.get("PRIVATE_KEY")
PUBLIC_KEY = os.environ.get("PUBLIC_KEY")
JWT_EXP_IN_MINUTES = int(os.environ.get("JWT_EXP_IN_MINUTES"))
