# httpie-kong-hmac

HMAC auth plugin for [HTTPie](https://httpie.org/) and [Kong](https://konghq.com/)

It currently provides support for Kong Hmac


## Installation

```bash
$ pip install httpie-kong-hmac
```

## Usage

```bash
$ http --auth-type=kong-hmac --auth='client-key:client-secret' example.org
```

You can also use [HTTPie sessions](https://httpie.org/doc#sessions):
```bash
# Create session
$ http --session=logged-in --auth-type=kong-hmac --auth='client-key:client-secret' example.org

# Re-use auth
$ http --session=logged-in POST example.org hello=world
```

If you use [requests](https://github.com/kennethreitz/requests):

```python
from httpie_kong_hmac import KongHMAC
import requests

resp = requests.get('http://example.org',
             auth=KongHMAC('client-key','client-secret'),
        )
print(resp.status_code, resp.content)
```
