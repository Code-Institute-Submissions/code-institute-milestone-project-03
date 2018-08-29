
# Code Institute Milestone Project 3

This is Practical Python Milestone Project called Riddle Me This. It is a project as part of the syllabus on the Full Stack Web Development course.

## Description

The game is a series of 10 text based riddles which are presented to the user one at a time

The player must choose a username at the beginning of the game which will be unique. 

The player is presented with a series of 10 text based riddles. Players enter their answer into a text box form. 

If the player guesses correctly, they are directed to the next riddle and awarded 1 point. 
If a player guesses incorrectly, their incorrect guess is storedand printed below the riddle.

At the end of the game, the players score will be recorded on the leaderboard using their username as a reference.
 
## UX
 
I spoke with three different potential users regardign what they would look for in a riddle app/ game.

User 1 wanted to play the game on the move so a responsive site was required for him.

User 2 wanted a clean, simple user interface that would let her concetrate on the riddle rather than be distracted by pictures or colors on the screen.

User 3 wanted puzzles that would make him think outside the box but would also be fun.

All three users were happy with the final product when presented with it for further testing.

The clean simple interface was important for me to produce to make it easier on the eye and not over cluttered which would distract from the presentation of the riddles.

The app is fully responsive which is important especially with so many people accessing games and websites on various mobile devices.

I have included a number of wireframes which I used in the development of the various screens in the production of this application. They are included in the repository.

## Features

The app features a game which requires a unique username so that results can be recorded on a leaderboard. The Top 10 results are displayed o nthe leaderboard. The app consists of a welcome page, an instruction page,
10 riddles and then a leaderboard page.

Users can restart the game at anytime by clicking the reset button at the bottom of the page. This returns the user to the starting page, so that the user can recommence.
 

### Features Left to Implement
I would of liked to explore some more automated testing on this project.
I would also like to add a contact section so that users can submit new riddles.
I would also like to add more riddles so that the user will be presented with new riddles each time.



### Some of the tech used includes:
-	**HTML**  and **CSS**
    *	To structure and style the web app content, Including creating the POST method form
-	**Python3**
    *	To design the logic of the game
    * For reading from, and writing to, the game’s text files
    * For unit testing the game’s functions. These tests are found in test_game.py
    *	Creating a requirements.txt and Procfile to deploy the app on Heroku 
    *	Sorting the leadboard data
-	**Flask** 
    *	For binding functions to URLs using routing 
    *	To render HTML templates, including the use of a base template. These templates are in the templates directory 
    *	To  enable Python programming within HTML pages
    *	To trigger functions on GET or POST requests
    *	For getting data from, and dumping data to, JSON files
    *	Used for debugging 
-	**JSON**
    *	For storing and editing player data (players.json) and previously asked questions (used_questions.json) throughout the game
    *	Used to store high score data, found in /data/high_scores.json
- **Bootstrap** 
    *	Used primarily for the website’s grid layout and for styling buttons, player cards, and the leaderboard table
- **Heroku** https://riddle-me-this-pon.herokuapp.com/
    *   Final deployment of the app

## Testing

### Manual Testing
Manual tests were carried out primarily for two purposes:
1.	**The flow of the App**:
Manual testing was required to ensure the game flowed as planned. The game was given to 3 separate testers to use and test on different platforms to try and find any issues. This proved successful and helped my development.
2.	**Experimenting with the project**:
The app was given to 3 differtent users to experiment with and raise any issues or problems. I received good feedback on the desing and flow of the app.
3.  **Responsive Testing**
The app was tested on Samsung S8, Apple iPhone 6, Apple iPad Air 2 and also using the Google Chrome inspect feature to tes for repsonsiveness and any errors that occurred. The main issue which was found was the sidevar/ navbar not resizing.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

4. **Browser Testing**
Broswer compatibility. The above features were tested in each of the following browsers:

Google Chrome
Opera
Microsoft Edge
Mozilla Firefox
Safari

Manual Testing
Manual tests were carried out primarily for two purposes:

Testing the flow off the game: The game loop (the render_game() function) is a combination of various functions. All these functions may work correctly, thus passing all the automated tests, but not work together as planned. Therefore, manual testing was required to ensure the game flowed as planned. An example of this was removing dead players from the JSON data before checking if all players have been eliminated.
Experimenting with the project: There were times throughout development where some experimentation was required to understand what functions to design. In these instances, the first step was to experiment by designing a few functions. Then, once it was known what functions should be designed, these functions could be tested to ensure that they worked as planned.

## Automated Testing

I created tests to measure the accuracy of the functions of my app. I tested for usernames, answers, riddles and leadboard.

## Deployment

The app is hosted on Heroku https://riddle-me-this-pon.herokuapp.com/ 

The GitHub Repository is hosted at https://github.com/pierceoneill/code-institute-milestone-project-03


## Credits

## Extra Resources

Stackoverflow.com

Slack

GitHub

## Images & Videos

Riddler Image - Pinterest - Link: https://www.pinterest.ie/pin/501025527274703156/

Background Video - Coverr.co Free Stock Videos - Link: https://coverr.co/videos/White%20Board

## Riddles

The riddles were sourced from the website http://www.riddles.com

### Acknowledgements

## Theme

The Boostrap Theme - Resume theme - was used as a template for the project. This was obtained from the free library at Startbootstrap.com

Link: https://startbootstrap.com/template-overviews/resume/

## Fonts

Google Fonts - Amatic SC - https://fonts.google.com/specimen/Amatic+SC?selection.family=Amatic+SC:400,700

Google Fonts - Source Sans Pro - https://fonts.google.com/specimen/Source+Sans+Pro

Font Awesome - v5.2.0
