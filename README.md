# BlogDjango
This the simple django app. This blog app main feature are create, delete, edit, display and search blog. 
There is the contact form that allow user to send request or feedback.
The display blog can perform in two way, 
    first when the url does not get any id it would display all the blog, 
    second if they get a specific id in the URL it would display only the found ID if no id is found it would return 404
The edit blog would be found by the title or slug, then allow user to edit the post
The delete and search would be also found by the title and slug. 
    For delete if there are many object with the same title it would delete the first one 
The edit create update would available only the user is login 
