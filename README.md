# chibitales.org - Milestone Project 3 - Data Centric Development
The third incarnation of chibitales.org, a website for players of Chibi Fighters 2.0, allows players to read, add and change content, using CRUD operations on the connected MongoDB database:
* Viewing and filtering existing content
* Adding new content
* Editing existing content
* Deleting existing content

The third Milestone Project contributes a new navigation element "Items" to the website and removes redundant html from the website by using Flask. Some changes were made to the navigation and its CSS styling as well to match different screen sizes better as well.

## Table of contents

* UX
* Features
* Future Features
* Database Structure
* Database Integration
* Technologies used
* Testing
* Defensive design
* Hard or impossibleto solve
* Deployment
* Deployment Steps
* Credits

## UX

As a potential player, I want to know if the game is well documented and if it is convenient for me to play. This content database provides this information.

As a new player, I want to find certain ingame content to achieve ingame goals. Filtering the Items page by what I am looking for shows me where and how to get it.

As an advanced player, I want to show new content I achieved to the community and support the community by providing this information.


The new database frontend allows players and potential players to create, browse, update and delete content and by doing so, to build community: 

* For users who found something new: Add names, sources and categories to the database and create new items: Click the Add button and a new page opens to add, submit or cancel a new item or category. After submitting the user will be redirected to the source page with an updated view.

* For users who are looking for information: Just scroll through the items overview or, if you are looking for something more specific, filter the overview by three main categories.

* For users who find a mistake in the information: Click the Edit button and a new page opens to update the information, displaying the selected dataset. After submitting or canceling the edit the user will be redirected to the source page with an updated view.

* For users who find a wrong or outdated information: Just click delete and remove this information from the database. After the delete the updated page will load.

To get an impression on the visualization, take a look into the wireframes folder on GitHub.

## Features
* Clicking "Browse Items" in the navigation dropdown "Items" brings you to the new items overview.

  * The left hand section allows the user to set and apply filters to the results by three provided categories "Name", "Source" and "Category" and an Filter button.
  * The right hand section dislays by default all results as an accordion with the main information (name, amount and source) visible straight away.  
  * Each item can be clicked and the accordion will provide additional information.
  * Each item provides a button to edit and a button to delete the item.
  * The section provides a button to add a new item in the top-right.

* Clicking "Name Editor" in the navigation dropdown "Items" brings you to the name-category overview.

  * The left hand section displays a text showing the users their current location on the site.
  * The right hand section dislays all name-categories and provides a button to add a new name.
  * Each name-category provides a button to edit and a button to delete the name-category.

* Clicking "Source Editor" in the navigation dropdown "Items" brings you to the source-category overview.

  * The left hand section displays a text showing the users their current location on the site.
  * The right hand section dislays all source-categories and provides a button to add a new source.
  * Each source-category provides a button to edit and a button to delete the source-category.

* Clicking "Category Editor" in the navigation dropdown "Items" brings you to the category overview.

  * The left hand section displays a text showing the users their current location on the site.
  * The right hand section dislays all categories and provides a button to add a new category.
  * Each category provides a button to edit and a button to delete the category.

* Clicking the "Add" button on any of the pages will open a new page to add either an item or one of the categories name, source and category.

  * The page offers all necessary fields to add a new unit and a button to submit the new unit.
  * After submitting the user will be brought to the source page, which reloads the updated information from MongoDB using a route.

* Clicking the "Edit" button on any of the pages will open a new page to edit the selected item or category.

  * These pages offer all necessary fields to edit the unit.
  * They provide a button to submit the changes and a button to cancel the edit.
  * After submitting from one of the buttons the user will be brought to the source page, which reloads the updated information from MongoDB using a route.

* Clicking the "Delete" button on any of the pages will delete the dataset straight away from the database and reload the page using a route.

  * There is no defensive design integrated for this, because of a) the course requirements and b) the free available options in MongoDB.
  * The original plan was to just label the dataset as deleted using a Boolean and hide them from display.

## Possible future features in regards to Data Centric Development

* Defensive design for the delete buttons: Confirmation pop-up and delete as a process as first marked for deletion and then delete via admin confirmation.
* Logic checks preventing users from creating duplicates.
* A user login providing different permissions.

## Database Structure in MongoDB

Administrating a variety of completly different objects requires an mostly open approach. To be able to admistrate such different things as e.g.:
* Mini Games 
* Events
* Cards
* Fragments of items
* Currencies
 
 and opening the option to extend the informtion stored for future changes in the game, lead to the approach of one main collection structure for the items of the game. Items actually should rater be called objects because they do not only represent player's inventory.
 On the other hand, this would confuse the users of the frontend rather than being supportive of a good UX.
 This main table is fed by three catalogue tables providing names, sources and categories to allow convenient and unified data entry.
 These catalogue names are self explanantory except categories, which covers objects like currency, weapon and game.
 Combined with some more individual fields this approach allows to create any type of object found in the game.
 Duplicates are possible, because several sources can provide the same item. A logic check if the exact same item, with all properties identical was considered but not implemeted.
 If this happens, the delete button is just one click away.

