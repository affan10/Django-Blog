# Blog in Django REST 3.11.0, Django 3.0.5 and Python 3.6.9

This blog was developed as a practice for understanding Python's Django Web Framework. The blog was built and 
designed via The Net Ninja's Django Blog tutorial. After completing his tutorial, I added more functionality 
to it and improved the blog's overall User Experience.


Additional functionality includes:
- Serving BootStrap files
- BootStrap footer
- Images showing in thumbnails on blog's main page
- Showing newest blogs added on top
- Ability to update a blog
- Ability to delete a blog
- Only the user whose the author of the blog can update or delete it
- Improved styling

After adding these features, I added Django REST APIs support as well as a search bar to the blog. The APIs were added by taking inspiration from Coding With Mitch's and Parwiz Forogh's Django REST Framework tutorials, albeit my implementation was a little different. Through the APIs, the following operations are supported:
- Signup a new user
- Login an existing user
- Token Authentication
- Adding a new article
- Updating an article; only the author of the blog can perform this action
- Deleting an article; only the author of the blog can perform this action
- Viewing all or an individual article
- Pagination for better experience on mobile devices
- Searching for blogs through GET query parameters through the API
- Search bar to the navbar

To access APIs:

!! For signing-up, send POST request to the following endpoint after running server with the following paramters and their
values of your choice. NOTE that the params username, password, confirm_password should be written as is:

Endpoint: <localhost:port>/api/accounts/signup/
Params:
- username                  # Your value of username must not contain spaces
- password
- confirm_password

If the passwords's will not match or you'll miss a required field, appropriate Response with Status Codes will be returned. You will receive your authentication token in reply to this POST request. Copy & paste it to use it for upcoming operations.

!! For logging-in, send POST request to the following endpoint with your registered username and password as well as the authentication token received from the previous step:

Endpoint: <localhost:port>/api/accounts/login/
Params:
- username
- password
- Authorization # Authorization token

This step will log you in and will return your authentication token in Response.

!! For viewing all articles, send a GET request to the following endpoint with the following parameters. You'll receive an array of articles as JSON objects in Response:

Endpoint: <localhost:port>/api/articles/
Params:
- username
- password
- Authorization # Authorization token as its value

!! For viewing a single article, send a GET request to the following endpoint with the parameters below. You'll receive a array of articles with a single JSON object in Response:

Endpoint <localhost:port>/api/articles/<id of an article>/
Params:
- username
- password
- Authorization # Authorization token as its value

You can compare the differences between the blog in the tutorial and my repo from the video titled Django Tutorial #1
from time 1:41 onwards. Massive credits to The Net Ninja for making this tutorial:
https://www.youtube.com/playlist?list=PL4cUxeGkcC9ib4HsrXEYpQnTOTZE1x0uc 
