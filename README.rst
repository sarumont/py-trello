A wrapper around the Trello API written in Python. Each Trello object is
represented by a corresponding Python object. The attributes of these objects
are cached, but the child objects are not. This can possibly be improved when
the API allows for notification subscriptions; this would allow caching
(assuming a connection was available to invalidate the cache as appropriate).

I've created a `Trello Board <https://trello.com/board/py-trello/4f145d87b2f9f15d6d027b53>`_
for feature requests, discussion and some development tracking.

Install
=======

    pip install py-trello

Usage
=====

    from trello import TrelloClient

    client = TrelloClient(
        api_key='your-key',
        api_secret='your-secret',
        token='your-oauth-token-key',
        token_secret='your-oauth-token-secret'
    )

Where `token` and `token_secret` come from the 3-legged OAuth process and
`api_key` and `api_secret` are your Trello API credentials that are
(`generated here <https://trello.com/1/appKey/generate>`_).

Getting your Trello OAuth Token
===============================
Make sure the following environment variables are set:

* `TRELLO_API_KEY`
* `TRELLO_API_SECRET`

These are obtained from the link mentioned above.

`TRELLO_EXPIRATION` is optional. Set it to a string such as 'never' or '1day'.
Trello's default OAuth Token expiration is 30 days.

Default permissions are read/write.

More info on setting the expiration here:
https://trello.com/docs/gettingstarted/#getting-a-token-from-a-user

Run

    python ./trello/util.py

Required Python modules
=======================
Found in requirements.txt

Tests
=====
To run the tests, run `python tests.py`. Three environment variables must be set:

* TRELLO_API_KEY: your Trello API key
* TRELLO_TOKEN: your Trello OAuth token
* TRELLO_TEST_BOARD_COUNT: the number of boards in your Trello account
* TRELLO_TEST_BOARD_NAME: name of the board to test card manipulation on. Must be unique, or the first match will be used

And run (from `py-trello/`):

    PYTHONPATH=. python test/test_trello.py

Contributors
============

* `Adrien Lemaire <https://github.com/Fandekasp>`_
* `Kyle Valade <https://github.com/kdazzle>`_
* `Rick van Hattem <https://github.com/WoLpH>`_
* `Nathan Mustaki <https://github.com/nMustaki>`_
