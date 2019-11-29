# -*- coding: utf-8 -*-
from __future__ import with_statement, print_function, absolute_import
import os
from requests_oauthlib import OAuth1Session


def create_oauth_token(expiration=None, scope=None, key=None, secret=None, name=None, output=True):
    """
    Script to obtain an OAuth token from Trello.

    Must have TRELLO_API_KEY and TRELLO_API_SECRET set in your environment
    To set the token's expiration, set TRELLO_EXPIRATION as a string in your
    environment settings (eg. 'never'), otherwise it will default to 30 days.

    More info on token scope here:
        https://trello.com/docs/gettingstarted/#getting-a-token-from-a-user
    """
    request_token_url = 'https://trello.com/1/OAuthGetRequestToken'
    authorize_url = 'https://trello.com/1/OAuthAuthorizeToken'
    access_token_url = 'https://trello.com/1/OAuthGetAccessToken'

    expiration = expiration or os.environ.get('TRELLO_EXPIRATION', "30days")
    scope = scope or os.environ.get('TRELLO_SCOPE', 'read,write')
    trello_key = key or os.environ['TRELLO_API_KEY']
    trello_secret = secret or os.environ['TRELLO_API_SECRET']
    name = name or os.environ.get('TRELLO_NAME', 'py-trello')

    # Step 1: Get a request token. This is a temporary token that is used for
    # having the user authorize an access token and to sign the request to obtain
    # said access token.

    session = OAuth1Session(client_key=trello_key, client_secret=trello_secret)
    response = session.fetch_request_token(request_token_url)
    resource_owner_key, resource_owner_secret = response.get('oauth_token'), response.get('oauth_token_secret')

    if output:
        print("Request Token:")
        print("    - oauth_token        = %s" % resource_owner_key)
        print("    - oauth_token_secret = %s" % resource_owner_secret)
        print("")

    # Step 2: Redirect to the provider. Since this is a CLI script we do not
    # redirect. In a web application you would redirect the user to the URL
    # below.

    print("Go to the following link in your browser:")
    print("{authorize_url}?oauth_token={oauth_token}&scope={scope}&expiration={expiration}&name={name}".format(
        authorize_url=authorize_url,
        oauth_token=resource_owner_key,
        expiration=expiration,
        scope=scope,
        name=name
    ))

    # After the user has granted access to you, the consumer, the provider will
    # redirect you to whatever URL you have told them to redirect to. You can
    # usually define this in the oauth_callback argument as well.

    # Python 3 compatibility (raw_input was renamed to input)
    try:
        inputFunc = raw_input
    except NameError:
        inputFunc = input

    accepted = 'n'
    while accepted.lower() == 'n':
        accepted = inputFunc('Have you authorized me? (y/n) ')
    oauth_verifier = inputFunc('What is the PIN? ')

    # Step 3: Once the consumer has redirected the user back to the oauth_callback
    # URL you can request the access token the user has approved. You use the
    # request token to sign this request. After this is done you throw away the
    # request token and use the access token returned. You should store this
    # access token somewhere safe, like a database, for future use.
    session = OAuth1Session(client_key=trello_key, client_secret=trello_secret,
                            resource_owner_key=resource_owner_key, resource_owner_secret=resource_owner_secret,
                            verifier=oauth_verifier)
    access_token = session.fetch_access_token(access_token_url)

    if output:
        print("Access Token:")
        print("    - oauth_token        = %s" % access_token['oauth_token'])
        print("    - oauth_token_secret = %s" % access_token['oauth_token_secret'])
        print("")
        print("You may now access protected resources using the access tokens above.")
        print("")

    return access_token

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
