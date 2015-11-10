import yaml
from django.contrib.auth import authenticate, login, logout

class SSOIntegrationMiddleware(object):

    header_fields = ['STANDARDID','FIRSTNAME','LASTNAME','EMAIL']

    def process_request(self, request):
        headers = {x:request.META.get(x) for x in self.header_fields}
        if not (request.user.username == request.META.get('STANDARDID')):
            logout(request)
        if not request.user.is_authenticated():
            user = authenticate(**headers)
            if user is not None:
                login(request, user)

        return None


class SSOWithMockMiddleware(object):

    header_fields = ['STANDARDID','FIRSTNAME','LASTNAME','EMAIL']

    def process_request(self, request):
        if not request.META.get('STANDARDID'):
            headers = self._get_mocked_headers()
            request.META.update(headers)
        else:
            headers = {x:request.META.get(x) for x in self.header_fields}
        if not (request.user.username == request.META.get('STANDARDID')):
            logout(request)
        if not request.user.is_authenticated():
            user = authenticate(**headers)
            if user is not None:
                login(request, user)

        return None

    def _get_mocked_headers(self):
        headers = None
        with open('ssomock.yaml','r') as f:
            raw = yaml.load(f)
            active = raw.get('active')
            if active:
                headers = raw.get(active)
        return headers

