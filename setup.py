from setuptools import setup

import httpie_kong_hmac

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='httpie-kong-hmac',
    description='Kong Hmac plugin for HTTPie.',
    long_description = long_description,
    long_description_content_type='text/markdown',
    version=httpie_kong_hmac.__version__,
    author=httpie_kong_hmac.__author__,
    author_email='yushijun110@126.com',
    license=httpie_kong_hmac.__license__,
    url='https://github.com/JoveYu/httpie-kong-hmac',
    py_modules=['httpie_kong_hmac'],
    zip_safe=False,
    entry_points={
        'httpie.plugins.auth.v1': [
            'httpie_kong_hmac = httpie_kong_hmac:KongHMACPlugin'
        ]
    },
    install_requires=[
        'httpie>=0.9.7'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Intended Audience :: Developers',
        'Environment :: Plugins',
        'License :: OSI Approved :: BSD License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Utilities'
    ],
)
