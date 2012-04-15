A wrapper around the Trello API written in Python. Each Trello object is represented by a corresponding Python object. The attributes of these objects are cached, but the child objects are not. This can possibly be improved when the API allows for notification subscriptions; this would allow caching (assuming a connection was available to invalidate the cache as appropriate).

I've created a `Trello Board <https://trello.com/board/py-trello/4f145d87b2f9f15d6d027b53>`_ for feature requests, discussion and some development tracking. 

Install
=======

    pip install py-trello

py-oauth2
=========

py-oauth2 works if you `apply this patch <https://github.com/tylerwilliams/python-oauth2/commit/e97b6a678ea6df38f0f1c33a5a7450714a72c38b>`_. To use 3-legged authentication, construct your Trello client as follows:

    client = Trello(api_key = '...', api_secret = '...', token = '...', token_secret = '...')

Where `token` and `token_secret` come from the 3-legged OAuth process. `api_key` and `api_secret`
are your Trello API credentials (`generated here <https://trello.com/1/appKey/generate>`_).

Required Python modules
=======================
* `httplib2 <http://code.google.com/p/httplib2/>`_

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

`Adrien Lemaire <https://github.com/Fandekasp>`_
