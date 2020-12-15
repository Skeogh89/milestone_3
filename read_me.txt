




Debugging: 

FIXED
-------------------------------------------------------------------------------------------------------------------------------------
Fixed issue where recipe name was not displaying on new recipes - variable was inccorect writing to mongoDB

Fixed issue where font awsome icons not displaying on new recipes - if statement check had to be changed to "on" rather than "yes"

Fixed for loop for yield dropdown list causeing a pymongo error message when accessing the page. 

ISSUE 
----------------------------------------------------------------------------------------------------------------------------------------

Yeilds values not loading from dropdown list. 

Edit recipes page getting a 404 error - looks like object id in mongoDB is not getting injected into URL. 

Resources: 

https://stackoverflow.com/questions/12096522/render-template-with-multiple-variables   -- answer to "yield" issue found here in comments
