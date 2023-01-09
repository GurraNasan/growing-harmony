# Growing in harmony

![amiresponsive](documentation/img/Responsiv.jpg)

Live App link : [Grow in harmony](https://growingharmoni.herokuapp.com/)
Git Hub Repository : [Grow in harmony](https://github.com/GurraNasan/growing-harmony/)

Grow in harmony is a app for home farmers and plant lovers, it is build on a blog but is meant to be more
interactiv. On the site the user can read and make there own posts and comment on other users posts. You need
to register a user if you want to post/like or comment on a post. But it is also a page for the owner to sell her
merch and sell in the brand.

# Contents

+ [User Experience(UX)](#user-experience-ux)
  + [Agile Method](#agile-method)
      + [User Stories](#user-stories "User Stories")
      + [Data modal](#data-modal)
      + [Future Features](#future-features)
      
+ [Page Features](#page-features)
   + [nav bar](#nav-bar)
   + [Index](#index-page)
   + [Shop](#shop)
   + [Forum](#forum)
      + [Category](#category)
      + [Category Posts](#category-post)
      + [Post](#post)
      + [Add post](#add-post)  
   + [Contact](#contact)
   + [Register](#register)
   + [Admin](#radmin)
   
+ [Technologies](#Technologies)
   + [Programming Languages](#programming-languages)
   + [Support Programs & libraries](#support-programs-libraries)

+ [Testing](#Testing)
   + [Bug](#bugs)
   + [ManuelTesting](#manuel-testing)
       + [NavigationHeader](#navigation-header)
   + [PageManualTesting](#home-page-maual-testing)
      + [Index page](#testing-index-page)
      + [SignInManualTesting](#sign-in-manual-testing)
      + [Forum](#teseting-forum)  
        + [Category Page](#category-page-testing)
        + [Category Posts](#category-post-testing)
        + [Posts](#post-testing)            
   + [Validation](#validator-testing)
   
+ [Deployment](#deployment)
   + [Github](#github)
   + [Django and Heroku](#django-and-heroku)   
   + [Clone Project](#clone-project)
   
+ [Acknowledgments](#acknowledgments)
    + [Credits](#credits)
    + [CopiedCode&CodeAssistance](#copied-code--code-assistance)
    + [Note](#note)
    
## User Experience UX

I found a good bootstrap template from [Bootstrapmade](https://bootstrapmade.com/) called PhotoFolio. I liked the green colors because
i was making a plant forum and fellt like it was a great fit. It had a nice nav menu that worked good both on computer and on a phone. 

### Agile Method

I used the github projects as a agile tool to manage the planning and implamentation of functions to the site. 
[Project Board](https://github.com/users/GurraNasan/projects/5)

### User Stories

Before i started to write the code a made user stories to for what the user/admin wanted and what they would get from it. 
This are my user stories:
+ [USER STORY: Account registrator](https://github.com/GurraNasan/growing-harmony/issues/1)
+ [USER STORY: Admin](https://github.com/GurraNasan/growing-harmony/issues/8)
+ [USER STORY: Add post](https://github.com/GurraNasan/growing-harmony/issues/3)
+ [USER STORY: Comment on post](https://github.com/GurraNasan/growing-harmony/issues/4)
+ [USER STORY: Like/unlike](https://github.com/GurraNasan/growing-harmony/issues/2)
+ [USER STORY: View post](https://github.com/GurraNasan/growing-harmony/issues/7)
+ [USER STORY: Add category](https://github.com/GurraNasan/growing-harmony/issues/9)
+ [USER STORY: View like](https://github.com/GurraNasan/growing-harmony/issues/5)
+ [USER STORY: View shop](https://github.com/GurraNasan/growing-harmony/issues/6)

### Data Modal
Before a started i made a model diagram so i would know how to build up the databasa modal and
connect them toghter.

![models_diagram](documentation/img/models_diagram.jpg)

### Future Features
When i was coding i came up with a couple of more features to implant.
User can delete and edit comments, i have the knowledgs to do it, but felt i did not have time
A online shop for merch, i dont have the knowledge yet to do it.
A better design for the post when you choosed a category, with more information.

## Page Features

### Nav bar
![Nav_Bar](documentation/img/nav_not_logged_in.jpg)
Here you can see the name of the page and links to all pages, this is for big screens.
There is also social links to Instagram and Facebook

![Nav_Bar](documentation/img/nav_small.jpg)
The nav bar is responsiv and on smaller screens it turns in to a list

### Index page
![index_page](documentation/img/index.jpg)
Here you can read a short presentation about the page owner and what the page is about

### Shop
![shop_page](documentation/img/shop.jpg)
Here you can see on a google linked map were you can by the page owners merch

### Forum
#### Category

![forum](documentation/img/forum.jpg)
Here the user can see the categories the page owner/admin choosed to make and can press on them if they want to read or add a post in that category. 

#### Category post
![category posts](documentation/img/post_in_category.jpg)

Here the user can see all the posts in that category and see how many likes they have got. 
If the user is logged in he/she gets a button to add post in that category. The user can press the
post and see it in whole. I feel that there is alot with the design to fix here but that will be in next circle.
      
#### Post
![read posts](documentation/img/read_post.jpg)
 
Here the user can read the whole post with title, content and image if there are any. If there is the author of the post he/she gets a edit and a delete button so the user can interakt with it. 

![read posts](documentation/img/comment_post.jpg)
 
Here the user can read comments on the post and if they are logged in they can leave there own.

#### Add post
![add posts](documentation/img/add_post.jpg)
 
Here the user get a Field to type title, a field for content and can uploade a image if he/she want. The edit page looks the same. 

### Contact
![Contact](documentation/img/contact.jpg)
 
Here the user get the email adress and real adress to the site owner 

### Register
![register](documentation/img/signup.jpg)

Here a user can sign up to the site so he/she can comment and post in the forum.

![signin](documentation/img/signin.jpg)
If the user already have a account on the page.

![signout](documentation/img/signout.jpg)
If the user want to sign out

### Admin
![admin](documentation/img/admin_page.jpg)
 
Here the site owner got there own page to controll the page. He/she can add/delete/edit categorys, posts and comments. 

## Technologies

### Programming Languages
+ [HTML5](https://en.wikipedia.org/wiki/HTML5)
+ [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
+ [Javascript](https://en.wikipedia.org/wiki/JavaScript)
+ [Python](https://www.python.org/)

### Support Programs & libraries

+ [Git](https://git-scm.com/)
    - Version control.
+ [GitHub](https://github.com/)
    - For storing code and deploying the site.
+ [Gitpod](https://www.gitpod.io/)
    - Used for building and editing my code.
+ [Django](https://www.djangoproject.com/)
    - A python based framework that was used to develop the site.
+ [Bootstrap](https://getbootstrap.com/)
    - For help designing the html templates.
+ [Google Fonts](https://fonts.google.com/)
    - Used to add style the website's font.
+ [Font Awesome](https://fontawesome.com/)
    - Used to obtain the icons used.
+ [Favicon.io](https://favicon.io/emoji-favicons/amphora/)
    - Used to generate the site's favicon.   
+ [Google Developer Tools](https://developers.google.com/web/tools/chrome-devtools)
    - Used to help fix problem areas and identify bugs.
+ [Cloudinary](https://cloudinary.com/)
    - Used to store static files and images.
+ [ElephantSQL](https://www.elephantsql.com/)
    - Storage for the database
+ [W3C Markup Validation Service](https://validator.w3.org/) 
    - Used to validate HTML code.
+ [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/#validate_by_input)
    - Used to validate CSS code.
+ [Pep8ci](https://pep8ci.herokuapp.com/) - Thank you Code Institute
    - Used to validate Python code found on slack #announcements
+ [JSHint](https://jshint.com/)
    - Used to validate JS code.
+ [Summernote](https://summernote.org/)
+ [Heroku](https://www.heroku.com/)
    - To deploy the project.
   
   
## Testing

### Bug
I have run in to a couple of bug while you writing the code and i tried to squash them direct when i run in to them. So i forgot to document them. 

But the biggest one was that my css was gone when first deployed the page, to see if it worked

![no_css](documentation/bug/no_css.jpg)

This was fixed by setting debug to False.




   + [ManuelTesting](#manuel-testing)
       + [NavigationHeader](#navigation-header)
   + [PageManualTesting](#home-page-maual-testing)
      + [Index page](#testing-index-page)
      + [SignInManualTesting](#sign-in-manual-testing)
      + [Forum](#teseting-forum)  
        + [Category Page](#category-page-testing)
        + [Category Posts](#category-post-testing)
        + [Posts](#post-testing)            
   + [Validation](#validator-testing)
[Back to top ⇧](#contents)
