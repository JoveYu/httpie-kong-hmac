httpie-kong-hmac
================

OAuth plugin for `HTTPie <https://httpie.org/>`_.

It currently provides support for Kong Hmac


Installation
------------

.. code-block:: bash

    $ pip install httpie-kong-hmac



Usage
-----

.. code-block:: bash

    $ http --auth-type=kong-hmac --auth='client-key:client-secret' example.org


You can also use `HTTPie sessions <https://httpie.org/doc#sessions>`_:

.. code-block:: bash

    # Create session
    $ http --session=logged-in --auth-type=kong-hmac --auth='client-key:client-secret' example.org

    # Re-use auth
    $ http --session=logged-in POST example.org hello=world

