import oauth2 as oauth

def test_oauth():

	request_token_url = 'https://trello.com/1/OAuthGetRequestToken'
	authorize_url = 'https://trello.com/1/OAuthAuthorizeToken'
	access_token_url = 'https://trello.com/1/OAuthGetAccessToken'

	consumer = oauth.Consumer(consumer_key, consumer_secret)
	client = oauth.Client(consumer)

	# Step 1: Get a request token. This is a temporary token that is used for 
	# having the user authorize an access token and to sign the request to obtain 
	# said access token.

	resp, content = client.request(request_token_url, "GET")
	if resp['status'] != '200':
		raise Exception("Invalid response %s." % resp['status'])

	request_token = dict(urlparse.parse_qsl(content))

	print "Request Token:"
	print "    - oauth_token        = %s" % request_token['oauth_token']
	print "    - oauth_token_secret = %s" % request_token['oauth_token_secret']
	print 

	# Step 2: Redirect to the provider. Since this is a CLI script we do not 
	# redirect. In a web application you would redirect the user to the URL
	# below.

	print "Go to the following link in your browser:"
	print "%s?oauth_token=%s&scope=read,write,comment" % (authorize_url, request_token['oauth_token'])
	print 

	# After the user has granted access to you, the consumer, the provider will
	# redirect you to whatever URL you have told them to redirect to. You can 
	# usually define this in the oauth_callback argument as well.
	accepted = 'n'
	while accepted.lower() == 'n':
		accepted = raw_input('Have you authorized me? (y/n) ')
	oauth_verifier = raw_input('What is the PIN? ')

	# Step 3: Once the consumer has redirected the user back to the oauth_callback
	# URL you can request the access token the user has approved. You use the 
	# request token to sign this request. After this is done you throw away the
	# request token and use the access token returned. You should store this 
	# access token somewhere safe, like a database, for future use.
	token = oauth.Token(request_token['oauth_token'],
		request_token['oauth_token_secret'])
	token.set_verifier(oauth_verifier)
	client = oauth.Client(consumer, token)

	resp, content = client.request(access_token_url, "POST")
	access_token = dict(urlparse.parse_qsl(content))

	print "Access Token:"
	print "    - oauth_token        = %s" % access_token['oauth_token']
	print "    - oauth_token_secret = %s" % access_token['oauth_token_secret']
	print
	print "You may now access protected resources using the access tokens above." 
	print
