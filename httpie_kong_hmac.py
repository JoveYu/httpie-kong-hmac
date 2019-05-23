
import datetime
import hashlib
import base64
import hmac

from httpie.plugins import AuthPlugin

__version__ = '0.0.2'
__author__ = 'Jove Yu'
__license__ = 'MIT'

class KongHMAC:
    def __init__(self, username, password, algorithm='hmac-sha256',
                 headers=['request-line', 'date', 'digest'], charset='utf-8'):
        self.username = username
        self.password = password
        self.algorithm = algorithm
        self.headers = headers
        self.charset = charset

        self.auth_template = 'hmac username="{}", algorithm="{}", headers="{}", signature="{}"'

    def __call__(self, r):

        # add Date header
        if 'date' in self.headers and 'Date' not in r.headers:
            r.headers['Date'] = self.create_date_header()

        # add Digest header
        if 'digest' in self.headers and r.body:
            r.headers['Digest'] = 'SHA-256={}'.format(self.get_body_digest(r))
        else:
            self.headers.remove('digest')

        # get sign
        sign = self.get_sign(r)
        r.headers['Authorization'] = self.auth_template.format(self.username,
                            self.algorithm, ' '.join(self.headers), sign)

        return r

    def create_date_header(self):
        now = datetime.datetime.utcnow()
        return now.strftime('%a, %d %b %Y %H:%M:%S GMT')

    def get_sign(self, r):
        sign = ''
        for h in self.headers:
            if h == 'request-line':
                sign += '{} {} HTTP/1.1'.format(r.method, r.path_url)
            else:
                sign += '{}: {}'.format(h, r.headers[h.title()])
            sign += '\n'

        h = hmac.new(self.password.encode(self.charset), sign[:-1].encode(self.charset),
                     getattr(hashlib, self.algorithm[5:]))
        return base64.b64encode(h.digest()).decode(self.charset)

    def get_body_digest(self, r):
        if r.body:
            h = hashlib.sha256(r.body)
            return base64.b64encode(h.digest()).decode(self.charset)
        return ''


class KongHMACPlugin(AuthPlugin):
    name = 'Kong HMAC auth plugin'
    auth_type = 'kong-hmac'
    description = 'Sign requests using HMAC authentication method for Kong API gateway'

    def get_auth(self, username='', password=''):
        return KongHMAC(username, password)