For a visual, take a look at the database diagram under wireframes.

This structure could have been achieved with a relational database as well, but the structure of the NoSQL database MongoDB allows more flexibility for future extensions.

Given the fairly limited amount of items so far, which  most likely will not grow exponential, database speed was not a main consideration.

## Database Integration

Frontend - backend communication is implemented using environment variables in an env.py file to protect the database from unwanted access by other people.

## Technologies used

* HTML5
  * to build the site
* CSS3
  * to style the site
* javaScript
  * to build the search function
* jQuery 3.5.1.min
  * to build the search function and reduce coding
* Bootstrap 4.3.1.min
  * to style the site and make it responsive
* FontAwesome
  * to get all those lovely icons
* Popper
  * will be used for tooltips
* Hover 2.3.1.min
  * will be used for tooltips
* Google Fonts
  * to get all those lovely fonts
* Python 3 
  * to communicate between frontend and backend
* Flask Framework
  * to simplify Python entry and remove code redundencies
* MongoDB 
  * to store the data
* Heroku
  * for project deployment

## Testing
All HTML5 code is tested via the W3C Markup Validation Service. All error messages refer to Jinja \
All CSS3 code is tested via the W3C CSS Validation Service.\
The website displays as expected on all devices and browsers used.
All Python3 and Flask code was tested manually.\
* Read operations worked on all devices and browsers in any of many screen scales tested.
* Create operations were executed on four devices and several browsers.
* Update operations were executed on four devices and several browsers.
* Delete operations were executed on four devices and several browsers.

Navigation and responsive design was tested with the latest versions of:
* Google Chrome
* Firefox
* MS Edge
* Brave
* Opera

Navigation and responsive design was tested on:
* Mobile Alacatel A1
* Mobile Motorola G8pro
* Amazon Fire tablet
* MSI GP63 Leopard 8RE
* MacBook Air and 24inch screen

## Defensive design
* With every step taken the website's inner structure was tested extensivly against user breaking it by using it.
* There is no way to break out of the paths layed out on the site with built-in functionality.
* The only weaknesses are:
  * Users can just delete content. Asking for confirmation to delete seemed useless under this requirement.
  * Users can create duplicates. I did not have the time to fully anticipate the necessitys of a feature preventing this.

## Hard or impossible to solve
* A datamodel to display such a wide variety of content.
* Breaking down the complexity of the game's infrastructure into a simple data model.
* The solution is to keep it flexible and not trying to structure it to much. Every thing is made up from a few relevant characteristics which I caught, I think.
* GitPod is throwing warnings because of the @app.routes. They are fully working but I did not find a way to make them disappear. They are confusing and might make some actual mistake slip through.

## Deployment
The domain chibitales.org was purchased on godaddy.com. The domain was forwarded to the Heroku App under GoDaddy's DNS settings before submission. \
The open project repository is available under https://github.com/RaphaelRohner/chibitales.org_milestoneproject3 \
The project is deployed under https://chibitales.herokuapp.com/ \

## Deployment steps
* A GitHub project was created from the CodeInstitute full template.
* The project was created in GitPod to programme it.
* A MongoDB database with four collections for the data needed in the project was created.
* A Heroku app named chibitales was created to deploy the project.
* The connection from GitPod to MongoDB was established using environment variables.
* Each major step programmed in GitPod was pushed to the projects GitHub repository using git status, git add ., git commit -m"message" and git push.
* Five days before submission Heroku was installed to the GitPod repository and the commits went to Heroku, so the live site could be tested.
* The Heroku settings were changed to automatically sync with GitHub under Deploy > Deployment method.
* Further commits were pushed to GitHub using the command git push origin master from GitPod. Thanks Steven from the tutoring support!!
* The domain chibitales.org was forwaded to chibitales.herokuapp.com and tested.
* The app is live

## Credits

### Content
Graphics, content and colors: Chibifighters.com by Gary Runke

### chibitales.org is based on modified:

#### Codeinstitute's Resume Walkthrough project
#### Codeinstitute's Whiskey Drop Walkthrough project
#### Task Manager Walkthrough project
#### Bootstrap

### Acknowledgements
Major Thanks @ Gary for the OK to use Chibi Fighters graphics and for the game itself! Let's make it a success - it's so cool!\
Thanks @terminali for https://stackoverflow.com/a/42794613 and how to remove a box-shadow!\
And big thumbs up to everyone @Slack, w3schools and stackoverflow. Without your answers to other problems, I wouldn't have figured out the solutions to mine!