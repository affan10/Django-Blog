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

After adding these features, I added Django REST APIs support as well as a search bar to the blog. The APIs were added by taking inspiration from Coding With Mitch's and Parwiz Forogh's Django REST Framework tutorial, albeit my implementation was a little different. Through the APIs, the following operations are supported:
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


You can compare the differences between the blog in the tutorial and my repo from the video titled Django Tutorial #1
from time 1:41 onwards. Massive credits to The Net Ninja for making this tutorial:
https://www.youtube.com/playlist?list=PL4cUxeGkcC9ib4HsrXEYpQnTOTZE1x0uc 
