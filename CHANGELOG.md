

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


**v0.3.1**


[view](https://github.com/sarumont/py-trello/commit/c572b91998b34c26df4827a75335858638070d7c) &bull; bump version since I forgot to sign  


**v0.4.0**


[view](https://github.com/sarumont/py-trello/commit/daa7faf95fdeee6ecb146f8ad9488af88a3e1ee9) &bull; Revert "Removed Board.open() and List.open() for the pull request"  
[view](https://github.com/sarumont/py-trello/commit/b0f91c603e3f8e6c5774a177cec2a9b16ab27884) &bull; datetime.strptime -> dateparser.parse  
[view](https://github.com/sarumont/py-trello/commit/84a85709215284f686d44cfa80e5ece9551de3e2) &bull; The fields 'status' and 'initials' appear optional  
[view](https://github.com/sarumont/py-trello/commit/66fbb599338c1bb18d8975a444a541b3a523ee75) &bull; Use hour, min, sec to help deal with TZ issues  
[view](https://github.com/sarumont/py-trello/commit/b5ba124fb596dd8b8c260443ebaf2a0905337836) &bull; Don't error out if no due date  
[view](https://github.com/sarumont/py-trello/commit/a39b61eb6c6cb7a6e8f7374f0e13a109a04c7dc7) &bull; Add ability to subscribe to a card  
[view](https://github.com/sarumont/py-trello/commit/b45ca356b4c9db69e6209e56abfff5d95c370715) &bull; broken code into multiple files  
[view](https://github.com/sarumont/py-trello/commit/89ba89a567fbfa0c13f5eddf48f91363b05112de) &bull; broken tests into multiple files + change board test list behavior (each run create a new list)  
[view](https://github.com/sarumont/py-trello/commit/ec9dba31a211b0fc49c8b4d97d37ea19309ee8e8) &bull; FIX saner way to deal with circular import between list/card  
[view](https://github.com/sarumont/py-trello/commit/da57e62be2cff901c3c9de17171e43205aa82ac2) &bull; Add myself to contributors list and cleanup setup.py  


**v0.4.1**


[view](https://github.com/sarumont/py-trello/commit/be01f34b77d6af794eda4609503b410f3230c1bb) &bull; Fix import bugs + bug in tests for card due date  
[view](https://github.com/sarumont/py-trello/commit/abe08b6cc106e81443a52064f4a3c458c15bd63e) &bull; bump to 0.4.1  
[view](https://github.com/sarumont/py-trello/commit/ce85d3334f5172c5706e0c6bd568e1fd9e15854c) &bull; fix unicode bug (tests for python3 are broken)  


**v0.4.2**


[view](https://github.com/sarumont/py-trello/commit/f4ebdc41c03984516ce5bf4d7d73e962ab7a7b05) &bull; card : checklists and comments are sorted; checklists and comments won't raise AttributeError if not already fetched; style nitpicking  
[view](https://github.com/sarumont/py-trello/commit/daf6bbe704162e8684dc455ac904a56211e5e41d) &bull; members : comments are sorted  
[view](https://github.com/sarumont/py-trello/commit/a61fcf9f13f203c9934c9bb84b9f2f8d93deb78e) &bull; trelloclient : add optional import of PyOpenSSL useful for python < 2.7.9 and 3.2 to prevent security issues with openssl (More info : https://urllib3.readthedocs.org/en/latest/security.html#insecureplatformwarning)  
[view](https://github.com/sarumont/py-trello/commit/40653c0fe8dfeebd987e1a4e61bbd68b1b4c3032) &bull; tests : more tests and broken into multiple files  
[view](https://github.com/sarumont/py-trello/commit/880e7aeb6e337659e5459f3618f2961185ef57d2) &bull; Proposition of changelog for 0.4.2  


**v0.4.3**


[view](https://github.com/sarumont/py-trello/commit/ec6202b60a85c3b4be4307aa1cea1fb6df547a6b) &bull; Allow cards to unassign members  
[view](https://github.com/sarumont/py-trello/commit/1d0934c15f83be6d5dac8af7eadac011b94d417e) &bull; Use the proper ref in the lambda (fixes #108)  


**v0.5.0**


[view](https://github.com/sarumont/py-trello/commit/98a20a1eab377842113bf934dc71b3eb35246629) &bull; Add remove_label function to card  
[view](https://github.com/sarumont/py-trello/commit/f81227c05396ce5a9e9ffef3f2c6527d15a41ccd) &bull; Members: Add "fetch_cards" and "fetch_notifications" methods.  
[view](https://github.com/sarumont/py-trello/commit/8a6aa7a60f4cd6aca9208e43ab576e44f4f7d145) &bull; A few things I added for a project of mine: 1. all_boards can now filter, for example open (https://developers.trello.com/advanced-reference/member#get-1-members-idmember-or-username-boards) 2. Cards and boards parse dateLastActivity without needing another fetch (as it is returned in the original json).  
[view](https://github.com/sarumont/py-trello/commit/f4c160d48856119a1302d13043150edf9bd448ae) &bull; None out the date_last_activity as I "promoted" it to the json parsing, so it'll be weird if it just didn't exist if parse failed.  
[view](https://github.com/sarumont/py-trello/commit/06765127704cd795744bc0aeb9616e3cf02e0634) &bull; How the hell did I manage to add tabs? :)  
[view](https://github.com/sarumont/py-trello/commit/11945eaf9380654ffe7ae545fc239445e0745836) &bull; fix #66 - strings are encoded with UTF-8 to be compatible with python 2 and decoded with utf-8 to be compatible with python 3  
[view](https://github.com/sarumont/py-trello/commit/7e51b10b7e3e15f0fec0e62e090e86de6078151c) &bull; Revert "fix #66 - strings are encoded with UTF-8 to be compatible with python 2 and decoded with utf-8 to be compatible with python 3"  
[view](https://github.com/sarumont/py-trello/commit/0ad3eb20338dfad47be481bd2ef21544ddb8da29) &bull; Add card filter parameter to List.list_cards()  
[view](https://github.com/sarumont/py-trello/commit/1d3464de716983516dd396280afd5cfcdcef94e1) &bull; Add cloning from a source card to add_card()  
[view](https://github.com/sarumont/py-trello/commit/2519f2460fc63a6e263cef86c5be8d3034eed219) &bull; Add functionality to retrieve a Label object  
[view](https://github.com/sarumont/py-trello/commit/dc4a2841cf573bf6577485c1917f9dd59bc7c99e) &bull; Add URL shorturl property  
[view](https://github.com/sarumont/py-trello/commit/a1f7dd22a3cd7d5ef44a98526cb8272d9f4852be) &bull; Added card_filter argument to Board.get_cards()  
[view](https://github.com/sarumont/py-trello/commit/0d43bce31037cd26ed65da8301224a03373614ee) &bull; Fixed gh-124.  -Added support for a source_board parameter to add_board  - Added tests for add_board, copy_board, close_board  - Modified list boards to only look at open boards  - This commit now causes the test account to accumulate closed boards  
[view](https://github.com/sarumont/py-trello/commit/51e3a8f7b61ce9377aea024b7214d87213d132d0) &bull; gh-124 Fix for original PR, unit tests had flaw that hid non-working code for copying board.  
[view](https://github.com/sarumont/py-trello/commit/c7e8f089372a156ba667f7bbc76c6b7fc6073fc3) &bull; added test for closed cards, fixed tests for python3(except test_delete_cards)  
[view](https://github.com/sarumont/py-trello/commit/ac2f581dbd7b04ea9efe88296577a2064b04865e) &bull; added action_limit for board. plus the unittests  
[view](https://github.com/sarumont/py-trello/commit/3107195bcda8395210bca51992ba2d2f51868d4d) &bull; action_limit is an optional parameter  
[view](https://github.com/sarumont/py-trello/commit/33404517a08a3090a503a91ae00429ce1860e766) &bull; add due date  
[view](https://github.com/sarumont/py-trello/commit/baef0fa2a716dd38b6d54fdcb4f7162f54a90901) &bull; Add ability to specify which organization to create a board on  
[view](https://github.com/sarumont/py-trello/commit/77eb3f44137632d3fab9d0966a022d4eb02080d9) &bull; implement deletion of single checklist items  
[view](https://github.com/sarumont/py-trello/commit/f2e754171fa59490cc014a4a2986e3b8eb5cb082) &bull; refactoring by removing some duplication  
[view](https://github.com/sarumont/py-trello/commit/1f75070b3688a83baa90c4d8a5eacc33ffc70eb3) &bull; implement clearing of checklists  
[view](https://github.com/sarumont/py-trello/commit/bec258af618649bab021788ec230089da5c7158f) &bull; Updates to support attachments as per Walter's comments https://trello.com/c/5L574YgX/4-add-attachments-to-card  
[view](https://github.com/sarumont/py-trello/commit/2d121d33aa9e51acf20a65070606c17309378959) &bull; Added obtaining all checklists directly from the board and the respective test  


**0.5.1**


[view](https://github.com/sarumont/py-trello/commit/f7c235b65fe93c493d1718faa3fdf7a4ede960d9) &bull; Once a card has reached done list stop time measurement  
[view](https://github.com/sarumont/py-trello/commit/fd0a3d8294645707ac037c20aa1afd575de242ac) &bull; Refactoring to avoid repeated code between Card.listCardMove_date and Card.list_movements  
[view](https://github.com/sarumont/py-trello/commit/dcf59eb18719c24901b8f91285c13630a65a08f3) &bull; Complete statistics about Trello cards  
[view](https://github.com/sarumont/py-trello/commit/f77239181e328ad00a5fa57e2be6c5de03878630) &bull; List position should not be computed based on list.pos, it should be computed by an external function passed as a parameter  
[view](https://github.com/sarumont/py-trello/commit/4cf58437d2e4df65698c19033dabbf587009d796) &bull; Improve the comments in Card.get_stats_by_list  
[view](https://github.com/sarumont/py-trello/commit/b82cbe3a591e02fc8cf65fc3fb6e8efdab174afc) &bull; Adds date filter when extracting card stats. This way we can have a workaround to the limitation of Trello API to get only last 1000 board movements  
[view](https://github.com/sarumont/py-trello/commit/60892d4718c696735970f2e2e41c23558895a1e0) &bull; added card_created_date() function  
[view](https://github.com/sarumont/py-trello/commit/c4db68827bfdfb70a97232762b8689e3ef9a0820) &bull; changed oauth section run command into block quote to match the rest of the file  
[view](https://github.com/sarumont/py-trello/commit/faa71e421c83145e1051914ad67449ce8a35dade) &bull; try this version  
[view](https://github.com/sarumont/py-trello/commit/b0e6aa7088d413a0a0bbd7892400821f1efe61a4) &bull; RST hates me  
[view](https://github.com/sarumont/py-trello/commit/6db587d0c958e68585c56dd8cfa4e1e3c6e98ba6) &bull; RST hates me  
[view](https://github.com/sarumont/py-trello/commit/bad3c778d468a3fde8c8fc208f947514bba67db3) &bull; it would help if I wasn't previewing on the master branch  
[view](https://github.com/sarumont/py-trello/commit/751c6b77d6d0b52d0de39324522ab5022cc6b926) &bull; Added remove_attachment shortcut  
[view](https://github.com/sarumont/py-trello/commit/9fd36c064282cc8bbc6ae18267c33ed23a7cc2ea) &bull; Implement delete comments method on card  

**0.6.0**


[view](https://github.com/sarumont/py-trello/commit/1644e815c053c8d5476d1c58e850484c1fb1ae0e) &bull; Encoding: use unicode everywhere  
[view](https://github.com/sarumont/py-trello/commit/c566142399deda4b7de9441b13cc574510fc8e09) &bull; tests: add tox support  
[view](https://github.com/sarumont/py-trello/commit/a4c2fa0947ce66bd145bbf61a9f832cfc5529be1) &bull; tests: replace use of deprecated assertEquals with assertEqual  
[view](https://github.com/sarumont/py-trello/commit/0023119401dd2e04dd7d214cde583eca96a422de) &bull; README: formatting fixes  

**0.6.1**


[view](https://github.com/sarumont/py-trello/commit/5980421f35e0de3016ac488ed593def3a2e20b13) &bull; README: fix hybrid markdow/rst syntax  
[view](https://github.com/sarumont/py-trello/commit/f3622e5c66b34f41194f622d0a8c3d0f0902aedd) &bull; add gitignore .tox/\nupdate all of comment about :rtype: to remove warning  
[view](https://github.com/sarumont/py-trello/commit/a263c488d6e8b96324741bccbbaa0de79433a9f1) &bull; fix inverted logic in python2 check  
[view](https://github.com/sarumont/py-trello/commit/8f09276984ba335e7f0780b7e38bbb946038205b) &bull; Python 2 is less than Python 3  
[view](https://github.com/sarumont/py-trello/commit/7269cca82a0577410b4dc0b5f04fab4a65b98987) &bull; Don't call it a checklist item id if it's actually an index  
[view](https://github.com/sarumont/py-trello/commit/8caa67f24067e1106f27653afdba6897304c7119) &bull; Fix the docstring to match the call signature  
[view](https://github.com/sarumont/py-trello/commit/1ef99f3307a23fba07b99a03a381fc761e186178) &bull; Note that 'eager' fetches attachments also  
[view](https://github.com/sarumont/py-trello/commit/8ac5d4a709736d410c0d7a6b52d52e0d71a5132f) &bull; Don't be coy about returning an empty list if there are no attachments  
[view](https://github.com/sarumont/py-trello/commit/8de0ac103ca7536f6c427aa259649cb129e1bc07) &bull; Some whitespace tweaks and a comment fix  
[view](https://github.com/sarumont/py-trello/commit/571fb2ccf9e89ace9f4a49aa50f327f762d6099d) &bull; 'create_date' is evidently a typo  


**0.7.0**


[view](https://github.com/sarumont/py-trello/commit/108f7aefe063b095e9fdae238f6ca0cbd06f05e5) &bull; Don't use actions to compute creation_date, use id of the card that contains the creation_date  
[view](https://github.com/sarumont/py-trello/commit/a3006a5c7fe697bff8975e197c1c2fb413ebc344) &bull; Don't use actions to compute creation_date, use id of the card that contains the creation_date  
[view](https://github.com/sarumont/py-trello/commit/d824836fc3fa373f04eb5ab5b53f14f93882815a) &bull; Card and timezone configuration  
[view](https://github.com/sarumont/py-trello/commit/d27708f599c355b7768436c54271df2d5f8314f1) &bull; Don't pass tz to Card.get_stats_by_list because it is already defined in Configuration  
[view](https://github.com/sarumont/py-trello/commit/ae2032069d7f3b74bdf50915c74aed9e7073e831) &bull; dateLastActivity was not initialized in Board when fetching data  
[view](https://github.com/sarumont/py-trello/commit/78bd270d0c0b0d2f0cd30d9d8c30a0fde57319d7) &bull; Check if actions are already fetched in _list_movements  
[view](https://github.com/sarumont/py-trello/commit/1af1dc178d29473bbd65a7d9317b6fbbaf8b854e) &bull; Ignoring MacOS .DS_Store files  
[view](https://github.com/sarumont/py-trello/commit/85c37841f852d92efc0a013aff1a9bc4ede7a5e0) &bull; Deleting Configuration class that has been replaced by Organization. Organization was created by upstream  
[view](https://github.com/sarumont/py-trello/commit/08d3a6fb6f95fe57937b5570e4c142dffe03a5c6) &bull; Fix bad import of Organization class. It is trello.organization not trello  
[view](https://github.com/sarumont/py-trello/commit/83ffae9cfa2ec3dfb805739a1e0e8e67345d3686) &bull; Fix circular import in organization.Organization  
[view](https://github.com/sarumont/py-trello/commit/6b85694f377c9fbe6f2ae0f081e20500a8362f7a) &bull; Board.fetch_actions allows pagination with since parameter  
[view](https://github.com/sarumont/py-trello/commit/4494bce1b7e5946ee6162ee8505fea32f71fc7b0) &bull; Card needs more attributes to be created from Board.all_cards  
[view](https://github.com/sarumont/py-trello/commit/e0d7417ae68a60c07bc3c6f6df5e54bc8f93206e) &bull; Initialize on fetch_checklists() (Closes #145)  
[view](https://github.com/sarumont/py-trello/commit/af8668c2e667b46a57a45dc2c87001d8107f4dff) &bull; Fix  "datetime.fromtimestamp(unix_time)" => "datetime.datetime.fromtimestamp(unix_time)"  
[view](https://github.com/sarumont/py-trello/commit/4c5d3bd0f5105ba02f293be1950714d164a5dbf7) &bull; Fix "AttributeError: 'Card' object has no attribute 'idBoard'"  
[view](https://github.com/sarumont/py-trello/commit/f642144f753fe76896402359106c7f08492464ef) &bull; Fix "AttributeError: 'Card' object has no attribute 'idShort'"  
[view](https://github.com/sarumont/py-trello/commit/3c8014b53a2fa5e62956c830a904948b08bb37ea) &bull; Add list position attribute (pos) to list. This attribute is fetched by default when calling Board.get_lists  
[view](https://github.com/sarumont/py-trello/commit/f6fe04fbaa0813875d8f2bac959b61d66e5f6268) &bull; Add support for creating public boards  
[view](https://github.com/sarumont/py-trello/commit/f95e0bc4b2f053a9330bde366170d5458518a773) &bull; Fix ":token_key:" => ":token:"  
[view](https://github.com/sarumont/py-trello/commit/dab2ac85572653d7654b67fee22fb09e4ab23f88) &bull; Add Board.list_lists  
[view](https://github.com/sarumont/py-trello/commit/2ec62cd6aed8feccfa8ede2e5c3a170ca8815d1a) &bull; Saves a new Trello board  
[view](https://github.com/sarumont/py-trello/commit/b6f9afa12f4ee9fc89b704bd38bd4215155f425b) &bull; Saves a new Trello board. Avoid creating default lists.  
[view](https://github.com/sarumont/py-trello/commit/ca67ffcdc598bdcb9161a36b8297616080eba1d3) &bull; Add 'pos' parameter to Board.add_list to allow creation of lists with an initial position  
[view](https://github.com/sarumont/py-trello/commit/f16a28bbb5be79f2fe23570c59a9c4b9d09fe5c7) &bull; Return the new comment data when creating a comment  
[view](https://github.com/sarumont/py-trello/commit/4a5eefa85dcaf0333849b826e806abd0defedd8d) &bull; Adding before parameter to Board.fetch_actions to enable pagination  
[view](https://github.com/sarumont/py-trello/commit/a01613080081848cd7265eec5527c6ade0ac5c23) &bull; Adding before parameter to Board.fetch_actions to enable pagination  
[view](https://github.com/sarumont/py-trello/commit/4efab4546c7deab9b37a667fe77afd33298db6bc) &bull; add change_pos functionality  
[view](https://github.com/sarumont/py-trello/commit/814c2a486357dbb1525f75dda74348bb63ee727b) &bull; Add limit param to card comments (now is limited to 50 by default)  
[view](https://github.com/sarumont/py-trello/commit/fe3f01577b73f26bd349926a17986031b623d98d) &bull; Add `Attachments`  
[view](https://github.com/sarumont/py-trello/commit/4a8bb0341e65afbdcce4e0289e56247edfdf0c4f) &bull; Add `Attachments Preview`  
[view](https://github.com/sarumont/py-trello/commit/8c666329bb0736d79ce23611460b038bf708766c) &bull; Refactoring params  
[view](https://github.com/sarumont/py-trello/commit/d13c08da46fbe200cd0359c7770b8377940789e7) &bull; Return python-object "Attachments"  
[view](https://github.com/sarumont/py-trello/commit/e2c0611d286d6494edb85b503c78b6320f345540) &bull; Add new method `Board.set_name`  
[view](https://github.com/sarumont/py-trello/commit/1d02b9e4dc4a16df47e9f09c4c41c23ef71ac736) &bull; Add new method `Board.set_description()`  
[view](https://github.com/sarumont/py-trello/commit/7e13e5143944f73042ca5f023ad9d889748c3c9e) &bull; Edit `Attachments.date` return python datetime object  


**0.8.0**


[view](https://github.com/sarumont/py-trello/commit/ef0a8762f01e07b34e4899f38a9054c55fa8b218) &bull; Add pytz in install_requires  
[view](https://github.com/sarumont/py-trello/commit/1d30a8799ed31a6684eb7c7fb9d4622fd1f0c1f6) &bull; Add update_comment for card.  
[view](https://github.com/sarumont/py-trello/commit/5600b154b5260f679e9db1fe35e1d6d487bee1cc) &bull; Card.get_stats_by_list: sort card movements to get the time the card spends in each list  


**0.9.0**


[view](https://github.com/sarumont/py-trello/commit/56aaff1e33c1a547251a0a6075398f610d62e362) &bull; Fix #172  
[view](https://github.com/sarumont/py-trello/commit/86ef2f0184bd690d7d0714c2109480e21761064a) &bull; Add missing initials for members of an organization (fixes #176)  
[view](https://github.com/sarumont/py-trello/commit/aac3b3d007ca0a5bbe6e426d9a8f7f3bcbd38cbf) &bull; Organizations do not have a 'closed' attribute  
[view](https://github.com/sarumont/py-trello/commit/a8bad96afc768584006d2f304f22d5bdc99e2fd6) &bull; Implement partial search API  
[view](https://github.com/sarumont/py-trello/commit/3d12518b632188b550631df68c35f5ad243dd780) &bull; Improve documenation of TrelloClient.search return values  
[view](https://github.com/sarumont/py-trello/commit/e023fded840d34c7f592b67a26e8685f4c279a09) &bull; Eliminate unnecessary fetch calls for search results  
[view](https://github.com/sarumont/py-trello/commit/8ef5552104548dd75706f2135e7a80814ee07f53) &bull; Add position attribute to TrelloList's add_card method to allow creating cards in the top, bottom or an specific position of the list  
[view](https://github.com/sarumont/py-trello/commit/f2524319894f22c523f5c316b04eb7527b948d1d) &bull; Position must be optional in List.add_card. Adding new method move(position) that allows moving a List in a board  
[view](https://github.com/sarumont/py-trello/commit/d1b6d46f139521f052248eef5f8e10b6f9094a9f) &bull; New operations: add and remove member of a board  
[view](https://github.com/sarumont/py-trello/commit/75c319370b63920cc0d00639aa887a6061e332a9) &bull; New feature: move all list from a card to another list  
[view](https://github.com/sarumont/py-trello/commit/aa8d01aa19e30cef5dcd5325c343980c49fd88c5) &bull; Add remove due datetime from a card  
[view](https://github.com/sarumont/py-trello/commit/562e8c35337825e0f4fd3a042e04d82839d05a12) &bull; Add the member type when calling board's get_members  


**0.10.0**


[view](https://github.com/sarumont/py-trello/commit/06f643b339290a2c619127a879e07273baa0fc47) &bull; fix checklist item not sorted  
[view](https://github.com/sarumont/py-trello/commit/11ea9ab1fbcfdb3aebaf3256c2532a4a1af0fd8c) &bull; Third authentication: initialize TrelloClient correctly  
[view](https://github.com/sarumont/py-trello/commit/c04847ba7044ba7e42b23aee5df4edf8f4f27cd7) &bull; Add the option to choose the third authentication  
[view](https://github.com/sarumont/py-trello/commit/25c4e9a5fe94d438435554812499121ed8036f7e) &bull; add function create_label in card.py, which could create new label of the card by given name and color  
[view](https://github.com/sarumont/py-trello/commit/6b818c66d62007aeb7df79439d96d58b7a6c6696) &bull; Fixed fetch_actions for individual cards.  
[view](https://github.com/sarumont/py-trello/commit/3d373fe0a5108853674bc2e52164ffeb159555f3) &bull; Use UTC as default  
[view](https://github.com/sarumont/py-trello/commit/e786d9a5dc0558f7af4b7813b8f77873eb641d74) &bull; Fix typo  
[view](https://github.com/sarumont/py-trello/commit/a1b3b80110201d9e95f0e07e07ddc3424a18c867) &bull; Added little documentation for new users of py-trello  
[view](https://github.com/sarumont/py-trello/commit/d9e3a5c4c939b3a26755dc7e48baed0834fee3a0) &bull; Regenerate the docs  
[view](https://github.com/sarumont/py-trello/commit/192adbfda4e00b07cea748088f057fa2db1ce2ff) &bull; Add get_list() to TrelloClient  
[view](https://github.com/sarumont/py-trello/commit/3d4a30f3789267ad4ef42caadc6ad291bfecb6c9) &bull; Handle dateLastActivity being empty  
[view](https://github.com/sarumont/py-trello/commit/e30b4cc920e3ddf083918d0241dc79fa54be932d) &bull; Make card.fetch_actions() and list.fetch_actions() return the result  
[view](https://github.com/sarumont/py-trello/commit/e8bc3c8705943f8f55ff7349270f0f690edfad76) &bull; Add/Remove member to card functions  
[view](https://github.com/sarumont/py-trello/commit/a94a8134c340e755259b1908ddaebc1dcffc76cb) &bull; introduce Board.get_last_activity()  
[view](https://github.com/sarumont/py-trello/commit/ba8787cff23cb87052256c8bfcd436164edcb12a) &bull; Remove out-of-date contributors list  
[view](https://github.com/sarumont/py-trello/commit/6430753813344685fb44c95d861b12ce938f65d2) &bull; add AUTHORS file (closes #206)  
[view](https://github.com/sarumont/py-trello/commit/ac82230fe532c715bebbe50f106d7166886ffde8) &bull; Add assignee to list.add_card  
[view](https://github.com/sarumont/py-trello/commit/5c13756550943a594a23a491100eb42700049b48) &bull; Python 2 constructor style  
[view](https://github.com/sarumont/py-trello/commit/7d8396bbbfcd5aa117a472d897fe515022254bea) &bull; Fix TrelloBase import path in attachments.py  
[view](https://github.com/sarumont/py-trello/commit/ac9e3b9e3de0c5e12046aa485b31565f60e6d954) &bull; Fix Card.get_stats_by_list. In case a movement is from/to a list in other board, it is ignored  
[view](https://github.com/sarumont/py-trello/commit/60af41bcab0a13fad2dda3d4d15e11fc0abb657f) &bull; Concentrated hash and eq inside TrelloBase to avoid repetition  
[view](https://github.com/sarumont/py-trello/commit/46e468c6f1be34a9b2d3507239ebddfad7d7872a) &bull; - Added __hash__ and __eq__ for some more modules  
[view](https://github.com/sarumont/py-trello/commit/41e07ef8612f1237ffee97399ea42730cf6125ea) &bull; Add util to __init__.py  
[view](https://github.com/sarumont/py-trello/commit/736eecc8f76e622c167b23091757ea6b48e876ca) &bull; Refactoring import  
[view](https://github.com/sarumont/py-trello/commit/f8990a2a1cd08832f975f5e02fb9136ec3207431) &bull; Add `Card.set_due_complete` and `Card.remove_due_complete`  
[view](https://github.com/sarumont/py-trello/commit/a5fc4205c7e18c8665aab30d5bd67e9646b50a8c) &bull; Add `Card.is_due_complete`  
[view](https://github.com/sarumont/py-trello/commit/8fc3c8cf91311b168293318110d6a5b220e6bcf1) &bull; Added a link to the documentation  
[view](https://github.com/sarumont/py-trello/commit/7f226616dea82965d59d8e5933d3bd3da20ea7e4) &bull; Delete `Card.create_date` is deprecated  
[view](https://github.com/sarumont/py-trello/commit/5f6e6c81c9207f6e666f933b1ae952d9983bc27e) &bull; close #187  
[view](https://github.com/sarumont/py-trello/commit/3040ab1ef996a4623dc901a62934353a37a232b7) &bull; add new properrty - plugin_data to cover https://developers.trello.com/advanced-reference/card#get-1-cards-card-id-or-shortlink-pluginData  
[view](https://github.com/sarumont/py-trello/commit/f172a49e06ae81db78bf6899057d2fe56d75dcd8) &bull; enhance trellolist list_cards  
[view](https://github.com/sarumont/py-trello/commit/ce2b29115d2c4373f5648ae76f8cc0dc97df9cf6) &bull; Add attachements to the card if present in the response JSON  
[view](https://github.com/sarumont/py-trello/commit/89331cf2e9132c367c414feb05607c3c295bbdfa) &bull; Add a way to know what id assigns Trello to a new attachment  
[view](https://github.com/sarumont/py-trello/commit/a3efa16c8e89f4dc3dc211db2e1be02f641a70e3) &bull; Set name of the list  
[view](https://github.com/sarumont/py-trello/commit/e4dc488374d8236caa03dcdd90355c4e5bbb28d7) &bull; card comment docstring param  
[view](https://github.com/sarumont/py-trello/commit/ec81b804b2c55085c9ecb25ec5049958ff1e65a0) &bull; card set_name docstring  
[view](https://github.com/sarumont/py-trello/commit/767b825cce01deba10ab2e068990d8ed9cab703b) &bull; card a bit of pep8 fixes  
[view](https://github.com/sarumont/py-trello/commit/249f4fc7f31575ceaf4d0b2feea7bdf9536392fc) &bull; card from_json docstring return type  
[view](https://github.com/sarumont/py-trello/commit/8382fe7dc789f8f610b2d1e4e313cbcdb858a777) &bull; card from_json method - parameter is named `parent`, but in docstring it was `trello_list`  
[view](https://github.com/sarumont/py-trello/commit/086455fb77ea5e719d76e3901f248a77eb1e9677) &bull; card init - parameter is named `parent`, but in docstring it was `trello_list`  
[view](https://github.com/sarumont/py-trello/commit/30c60b3378146106141de1fe8c4398ade8dbb53d) &bull; board get_members docstring  
[view](https://github.com/sarumont/py-trello/commit/eef0d3f8e9925fcf23be08a4d4638276710c570f) &bull; boards fetch_actions pep8 fix  
[view](https://github.com/sarumont/py-trello/commit/451bf8bea9bdfb488fc0c32476d44af0dd7f543e) &bull; add board fetch_actions docstring  
[view](https://github.com/sarumont/py-trello/commit/72a889d5138c9d56cf49fa639f14806b9f8e9049) &bull; prep for 0.9.0 (fixes #184)  
[view](https://github.com/sarumont/py-trello/commit/92637e1e5a5f490ef80012e64c7319ee38f65924) &bull; prep for 0.9.0  


**0.11.0**

[view](https://github.com/sarumont/py-trello/commit/f6021e79f2cb986cd2150bf23829d99ae6ecf361) &bull; Add basic support for custom fields  
[view](https://github.com/sarumont/py-trello/commit/2ba36c399635eec07fd0284a0b49a153146254dd) &bull; Add set_organization method to Board object to work with organizations  
[view](https://github.com/sarumont/py-trello/commit/1e3b313c0d964988438e616217ceddb68f72f986) &bull; commit check  
[view](https://github.com/sarumont/py-trello/commit/47834a2a0b5efa0e4b3ef23f6e311d5ae009fca5) &bull; Fix lazy loading in Card  
[view](https://github.com/sarumont/py-trello/commit/551e923d41b1952f3a88e51573c07cc21c6490ea) &bull; Inject request  
[view](https://github.com/sarumont/py-trello/commit/df1b2903464456f732710187c1c1634e269cd547) &bull; Add get_boards method to Member object with organization support  
[view](https://github.com/sarumont/py-trello/commit/2e1d93945f35301cfb2639cebe1d231ac3417cb2) &bull; Update trellolist.py  
[view](https://github.com/sarumont/py-trello/commit/1a6b0e54689585e198dd6aa864dc8c70e9b44fd3) &bull; Added support to get subscription status for lists as well as subscribe/unsubscribe from lists  
[view](https://github.com/sarumont/py-trello/commit/1699057ccddbc9f7261912beec05fd945453b72d) &bull; List, add, and delete stars.  
[view](https://github.com/sarumont/py-trello/commit/006e7ab0b66c13f8f104de165fa3b96b7c01105b) &bull; add remove_member and add_member methods to Organization object  
[view](https://github.com/sarumont/py-trello/commit/f9ceb4ee6e6000c67427d1f5b837571c36728bbf) &bull; untested star implementation  
[view](https://github.com/sarumont/py-trello/commit/64a1de3863f6ecd3b0bada26b0f69c21bbb70cac) &bull; Adds method to delete label from board  


**0.11.1**


[view](https://github.com/sarumont/py-trello/commit/b2c25e6e94842ab761d2ac0918a9acb061e4bf1c) &bull; Delete star string format hotfix for python 2.7 compatability  


**0.11.2**


[view](https://github.com/sarumont/py-trello/commit/6f0ea3ec9d3e10c83dac5f40505ebea32bc32191) &bull; Fixes Issue #247 KeyError: 'customFieldItems'  


**0.11.3**


[view](https://github.com/sarumont/py-trello/commit/6135d523ec2e76fdf202577cac4776c8cdc901ab) &bull; Modifies Cards.from_json to not require customFieldItems  


**0.12.0**


[view](https://github.com/sarumont/py-trello/commit/aae3317efe5a146088246cd1db6cc81b8a91fcae) &bull; Add check and fix for python3 unicode assertion  
[view](https://github.com/sarumont/py-trello/commit/4335327b6c32b6fab26c5ccd4332617367404060) &bull; Add warning that running tests will delete cards  
[view](https://github.com/sarumont/py-trello/commit/2ae76752c56bfd252f57a33e088e5fe5d3baa024) &bull; trelloclient: allow to customize cards_limit  
[view](https://github.com/sarumont/py-trello/commit/e6361cf691ebaf1ffbdcd5bf759714c5736a0ca6) &bull; more card API consistency  
[view](https://github.com/sarumont/py-trello/commit/9887c1bc2e9a23ba4a4a4a63c9d448573a2d9530) &bull; fixed customFields on cards  
[view](https://github.com/sarumont/py-trello/commit/758d133032bdb9b3d703058fb448dca2fd8592a5) &bull; added default_lists as parameter to add_board  
[view](https://github.com/sarumont/py-trello/commit/11d2d0881da14f8ef36ae217f2d80c777d01738f) &bull; Add lazy loading for card.customFields  
[view](https://github.com/sarumont/py-trello/commit/9cc1d5d8cafb3ccb7aae5e418d76e8bc8ab80756) &bull; Add function for accessing new/existing custom fields of a card by name  


**0.13.0**


[view](https://github.com/sarumont/py-trello/commit/b025d0f2e02da6c4e299642776ad9b9615df190a) &bull; Add ability to pass custom query parameters to get_cards  
[view](https://github.com/sarumont/py-trello/commit/8e2737e6998fc523476e036484fdc0ee7e4c830f) &bull; fix #256 can't set attribute errror  


**0.14.0**


[view](https://github.com/sarumont/py-trello/commit/a1b637bd15bacdcd7f82eda92b06efd02f470234) &bull; Fix timezone problem with tz aware datetime  
[view](https://github.com/sarumont/py-trello/commit/0313157aaa72482b2f0e64d0e93f22dc5fc63432) &bull; null/empty check for actions (closes #266)  
[view](https://github.com/sarumont/py-trello/commit/b88cabca401af72e5ad6573ec98f77462d6f1aff) &bull; provide access to the raw card json  


**0.15.0**


[view](https://github.com/sarumont/py-trello/commit/f0303805d292e5ed6cb803fa3c1634338c35dbf7) &bull; Add set_custom_field to card.py  
[view](https://github.com/sarumont/py-trello/commit/6a57526bfa73a1b46495571fe14e8bc12cb6245e) &bull; Allow proxy usage  
[view](https://github.com/sarumont/py-trello/commit/0ddd4bb79a3486775df6c8b32b5c2a480b7d068e) &bull; Fix card.badges unset for cards created by from_json()  
[view](https://github.com/sarumont/py-trello/commit/6b39e3d1cc2df69f139e8de3085efd66351b89db) &bull; fixed KeyError / missing subscribed key in Trello lists  
[view](https://github.com/sarumont/py-trello/commit/266bce5bcf4ff2c1864a029450186a9c8f6c94ea) &bull; Add documentation blurb about TRELLO_TEST_STAR_COUNT to README.rst  
[view](https://github.com/sarumont/py-trello/commit/630f5f7154b8282f23d967ec1f3cf0fa6c92b358) &bull; Lazy load property trello.Board.date_last_activity, using property _date_last_activity  
[view](https://github.com/sarumont/py-trello/commit/dd990f36381f4455d9107a68ab7b2379de21a852) &bull; fix typo  
[view](https://github.com/sarumont/py-trello/commit/b14b770d8a22aec49818c4e07277f77ee1254b82) &bull; add keep_from_source to add_card in trelloList  
[view](https://github.com/sarumont/py-trello/commit/0ffe8f22fba43e2d63a34a53b81948726deebd52) &bull; add list_cards_iter  
[view](https://github.com/sarumont/py-trello/commit/aa31d1e63ce7567ddea8372ae5dc9bbafd43a15a) &bull; Clean list_movement docstrings  


**0.16.0**


[view](https://github.com/sarumont/py-trello/commit/e6574fd28f4f6f1feb09948689e37052afb6f526) &bull; Add missing header and footer  
[view](https://github.com/sarumont/py-trello/commit/c591a97c87d3e8c52622c53433a6437d08f64693) &bull; Add __main__.py for creating OAuth token  
[view](https://github.com/sarumont/py-trello/commit/c94290425085c3cd2d6a26be28afec2c5d7c35b3) &bull; Fetch comments from copied cards  
[view](https://github.com/sarumont/py-trello/commit/5a73dc4df93d977ab00854ecd622fe393764b388) &bull; Adding custom field items when getting single card  
[view](https://github.com/sarumont/py-trello/commit/96cf17a91829ecef91ae772166338c2eb0707d91) &bull; add method for get all visible cards  


**0.17.0**


[view](https://github.com/sarumont/py-trello/commit/a153594cfbc18ae3a8ee01503cbf3358126f6f00) &bull; Allow set_custom_field to accept an empty value  
[view](https://github.com/sarumont/py-trello/commit/dce5d46c4e32bf811c5ec2e39029c2f614598703) &bull; add functions to add and delete custom field definitions from board  
[view](https://github.com/sarumont/py-trello/commit/0b857eb0d36c2b026b6502501a4d461b9c7baff0) &bull; setup.py: Add GitHub URL  
[view](https://github.com/sarumont/py-trello/commit/2d7cbc86430cd38e158783613158df879952e5b7) &bull; Update card.py  
[view](https://github.com/sarumont/py-trello/commit/f38734d622ba01680da0f2bdc541198be16f6639) &bull; Update card.py  
[view](https://github.com/sarumont/py-trello/commit/8f047ae62bc14ba44c058536292583d9f7b8dde3) &bull; Update card.py  
[view](https://github.com/sarumont/py-trello/commit/005438e0e3e11dab379ef9f0fa3a7aed540125f8) &bull; Make consecutive calls work with default query arg  


**0.17.1**


[view](https://github.com/sarumont/py-trello/commit/bd23d383be371f11d0aa45125ea256a99094d4d6) &bull; Removes the unused try statement that broke the last version  


**0.18.0**


[view](https://github.com/sarumont/py-trello/commit/d2338d27c3fc7ff8822c0305a9b873be5eb2b33a) &bull; fix last_activity typo  
[view](https://github.com/sarumont/py-trello/commit/fd01575bce6df6d1a64fd0ebbd3b8fc65695fd94) &bull; Add add_organization()  
[view](https://github.com/sarumont/py-trello/commit/df889cb813018c80a6e2f928d3f8d79d10efb248) &bull; Custom field list updates  
[view](https://github.com/sarumont/py-trello/commit/9b094dd3b9bbe6df6ca25587bb612148885a9223) &bull; Fixing TabError  
[view](https://github.com/sarumont/py-trello/commit/520666f22d921162e48b4dd059c056155a1dce12) &bull; Added powerups  
[view](https://github.com/sarumont/py-trello/commit/ec178fd13ba04fe3f5b407e57c491a832a883eef) &bull; Add files via upload  
[view](https://github.com/sarumont/py-trello/commit/10f5f8f1baa686acc8d8a5957ce0b615d233a8b3) &bull; Update custom field definition  
[view](https://github.com/sarumont/py-trello/commit/624c50c68b94c9f3443c4bec1048dc6d07437576) &bull; Updating set_reminder  
[view](https://github.com/sarumont/py-trello/commit/61579fe11556897a6885663df68cc32bc4f06a60) &bull; Two new methods  
[view](https://github.com/sarumont/py-trello/commit/e198d6abf47fd6f08325f1c399f1806a4ddc439e) &bull; Added two methods for checkitems  
[view](https://github.com/sarumont/py-trello/commit/39c4c2d6c80b39cd946e85f06da3b7d6ddd576c4) &bull; Add OAuth2 support to webhook list  
[view](https://github.com/sarumont/py-trello/commit/777b5daf7266af0df055b21799d00012074d4084) &bull; Add OAuth2 support to webhook creation  
[view](https://github.com/sarumont/py-trello/commit/8892b1ab86e57aea5d3ce83f93fa7cc88ccbb2d0) &bull; Return empty cards  
[view](https://github.com/sarumont/py-trello/commit/fa9d7f8a5b418f9f8edde21416841a6332c96c67) &bull; fixed a problem with fetching checklists  
[view](https://github.com/sarumont/py-trello/commit/1b54a74a4ce7f9c0ebc31382fc75602123055395) &bull; Update card.py  
[view](https://github.com/sarumont/py-trello/commit/7d9374d1fa93129e7f019814b29d8ade8d764f6f) &bull; Added setCover to the attach function  
[view](https://github.com/sarumont/py-trello/commit/c4e8a8bcc38218c37ca4525cb09464583ca60d19) &bull; Update trelloclient.py  
[view](https://github.com/sarumont/py-trello/commit/5ef931db0e7db7cf526c6ad7b302858d6df9ca42) &bull; Update trelloclient.py  
[view](https://github.com/sarumont/py-trello/commit/a5004daa635dc495597f28df817a2d22978af776) &bull; Implement the Move List to Board API  
[view](https://github.com/sarumont/py-trello/commit/e4290bd665cf99168a377fd23c4e9130ca06bd7d) &bull; update2 __repr__ to display all Board class attributes  
[view](https://github.com/sarumont/py-trello/commit/7cd745c66ef5b4c20f2a30af0c0f08d3e5c3d06f) &bull; update __repr__ to display all Board class attributes  
[view](https://github.com/sarumont/py-trello/commit/0b7ebdb718bf76fc94215964951b24597790bea8) &bull; fetch Member email  

**0.19.0**

[view](https://github.com/sarumont/py-trello/commit/4e4bcd7a4c84c54257d050ef6228364c44c2aace) &bull; Not all action has attributes related to movements (listBefore, listAfter), in that way it need to be checked.  
[view](https://github.com/sarumont/py-trello/commit/c7df55a9beeab72b68f61a48002b47941f0d1cfe) &bull; Fixing typo reported in #315. Fixing identation when checking last_list (comment was idented correctly, but code not). Fixing the calculation of the time that card has been on a list, correcting last_action_datetime update value by putting it before if/continue statement.  
[view](https://github.com/sarumont/py-trello/commit/1b74e5adb7766076e6bb8e8150442bec1fbe40c5) &bull; fix #325: allow working with duplicate checklist item names  
[view](https://github.com/sarumont/py-trello/commit/719f5e0f236d44e0ad27e6e15772b9a69c7f865e) &bull; Minor improvement: add Board.get_card(card_id)  
[view](https://github.com/sarumont/py-trello/commit/fbbbc727ed5b5e3aaa5ac4370bfe35d78f2dede6) &bull; Minor code improvement, instead of creating a member and updating field on Board class, using static factory Member.from_json. Adding Member.member_type; Adding Member.avatar_url;  
[view](https://github.com/sarumont/py-trello/commit/6190bb1a79ca406c258637ab1f5a9b215248e605) &bull; add 'displayName'  property to 'organization' class  
[view](https://github.com/sarumont/py-trello/commit/8715fc646b26a0c8f729c9e3ce6a1338adda830f) &bull; Adding get_label() into Board class  
[view](https://github.com/sarumont/py-trello/commit/4af7182afa6b5dc53a018eb403ae8bd6002a9b3d) &bull; deprecate enable/disable power up  
[view](https://github.com/sarumont/py-trello/commit/a66b525e7fdc8d4122bb9aba5b00fa9341e54818) &bull; fix: incorrect string format index  
[view](https://github.com/sarumont/py-trello/commit/bef7c034409622fd79652e87e5a3527be442f1e9) &bull; adapt card checklists handling to new Trello payload  
[view](https://github.com/sarumont/py-trello/commit/9817e97502d1822e2e58b5db562e05b60965cf93) &bull; Don't check completed checklist items if None  
[view](https://github.com/sarumont/py-trello/commit/f4ac3fbe609779a37c3253549be26dc141b8e49f) &bull; adding urlSource field for adding cards, which works brilliantly  
[view](https://github.com/sarumont/py-trello/commit/e7d50ea1aed0b3dd646af835b4438ae58a1b5342) &bull; Added Option To Delete Board  
[view](https://github.com/sarumont/py-trello/commit/c711809a076aee3fc04784e26e6b0b9688229ebd) &bull; chore: cleanup  


**v0.20.0**

[view](https://github.com/sarumont/py-trello/commit/89115fdd35ee16d50d8a909f3d619bfa1fd58a5f) &bull; Add HTTP User-Agent to fetchJSON (#375)  
[view](https://github.com/sarumont/py-trello/commit/4ff6f9667dce8514817f84d3ac8e99371fa980fb) &bull; Fix regression with trello api get requests. (#374)  
