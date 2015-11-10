AUTHENTICATION_BACKENDS = (
    'auth.IntegratedBackend',
    'auth.MyBackend',
    'django.contrib.auth.backends.ModelBackend'
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'middleware.SSOIntegrationMiddleware',
)



