"""
Django settings for CLeagueHero project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g%#ddae0ql&_^tfh*ly)m+#&+7ho9&y_5clh7uf#+))0-88!%q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'social.apps.django_app.default',
    'arenas',
    'players'
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'CLeagueHero.urls'

WSGI_APPLICATION = 'CLeagueHero.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    'default': {
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # Or path to database file if using sqlite3.
        'NAME': 'CLeagueHero',
        # The following settings are not used with sqlite3:
        'USER': 'postgres',
        'PASSWORD': '',
        # Empty for localhost through domain sockets or
        # '127.0.0.1' for localhost through TCP.
        'HOST': 'localhost',
        'PORT': '5433',                      # Set to empty string for default.
    }
}


SOCIAL_AUTH_STRATEGY = 'social.strategies.django_strategy.DjangoStrategy'
SOCIAL_AUTH_STORAGE = 'social.apps.django_app.default.models.DjangoStorage'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    "django.core.context_processors.request",
    'django.contrib.messages.context_processors.messages',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect'
)

AUTHENTICATION_BACKENDS = (
    # 'social.backends.facebook.FacebookAppOAuth2',
    'social.backends.facebook.FacebookOAuth2',
)

AUTH_USER_MODEL = 'arenas.CustomUser'

SOCIAL_AUTH_LOGIN_URL = '/logged/'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/arenas/'
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/done/'
URL_PATH = ''

SOCIAL_AUTH_STRATEGY = 'social.strategies.django_strategy.DjangoStrategy'
SOCIAL_AUTH_STORAGE = 'social.apps.django_app.default.models.DjangoStorage'

# SOCIAL_AUTH_EMAIL_FORM_URL = '/signup-email'
SOCIAL_AUTH_EMAIL_FORM_HTML = 'email_signup.html'
SOCIAL_AUTH_EMAIL_VALIDATION_FUNCTION = 'example.app.mail.send_validation'
SOCIAL_AUTH_EMAIL_VALIDATION_URL = '/email-sent/'
# SOCIAL_AUTH_USERNAME_FORM_URL = '/signup-username'
SOCIAL_AUTH_USERNAME_FORM_HTML = 'username_signup.html'

# Facebook Auth
#SOCIAL_AUTH_FACEBOOK_KEY = '716658848463245'
#SOCIAL_AUTH_FACEBOOK_SECRET = '65516a62ef936d3d78aec628ae85cc98'


# Facebook Auth Dev
SOCIAL_AUTH_FACEBOOK_KEY = '732845866844543'
SOCIAL_AUTH_FACEBOOK_SECRET = '292242ebf39c71f93790c2c809e304a2'

# in case we need more permissions
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

# for more facebook data
# SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {'locale': 'ru_RU'}


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.mail.mail_validation',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.debug.debug',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
    'social.pipeline.debug.debug'
)

SOCIAL_AUTH_DISCONNECT_PIPELINE = (
    # Verifies that the social association can be disconnected from the current
    # user (ensure that the user login mechanism is not compromised by this
    # disconnection).
    'social.pipeline.disconnect.allowed_to_disconnect',

    # Collects the social associations to disconnect.
    'social.pipeline.disconnect.get_entries',

    # Revoke any access_token when possible.
    'social.pipeline.disconnect.revoke_tokens',

    # Removes the social associations.
    'social.pipeline.disconnect.disconnect'
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

# Parse database configuration from $DATABASE_URL
# import dj_database_url
# DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
import os
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
