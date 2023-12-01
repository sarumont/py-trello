A wrapper around the Trello API written in Python. Each Trello object is
represented by a corresponding Python object. The attributes of these objects
are cached, but the child objects are not. This can possibly be improved when
the API allows for notification subscriptions; this would allow caching
(assuming a connection was available to invalidate the cache as appropriate).

Install
=======

::

    pip install ha-py-trello

Usage
=====

.. code-block:: python

    from trello import TrelloClient

    client = TrelloClient(
        api_key='your-key',
        api_secret='your-secret',
        token='your-oauth-token-key',
        token_secret='your-oauth-token-secret'
    )

Where ``token`` and ``token_secret`` come from the 3-legged OAuth process and
``api_key`` and ``api_secret`` are your Trello API credentials that are
(`generated here <https://trello.com/1/appKey/generate>`_).

To use without 3-legged OAuth, use only ``api_key`` and ``api_secret`` on client.

Working with boards
--------------------

.. code-block:: python

    all_boards = client.list_boards()
    last_board = all_boards[-1]
    print(last_board.name)

working with board lists and cards
----------------------------------

.. code-block:: python

    all_boards = client.list_boards()
    last_board = all_boards[-1]
    last_board.list_lists()
    my_list = last_board.get_list(list_id)

    for card in my_list.list_cards():
        print(card.name)


Getting your Trello OAuth Token
===============================
Make sure the following environment variables are set:

* ``TRELLO_API_KEY``
* ``TRELLO_API_SECRET``

These are obtained from the link mentioned above.

``TRELLO_EXPIRATION`` is optional. Set it to a string such as 'never' or '1day'.
Trello's default OAuth Token expiration is 30 days.

Default permissions are read/write.

More info on setting the expiration here:
https://trello.com/docs/gettingstarted/#getting-a-token-from-a-user

Run

::

    python -m trello oauth

Required Python modules
=======================

Found in ``requirements.txt``

Tests
=====

To run the tests, run ``python -m unittest discover``. Four environment variables must be set:

* ``TRELLO_API_KEY``: your Trello API key
* ``TRELLO_TOKEN``: your Trello OAuth token

*NOTE*: **It's recommended to create a separate Trello account for testing. While the tests try to only modify or delete
resources they've created, to remove all possibility of unintentional data loss, we recommend not using a personal
Trello account with existing data.**

To run tests across various Python versions,
`tox <https://tox.readthedocs.io/en/latest/>`_ is supported. Install it
and simply run ``tox`` from the ``ha-py-trello`` directory.

## Publishing
To publish, simply create a release on GitHub and a workflow will kick off to publish to PyPI. If you'd like to publish
locally, follow the below instructions.

First ensure the appropriate tools are installed locally:
```shell
python3 -m pip install --upgrade build
python3 -m pip install --upgrade twine
```
Then build and publish:
```shell
python3 -m build
python3 -m twine upload dist/*
```
For more information see the [official packaging and publishing docs](https://packaging.python.org/en/latest/tutorials/packaging-projects).

---
*Forked from original: https://github.com/sarumont/py-trello*
