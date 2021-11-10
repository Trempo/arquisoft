import requests
from social_core.backends.oauth import BaseOAuth2

class Auth0(BaseOAuth2):
    name = 'auth0'
    SCOPE_SEPARATOR = ' '
    ACCESS_TOKEN_METHOD = 'POST'
    EXTRA_DATA = [
        ('picture', 'picture')
    ]

    def authorization_url(self):
        return 'https://' + self.setting('DOMAIN') + '/authorize'

    def access_toke_url(self):
        return 'https://' + self.setting('DOMAIN') + '/oauth/token'

    def get_user_id(self, details, response):
        return response['user_id']

    def get_user_details(self, response):
        url = 'https://' + self.setting('DOMAIN') + '/userinfo'
        headers = {'Authorization': 'Bearer ' + response['access_token']}
        resp = requests.get(url, headers=headers)
        userinfo = resp.json()

        return {'username': userinfo['nickname'],
                'email': userinfo['email'],
                'picture': userinfo['picture'],
                'user_id': userinfo['sub']}


    def getRole(request):
        user = request.user
        auth0user = user.social_auth.get(provider='auth0')
        accessToken = auth0user.extra_data['access_token']
        url = 'https://isis2503-trempo.us.auth0.com/userinfo'
        headers = {'Authorization': 'Bearer ' + accessToken}
        resp = requests.get(url, headers=headers)
        userinfo = resp.json()
        role = userinfo('https://isis2503-trempo.us.auth0.com/role')
        return role