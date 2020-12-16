
# COOKBOOK

This webpage give users the abilty to enter new recipes to store in a Database. User can create accounts to login securly.
All the reciepes can be searched using the search page. 

Features Implemented:
----------------------------------------------------------------------------------------------------------------------------
Account creation/register
LogOut and Log in Feauture
View Recipes on the page
Search for resipes
Create new resipes and store to Database
edit existing resipes if the owner of the resipe.
Delete the resipe if also the owner of the resipe. Delte protected

Features left to implement:
-------------------------------------------------------------------------------------------------------------------------------

Liking feature on recipes 
infomation on profile page for the user logged into a session. 
More detailed statics on recipes.
More infomation on Homescreen showing user what can be achieved on the site and Greetings.

Technologies Used:
--------------------------------------------------------------------------------------------------------------------------------
HTML
CSS
Python 
Javascript
Jquery
jinja
heroku 
mongoDB
https://materializecss.com/
https://fontawesome.com/icons?d=gallery


Enviorment Variables:

-------------------------------------------------------------------------------------------------------------------------------------
below are the envoirment variables to run the code. These have been already entered into heroku to host the webpage.

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "*****************************************)
os.environ.setdefault("MONGO_URI", "***************************************")
os.environ.setdefault("MONGO_DBNAME", "**************************************)


Debugging: 

FIXED
-------------------------------------------------------------------------------------------------------------------------------------
Fixed issue where recipe name was not displaying on new recipes - variable was inccorect writing to mongoDB

Fixed issue where font awsome icons not displaying on new recipes - if statement check had to be changed to "on" rather than "yes"

Fixed for loop for yield dropdown list causeing a pymongo error message when accessing the page. 

ISSUE 
----------------------------------------------------------------------------------------------------------------------------------------

Yeilds values not loading from dropdown list correctly and loaded Null into Database.  -- FIXED

Edit recipes page getting a 404 error - looks like object id in mongoDB is not getting injected into URL. -- FIXED

Pymongo Error on seach (pymongo.errors.OperationFailure: "$search" had the wrong type. Expected string, found null 'errmsg': '"$search" had the wrong type.

Error above took up consirable time - I got around it by forcing the varibale "query" to be a String going into the function $search.

BUG: yield value when logging a new recipe seems to only show 1 douzen and 5 douzen. loop seems not to itterate the rest inbetween. 
Could possible be a database issue but looking more towards displating the infomation when going through the loop.S

TESTING 

-----------------------------------------------------------------------------------------------------------------------------------------

Checked all links to pages and work succefully.

Tested navigation and links and all work fine. 

materializecss looks after alot the UX and styling.

Can Create recipes and stored correctly with format on Mongo DB.

The infomation stored on MongoDB can be retrieved a dispalyed onscreen correctly.

Tested editing a recipe as well deleting. (message promt when deleting works.)

Tested all buttons and input fields. All displaying correctly at all resolutions. 

Log in and out feautes are working and Store password securely using feautes of Werkzeug. 

Checking all icons work when selected after inputing new resipe. Found vegatarian font awesome doest appear when selected. - Fixed typo- Vegetarian was set to Vegatarian

Found cuisname name was being set as null rather than selection after creating new resipe. Typo FIXED!. 



DEPLOYMENT:

---------------------------------------------------------------------------------------------------------------------------------------

Debug mode has been set to false in app.py file.

Deployed using Heroku.

Version control handled with GITHUB.

Link: https://milestone-3-cookbook.herokuapp.com/

Code is PEP8 Complaint and followed correct indentation.

Used https://validator.w3.org/ to validate html and css code: Alot of notification all point towards using jinja programming in files. No fatal errors.



RESOURCES/CREDITS:
----------------------------------------------------------------------------------------------------------------------------------------- 

https://stackoverflow.com/questions/12096522/render-template-with-multiple-variables   -- answer to "yield" issue found here in comments
https://stackoverflow.com/questions/10310004/jquery-delete-confirmation-box
https://courses.codeinstitute.net/courses/course-v1:CodeInstitute+DCP101+2017_T3/courseware/196c000dd670458cafc7b2dc9d4a8245/439095c6a5414cb3b014fb361829de93/
CodeInstitute Slack channel
https://validator.w3.org/
