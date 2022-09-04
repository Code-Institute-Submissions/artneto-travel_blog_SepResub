
# What a Trip|Blog  Milestone Django Project. 




What a Trip is a contemporary vision of a user who has decided to travel  all over the world and is interested in sharing tips and experiences with some other travellers.

## Objective
My 4th Milestone project is an E-commerce Django project. This project shows the knowledge I acquired during the course. The skills learned in the modules that led to this project, include HTML Fundamentals, CSS Fundamentals, JavaScript, Interactive Frontend Development, Python, Data-Centric Development, User-Centric Development, and Django. Adding Django to my skill set; I developed a blog that allows the user to interact with an efficient website.

Check out App Deployed on Heroku [here](https://blogtravel-django.herokuapp.com/)



## UI/UX
## Project goals

The website's user interface (UX) was designed with simplicity in mind. The app is fully functional on all screen sizes, including 1400px, 1200px, 992px, 768px, and 576px, with comprehensive examination for each functionality.


The goal of this assignment is to create a web interface that allows users to simply store and access and performance the CRUD (Create, Read, Update, and Delete) actions. This project's goal is to allow users to create, store, modify, and remove posts (CRUD). People that are interested in topics such as travel or planning to live abroad are the target audience for this initiative. Users can create new categories, which greatly expands the reach of the blog's conversation topics.


### User Stories:
As a user, I want:
*	Be able to launch the site on my preferred device (mobile, tablet, desktop).
*	Be able to view posts and comments created by other users without creating an account.
*	Be able to read selected blog posts. 
*	Be able to select category according to my interest.
*	Be able to create a user account.
*	Be able create user profile and bio. 
*	Be able to create a new category.
*	Be able to upload my picture and media.
*	Be able to link my social media to my profile.
*	Be able to view other users profile.
	Be able to not need to upload pictures in order to create a post.
*	Be able to edit my profile.
*	Be able to change my password and personal information.
*	Be able to edit and delete my posts.
*	Be able to like and dislike other users posts.
*	Be able to create a comment on others page. 
*	Be able to logout.


 This blog is informative and well-communicated with the user, with excellent UX and accessibility turning into a great blog for navigation.


## Agile Development

Agile can be found under projects tab in the github. 

 ![](static/img/agile.PNG)

## Wireframe

This site was built using ideas from preliminary wireframes created in Figma, and the image files exported from these are shown below. This website allows users to browse using a tablet, desktop, or mobile phone.

 - Tablet
  ![](static/img/tablet.PNG)


  ![](static/img/Browser.PNG)


  ![](static/img/phone.PNG)

## Colour Scheme

To produce distinct brilliant hues, I chose to just utilize a unique and eye-catching key color palette. The color scheme is as follows:

![](static/img/colors.PNG)
### Features

#	Navbar:
The navigation bar is at the top, with a logo that functions as a button and takes the user to the homepage.Navabar provides an option to register for new users, as well as the ability to login for those who already have an account. This blog's accessible social networks are listed on the right side of the navbar.

![](static/img/navbar.PNG)

The navbar will display the functionality to create a post and add a category after the access has been created (if the user still doesn't have an account) and logged in.

![](static/img/navbar2.PNG)

The user will have accessibility to a dropdown menu that contains Account preferences, Profile Page, Edit Profile, and Logout.

![](static/img/navbar3.PNG)

For a good user experience, a dropdown button will keep all menu options open and easily accessible for browsing when the blog is viewed on a smaller device such as a tablet or smartphone.

![](static/img/navbar4.PNG)

## Footer
The footer I selected was a sticky footer, and I kept it simple by presenting copyright details.

![](static/img/footer.PNG)

## Main Page Element

Below the contents of the container there is a photo, the user will find the category section with each new category created, this list will grow and appear below the main image. Each selected 
Category will display cards with the chosen subject blog. 

![](static/img/category.PNG)

![](static/img/newcaty.PNG)

![](static/img/groupcaty.PNG)



* Post Section- by default the large containers will be displayed with the title/author name /snippet of the content from each blog post and the date published. For more than three box sections the button next will be available below the cards for user access to older content.

On each individual post page, the user will have access to the full article. 

![](static/img/posts.PNG)



![](static/img/fullpost.PNG)

* In each article, the post owner's profile bio will appear with their details and social networks.

![](static/img/user01.PNG)

## Features
At the bottom of each article blog the like/dislike option will be available for registered users.

![](static/img/dislike.PNG)



![](static/img/liked.PNG)



The option to edit and delete post will only be available to those who created the post.


Unregistered users can read the comments, but only registered users are allowed to make comments on the posts.

![](static/img/seccoment.PNG)

![](static/img/comment10.PNG)





# Error message

Error message in case user is not logged in and try to add a post. 

![](static/img/errorlogin.PNG)


Error message in case unregistered user try to add comment.

![](static/img/register02.PNG)



![](static/img/dislike.PNG)

# User Profile 

Users can view the bio profile of other users on their social networks if available. If a profile photo is not uploaded when creating the profile, a default image will appear.

Login Page – Login form to input username and Password, however, register now link is also available below the form.

Not allowed to login due to incorrect username/password.

![](static/img/erroraccess.PNG)


# Create a Post 

User logged in will be able to create a post. 

![](static/img/createps.PNG)


A default picture will be available in case user skip this form. 


![](static/img/post3.PNG)

# Edit/Delete Post


User can only edit /delete your own post. 

![](static/img/editpost.PNG)


![](static/img/deletepst.PNG)


# Author Profile

The user can view the author of the post's profile as well as their social networks.

![](static/img/usernet.PNG)


# Create Profile

After the user creates your account, the option to create a profile will be available for user logged in.

![](static/img/createacc.PNG)


![](static/img/creatcc2.PNG)


=======



## Register Page

Register form required personal details in order to create a new account. In case user has already created an account there is a login link below the submit button.

 ![](static/img/registerform.PNG)

## Account setting 

* User can edit personal details such as username, first name, last name and email address. 

  ![](static/img/editcc.PNG)

* Change Password page- User can also change their password. 

![](static/img/passwordchange.PNG)

 ## Features left to Implement
Add comment section for user not registered and be able for they can reply to the other comments. 


## Tools/Technologies
*	GitPod
*	GitPodw hosted my Workspace for this project
*	Git
*	used to push and commit any and all changes to my repository on GitHub
*	Bootstrap
*	Installed as a dependency Provided my buttons, modals, Navbar, footer, table and basic grid structure.
*	Also used django-bootstrap-forms
*	JQuery
*	The project uses JQuery for DOM manipulation (Ex: Modal)
SQLite
*	used as my local database until I engaged Database Url for Postgres
*	Heroku
*	Deployment of my Blog
*	Postgres
*	Database used in Heroku after deployment
Testing
Automated Testing
*	Validation Services
*	W3C Markup Validator was used to validate my HTML code.
*	W3C CSS Validator was used to validate my CSS code.


# Back-End Technologies

  * Python 3.6.7 - Used as the back-end programming language.
  * Django 2.2.16 - Used as my Python web framework.
  * Heroku - Used for "Platform as a Service" (PaaS) for app hosting.
  * PostgreSQL 11.4 - Used as a relational SQL database plugin via Heroku.

# Frameworks, Libraries, & Programs Used
  Many Django libraries were used, including Django. shortcuts, Django. views.generic, Django.URLs, and Django. HTTP, among others.
  CKEditor was used to create the textarea.
  The requirements.txt file contains additional information on all Python packages used on this project.

## Deployment

Deployment instructions assume that you have already set up your repository and basic flask application. The website is deployed on the Heroku cloud platform using the following steps:
1. Create the necessary files for deployment
2. Create a requirements file using pip3 freeze > requirements.txt which will contain the required dependencies.
3. Create Procfile using echo web: python app.py > Procfile.
4. Push both files to GitHub
5. log in to Heroku and create a new app
6. Connect the app to your project
7. Go to the deployment method section and choose the method. If using GitHub, select that option, otherwise use the Heroku CLI method.
8. Following the GitHub method, search for the desired repository and connect to it
9. Enter configuration variables
10. Go to the settings tab and select Reveal Config Vars. Enter the variables defined in the env.py file (IP, PORT and SECRET_KEY).
11. Deploy and preview
12. Go back to the deployment tab and enable automatic deployment.
13. Finally, press deploys branch and preview your website.


=======




## Features left to Implement

* Add comment section for user not registered and be able for they can reply to the other comments.
* Explore by destination option with a 2D map integrated.
* Newsletter for users to sign up. 

## Models
  The Postgres database has been used in conjunction with a variety of collections or data models. The models are linked to each other to some extent, as well as being used to store various calculations and all general information on the page.

  Profile model

  * User: Stores the chosen username added by the user.
  * Bio: Stores the bio added by the user to the profile.
  * Profile_pic: Stores the profile picture uploaded by the user. If none is uploaded by the user,  a default image will be added instead.
  * Instagram_url: Store the URL of the user's Instagram account.
  * Facebook_url: Store the URL of the user's Facebook account.
  * Twitter_url: Store the URL of the user's Twitter account
  * Website_url: Store the URL of the user's Blog website account


  Post model

  * Post_title: Stores the title of the blog post.
  * Author: Stores the name of the user who created a post.
  * Publish_date : Stores when a post was created.
  * Header_img: Storage uploaded picture.
  * Content: Stores the actual content of the blog post.
  * Category: Stores which category the post belongs to.
  * Likes: Stores the likes  and dislike a post received.
  
  Categories model

  * name: It is the category name. Example: Travel.

  Comment model

  * Post: Stores which is the post to which the comment should be added.
  * Name: Stores the name of the user who commented.
  * Body: Stores the user comment.
  * Date_added: Stores when the comment seaction was created.

## Testing 

 # Creating an Account
  I've made my own personal account in addition to the master Admin account. In addition to these two primary accounts, I tested with about ten additional accounts to ensure that authentication and validation worked as expected.


 #  Add  Post | Edit | Delete 
  In addition to my personal posts, I created 11 test posts, primarily to test the pagination option at the bottom of the page. My Admin account and the testing accounts were used.
  Once the post has been created, the responsible user of this post will be able to edit or delete it.
  However, for authentication and security reasons, the logged in user will be unable to delete or edit other users' posts.
  As part of a test, I deleted some posts, and everything worked perfectly.


 #  Profile
  - New user, you will view three options on their account dropdown.

  ![](static/img/createcc.PNG)
 
 -  User with created profile can view your own Bio and can have access to your social media. 

  ![](static/img/profilepage.PNG)

 # Account Settings:
  User can edit your user details such as – Username, First Name, Last Name, email and change your own password. 
  1.	I was able to edit all the information detailed above and  able to login in. 
  
  # Create Profile:
  I was able to create my account and add a profile picture, however, iv profile picture is not added a default picture will be displayed. 
  
  # Logout:
  I was able to logout without creating a profile.
  

  # Create a Category

  I was able to create a new category. 

  ![](static/img/newcatego.PNG)

  ![](static/img/new-caty.PNG)

## Validators

  # HTML

  W3C HTML Validator - Unfortunately, the W3C Validator for HTML does not understand the syntax of Jinja templates, so it generates numerous errors regarding {{ variables }}, {% for %} {% endfor %}, and so on. Apart from the Jinja warnings and errors, all of the remaining code validates flawlessly.

  # CSS

  W3C CSS Validator - I am using :root{} variables in my CSS, which isn't validated by the validator This is causing a large number of parsing errors, which are not errors and work perfectly fine.

  # Javascript

  Javascript was used for pagination and about warning forms. No errors were found on the Javascript code.


  # PEP8 Online

  memebers_signup and world app all the .py files passed the validation.
  



## Tools/Technologies
*	GitPod
*	GitPod hosted my Workspace for this project
*	Git
*	used to push and commit any and all changes to my repository on GitHub
*	Bootstrap
*	Installed as a dependency Provided my buttons, modals, Navbar, footer, table and basic grid structure.
*	Also used django-bootstrap-forms
*	JQuery
*	The project uses JQuery for DOM manipulation (Ex: Modal)
SQLite
*	used as my local database until I engaged Database Url for Postgres
*	Heroku
*	Deployment of my Blog
*	Postgres
*	Database used in Heroku after deployment
Testing
Automated Testing
*	Validation Services
*	W3C Markup Validator was used to validate my HTML code.
*	W3C CSS Validator was used to validate my CSS code.

# Deployment

Deployment instructions assume that you have already set up your repository and basic flask application. The website is deployed on the Heroku cloud platform using the following steps:
1. Create the necessary files for deployment
2. Create a requirements file using pip3 freeze > requirements.txt which will contain the required dependencies.
3. Create Procfile using echo web: python app.py > Procfile.
4. Push both files to GitHub
5. log in to Heroku and create a new app
6. Connect the app to your project
7. Go to the deployment method section and choose the method. If using GitHub, select that option, otherwise use the Heroku CLI method.
8. Following the GitHub method, search for the desired repository and connect to it
9. Enter configuration variables
10. Go to the settings tab and select Reveal Config Vars. Enter the variables defined in the env.py file (IP, PORT and SECRET_KEY).
11. Deploy and preview
12. Go back to the deployment tab and enable automatic deployment.
13. Finally, press deploys branch and preview your website.

# Issues Encountered

- I had some difficulties in finding the correct media query resolutions for my page, but in the end I managed to make the content adapt to each different screen.
Outcome

- I have found a bug:" migrate says a column that does not exist does not exist and recommends renaming it", for solution, I have updated the database schema outside a migration.

- I was able to construct my first website using all of the material supplied during the course and with the aid of my mentor. I am pleased with the outcome.

- Thanks again to the entire support team and a big hug to Christina, Oisin and Sean who have always been patient and showing a great people skills.


# Resubmission Remarks 
After review by the evaluation team, below is a list of what was fixed in this project.

- Missing UX and/or navigation issues
- Template code results in various HTML errors.

Solution with the suggestion of the assets team I made sure to use the URL validator for each page and form on my site, being possible to: fix errors of classes that were open and it was also possible to fix the layout and background that was making some forms disheveled.


- No indication of sub-optimal implementation of user acceptance criteria in user stories.
- No indication or sub-optimal implementation of prioritized user stories within the agile tool.

Solution: I revised the module for Agile and the importance of this tool and as a result the implementation is visible in the Travel Blog dashboard under Projects as "done".

- Does not allow users to initiate actions based on their choice or allows broken functionality.

Solution: Create a comment section there was an error in the python logic and it was fixed, now the user can create a comment.

- Env.py file is present on Github.

Solution: This file was mistaken with that even when DEBUG only in false it was presented.
With the help of the tutors, it was possible to identify the error and the solution was to create a new repo environment for my project and reset all the keys that were in the env.py.
>>>>>>> 4daa1e70a5a3bd5f74cf92c47a58a4de539ad2a5
