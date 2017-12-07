A wrapper around the Trello API written in Python. Each Trello object is
represented by a corresponding Python object. The attributes of these objects
are cached, but the child objects are not. This can possibly be improved when
the API allows for notification subscriptions; this would allow caching
(assuming a connection was available to invalidate the cache as appropriate).

I've created a `Trello Board <https://trello.com/board/py-trello/4f145d87b2f9f15d6d027b53>`_
for feature requests, discussion and some development tracking.

Install
=======

::
    cd ~/path/py-trello/
    pip install .

Usage
=====

.. code-block:: python

    from trello import TrelloClient

    client = TrelloClient(
        api_key='your-key',
        api_token='your-secret',
    )

Where ``api_key`` and ``api_token`` are your Trello API credentials that are
(`generated here <https://trello.com/1/appKey/generate>`_).


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


Required Python modules
=======================

Found in ``requirements.txt``

Tests
=====

To run the tests, run ``python -m unittest discover``. Four environment variables must be set:

* ``TRELLO_API_KEY``: your Trello API key
* ``TRELLO_TEST_BOARD_COUNT``: the number of boards in your Trello account
* ``TRELLO_TEST_BOARD_NAME``: name of the board to test card manipulation on. Must be unique, or the first match will be used

To run tests across various Python versions,
`tox <https://tox.readthedocs.io/en/latest/>`_ is supported. Install it
and simply run ``tox`` from the ``py-trello`` directory.
