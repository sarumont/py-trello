

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
