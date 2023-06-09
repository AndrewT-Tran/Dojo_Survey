Assignment: Dojo Survey
=======================

Objectives:
-----------

*   Practice creating a server with Flask from scratch
*   Practice adding routes to a Flask app
*   Practice having the client send data to the server with a form
*   Practice redirecting after the POST request.
*   Use Session to display the form data on the result page.

* * *

![image](https://github.com/AndrewT-Tran/Dojo_Survey/assets/112746783/c27c515a-f28a-447f-b465-b39254d7246c)
  

Build a new Flask application that accepts a form submission and presents the submitted data on a results page.

The goal is to help you get familiar with sending POST requests through a form and displaying that information. Consider the below example as a guide.

![](https://assets.codingdojo.com/boomyeah/company_209/chapter_2982/handouts/chapter2982_3795_survey-form.png)

When you build this, please make sure that your program meets the following criteria:

*   http://localhost:5000 - have this display a nice looking HTML form.  The form should be submitted to '/process'
*   Save form data into session.
*   http://localhost:5000/result - have this display a html with the information that was submitted by POST

**Don't forget that any inputs we want to be able to access from the form submission need to have a name!**

It's always a good idea to print request.form to see if the form is delivering all the information you need in your routing method.
 Markup : - [ ] An uncompleted task
          - [x] A completed task
* Create a new Flask application
    
* Have the root route ("/") show a page with the form
    
* Have the "/result" route display the information from the form on a new HTML page
    
*   Put the form data into session
    
*   NINJA BONUS: Use a CSS framework to style your form
    
*   NINJA BONUS: Include a set of radio buttons on your form
    
*   SENSEI BONUS: Include a set of checkboxes on your form
