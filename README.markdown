A basic API into Trello

# Required Python modules
* httplib2 (http://code.google.com/p/httplib2/)

# Tests
To run the tests, run `python tests.py`. Three environment variables must be set:

* TRELLO_API_KEY: your Trello API key
* TRELLO_TOKEN: your Trello OAuth token
* TRELLO_TEST_BOARD_COUNT: the number of boards in your Trello account
* TRELLO_TEST_BOARD_NAME: name of the board to test card manipulation on. Must be unique, or the first match will be used
