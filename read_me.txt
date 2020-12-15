




Debugging: 

FIXED
-------------------------------------------------------------------------------------------------------------------------------------
Fixed issue where recipe name was not displaying on new recipes - variable was inccorect writing to mongoDB

Fixed issue where font awsome icons not displaying on new recipes - if statement check had to be changed to "on" rather than "yes"

Fixed for loop for yield dropdown list causeing a pymongo error message when accessing the page. 

ISSUE 
----------------------------------------------------------------------------------------------------------------------------------------

Yeilds values not loading from dropdown list correctly and loaded Null into Database. 

Edit recipes page getting a 404 error - looks like object id in mongoDB is not getting injected into URL. 

Pymongo Error on seach (pymongo.errors.OperationFailure: "$search" had the wrong type. Expected string, found null 'errmsg': '"$search" had the wrong type.

TESTING 

-----------------------------------------------------------------------------------------------------------------------------------------

Checking all icons work when selected after inputing new resipe. Found vegatarian font awesome doest appear when selected. - Fixed typo- Vegetarian was set to Vegatarian

Found cuisname name was being set as null rather than selection after creating new resipe. Typo FIXED!. 



RESOURCES:
----------------------------------------------------------------------------------------------------------------------------------------- 

https://stackoverflow.com/questions/12096522/render-template-with-multiple-variables   -- answer to "yield" issue found here in comments
