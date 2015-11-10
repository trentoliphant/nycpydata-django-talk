from django.contrib.auth.models import User

class IntegratedBackend(object):

    def authenticate(self, **credentials):
        username = credentials.get('STANDARDID')
        first_name = credentials.get('FIRSTNAME')
        last_name = credentials.get('LASTNAME')
        email = credentials.get('EMAIL')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = User(username=username,
                        password='Using external login',
                        first_name=first_name,
                        last_name=last_name,
                        email=email,
                        is_active=False)
            user.save()
        if not user.is_active:
            user = None
        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

class MyBackend(object):
    def authenticate(self, username=None, password=None):
        # Check the username/password and return a User.
        return User.objects.get(username=username)

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
