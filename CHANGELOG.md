

**v0.1.6**


[view](https://github.com/sarumont/py-trello/commit/aabe9be06cef056450e0d8508a3520081230ada7) &bull; Fixed setting attributes on the 5 readonly @property  
[view](https://github.com/sarumont/py-trello/commit/082135d37e509879c7d347c0a0f00adfceda2439) &bull; Refactored JSON deserialization for every class  
[view](https://github.com/sarumont/py-trello/commit/39f90849ec581eecb3d5b2f130b28dbf9c871278) &bull; Changed the due_date format in Card  
[view](https://github.com/sarumont/py-trello/commit/9919f254ebe6730cfcc021ab95f7a0740af4ba31) &bull; Rename an item for a Checklist.  
[view](https://github.com/sarumont/py-trello/commit/3e0369f12e74d980b50aa03cc10261422c80cb62) &bull; Rename header Content-type to Content-Type.  
[view](https://github.com/sarumont/py-trello/commit/4e23ca8b4e5440e008499010bd37f95e6aef86d6) &bull; Add setter to Card.description  
[view](https://github.com/sarumont/py-trello/commit/396ccb0c89272f3f77dd400fd7ba787da95cf653) &bull; Add members methods to Board class  
[view](https://github.com/sarumont/py-trello/commit/e643b20a4c4def904bb8b20d6f0921f43d05d5b4) &bull; rename to changelog  


**0.3.0**


[view](https://github.com/sarumont/py-trello/commit/ede0ceb10b1e08451767f2b709b52445ada72f37) &bull; use requests and requests-oauthlib to simplify code and make it Python 3 compatible  
[view](https://github.com/sarumont/py-trello/commit/9f2bdb11b63f370d4906f336b9c32bdbcca5646e) &bull; bumped version to 0.2.0, updated setup.py and requirements.txt  
[view](https://github.com/sarumont/py-trello/commit/2e3a1b1c7e8871fd0c4df0779a4d15e512e40143) &bull; added test for Board.get_cards and Card.delete -> 0.2.1  
[view](https://github.com/sarumont/py-trello/commit/03e7a276c899b8cb6d6fdaea49b42216f7ada51a) &bull; Extended test for Board.get_cards  
[view](https://github.com/sarumont/py-trello/commit/7862a2803fc46548244a51f2adc8827ea2bb8df9) &bull; Remove `get_list` from TrelloClient (closes #51)  
[view](https://github.com/sarumont/py-trello/commit/13b9bd8a5ec4f465528f9932dd6618c474b85b5f) &bull; Fix util.py for Python2  
[view](https://github.com/sarumont/py-trello/commit/987e01a5e6a89cbebd1719fd92998d475638d9aa) &bull; added property Card.date_last_activity : datetime, and test for fetching card attributes (including the new datetime property)  
[view](https://github.com/sarumont/py-trello/commit/166cd32fb089968d7a1c2ae12fe7bf09a611f5f6) &bull; Unified initialization of cards from JSON data. Added optionally lazy properties for comments and checklists.  
[view](https://github.com/sarumont/py-trello/commit/3e05f7bc17e592ca2f02c4510f6403bf047c206d) &bull; Python 2 fix (@henriquegemignani )  
[view](https://github.com/sarumont/py-trello/commit/ad0a8885c0923792afdb602173d10214c5499ec8) &bull; version bumped and dependency "dateutil" added  
[view](https://github.com/sarumont/py-trello/commit/2cfb79ef40891149ff87ecc5158c88991e35b0ef) &bull; Allow empty due dates  
[view](https://github.com/sarumont/py-trello/commit/f6d086aa0be14dd2f0c8d87e728939053408f2c9) &bull; Change requirement dateutil to python-dateutil.  
[view](https://github.com/sarumont/py-trello/commit/40ad8cdfc089490a05e08b5dce4be37d2d8bdab8) &bull; Fix python2 support (no annotations)  
[view](https://github.com/sarumont/py-trello/commit/9ec5b03d534a6dd022f1c33bc585721e535c534c) &bull; Add method get_card, fixes #62  
[view](https://github.com/sarumont/py-trello/commit/6d91f93e7e8f3842d26bb6d123b09be4a13c6d27) &bull; FIX: Inverted arguments  
[view](https://github.com/sarumont/py-trello/commit/4a6b7b49eeb5fc501e91f0a6093e15cc65fe2dd3) &bull; make util script executable  
[view](https://github.com/sarumont/py-trello/commit/1eb662bc6d77b3e84439e1de9540ef39ce275b3e) &bull; Add shebang to util.py  
[view](https://github.com/sarumont/py-trello/commit/d6d9426fabe7e45fe9b6ead4241fb259e84bdc09) &bull; [NEW]: support attachments from file or url  
[view](https://github.com/sarumont/py-trello/commit/48bc38f34cefafe77c82f1a31297766b04a4a354) &bull; Added method to Card object to update card name  
[view](https://github.com/sarumont/py-trello/commit/ee43db90e65ddb909bced04f65c9cbdbc15ea3a8) &bull; fetch_checklists: allow the list to be empty  
[view](https://github.com/sarumont/py-trello/commit/f190aa54a6c4c81205230273c53242407a600eb2) &bull; added the rename method on Checklist  
[view](https://github.com/sarumont/py-trello/commit/69c051d32f7a8eb2534fafe9da652816ace2120f) &bull; added the delete method on Checklist  
[view](https://github.com/sarumont/py-trello/commit/b474c2d88a1283cd183730bbc387c46489640355) &bull; refactor tests to avoid code duplication and flake8 reports  
[view](https://github.com/sarumont/py-trello/commit/467325b7b992e8d562ab9aec0824ac5c6a4df116) &bull; raised coverage to 80%  
[view](https://github.com/sarumont/py-trello/commit/3ad391529d4defa969c2193e5769118145cc6ab1) &bull; Added support for Organizations  
[view](https://github.com/sarumont/py-trello/commit/75a907707d1272af08c9d109faf5285f8d90c34d) &bull; Fix Board.from_json call parameterization  
[view](https://github.com/sarumont/py-trello/commit/dde0404ff6621787af2191e9ad1710aa26cacd93) &bull; Add a default app name  
[view](https://github.com/sarumont/py-trello/commit/c7ef1a1c99d25dcd36f486b2df44e2b78da2e90e) &bull; Updated the create_oauth_token() function to include the ability to suppress printing the secrets and tokens, as well as returning the access tokens after the OAuth request.  
[view](https://github.com/sarumont/py-trello/commit/4e29cd29d13b872f26263bbb2d5ebf14eec6140c) &bull; Added open() to Boards and Lists  
[view](https://github.com/sarumont/py-trello/commit/3ff2cd98320dbc3f26a9b52eb9e0108fdfc74ff9) &bull; added due_date property  
[view](https://github.com/sarumont/py-trello/commit/8295665270c40b9462c5aa66ce74c3ce8f6b0e1a) &bull; handling pos attribute  
[view](https://github.com/sarumont/py-trello/commit/8f10e13aa67b7c5a40f7db14749d48a51ba7f983) &bull; Added the Label class and fixed the labels property to cards  
[view](https://github.com/sarumont/py-trello/commit/2a1916f4e67577a6ce2f541f2173d818758869a6) &bull; Added functionality to add a Label to a board  
[view](https://github.com/sarumont/py-trello/commit/94473299c8fc02881a475cda3822abb06e32afe7) &bull; Updated the from_json documentation to reflect the parent board as being on the arguments, as opposed to the Trello Client I had originally  
[view](https://github.com/sarumont/py-trello/commit/016dcc18f0696d2e4c65af9519222ebf86b9e463) &bull; Removed Board.open() and List.open() for the pull request  
[view](https://github.com/sarumont/py-trello/commit/b080626d11b17f3043369fd0b6914f4408219591) &bull; Added the ability to add a label on card creation. Added a call to add a label to a card directly. Added a call to get all labels for a board  
[view](https://github.com/sarumont/py-trello/commit/6665de3d87875e91c77efe42f8e55f2edff9fd3e) &bull; Added the ability to archive all cards, and add a due date on a card. Additionally, I updated creating a new card to use the Card path instead of the List path, since it allows for adding Labels by ID instead of by color  
[view](https://github.com/sarumont/py-trello/commit/a389301b118e388872099dfab12d064ab37f1e54) &bull; added sphinx docs  
[view](https://github.com/sarumont/py-trello/commit/9f7ee5e048f24f64f0ba300aae36b2f811508e49) &bull; improved docs slightly  
[view](https://github.com/sarumont/py-trello/commit/d43ba4acd4b4f74bce32656458f676b07afdbee8) &bull; improved docs slightly  
[view](https://github.com/sarumont/py-trello/commit/9b0f462300a243e00168d9d4c706850904732227) &bull; improved docs slightly  
[view](https://github.com/sarumont/py-trello/commit/4629969e991d05aae4e148abf86f2101a27369c4) &bull; card might be initialized with either board or list  
[view](https://github.com/sarumont/py-trello/commit/a70156a0f174d40610e369cb9e4f977d58932ef0) &bull; card labels are returned as Label class instead of dicts  
[view](https://github.com/sarumont/py-trello/commit/69a4877f02c29955ca10c949ba42845bad0def1a) &bull; setUp -> setUpClass  
[view](https://github.com/sarumont/py-trello/commit/bae80fc089aa29fee8e1355942d03d9339fc91b5) &bull; added list to card  
[view](https://github.com/sarumont/py-trello/commit/3a8232967e1b716cc8ab73872b7a13e842188fa0) &bull; Remove unused Member.commentCard attribute  
[view](https://github.com/sarumont/py-trello/commit/bd839071763cd4c2a1999c74cb54e4bb6ce5b665) &bull; Fix docstring typo in Member.fetch()  
