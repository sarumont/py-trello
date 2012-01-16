A wrapper around the Trello API written in Python. Each Trello object is represented by a
corresponding Python object. The attributes of these objects are cached, but the child objects are
not. This can possibly be improved when the API allows for notification subscriptions; this would
allow caching (assuming a connection was available to invalidate the cache as appropriate).

I've created a Trello Board for feature requests, discussion and some development tracking. It can
be found [here] (https://trello.com/board/py-trello/4f145d87b2f9f15d6d027b53 "Trello")

## Required Python modules
* httplib2 (http://code.google.com/p/httplib2/)

## Tests
To run the tests, run `python tests.py`. Three environment variables must be set:

* TRELLO_API_KEY: your Trello API key
* TRELLO_TOKEN: your Trello OAuth token
* TRELLO_TEST_BOARD_COUNT: the number of boards in your Trello account
* TRELLO_TEST_BOARD_NAME: name of the board to test card manipulation on. Must be unique, or the first match will be used
