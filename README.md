# Your Task
Create a Django application with the following features.

## Back end:

* One model to represent both boasts and roasts
* Boolean to tell whether it's a boast or a roast
* CharField to put the content of the post in
* IntegerField for up votes
* IntegerField for down votes
* DateTimeField for submission time

## Front end: 

* Homepage that displays boasts and roasts, sorted by time submitted (hint --> https://docs.djangoproject.com/en/3.0/ref/models/querysets/#order-by (Links to an external site.)Links to an external site.)
* Buttons to filter the content by either boasts or roasts, sorted by time submitted
* Upvote and downvote buttons for each boast and roast
when clicked, these buttons affect the numbers on the relevant post appropriately
* Ability to sort content based on vote score (hint: you may need to calculate the vote score) 
* Page to submit a boast or a roast
### Hints:

* button hrefs can use template data, just like everything else
* voting is not meant to be secure; this is effectively a proof of concept application
* you do not need to worry about figuring out if someone has already voted on something
 

## Extra credit (7 points):

* Add a post deletion method that works for both boasts and roasts on the detail page. "Wait, how will we delete if it's anonymous?", I hear you ask. When a boast or a roast is created, it should have a random 6 character string associated with it (so that it's hard to guess). Every post now has two URLs... but one is public and one is private. For example, a valid post could have these two URLs:
    * localhost:8000/posts/1
    * localhost:8000/posts/abcdef
* The one that ends in an ID should display a "public" version of the detail page; just the post itself. The one that ends in the "secret key" should be the same content, but with an additional button that allows you to delete the content. (Hint: have the button link to a different view that can delete a post by ID)
* When the object is created, the magic string should be passed back to the front end in a link and given to the user; something like "Keep this link secure; this is your private link for managing this post!"