# Word Puzzle

Word puzzle is a Python terminal game that runs in a mock terminal(set up by Code Institute) on Heroku.

User can generate a 15 x 15 letter matrix that contains english words. Some ~25 words are purposely planted in the matrix.
User gets to enter the words that they can find in the matrix, to the command line and is awarded points for each word that they find. Players can play for as long as they want an terminate the game at will.
When player chooses to go for "game over", a list of the remaining unfound words are displayed to the user.

[See this live link for the finalized project.](https://wordpuzzle.herokuapp.com/)

![Responsice Mockup](#)

## How to play

When game is iniated, the computer generates and displays a 15x15 letter matrix.
The user should try to find as many words as one can within the matrix.
Words are written verticly downwards, and horizontaly from left to right.
The user inserts the words they find into the command line and recieves feedback about ones current results.
When user can not find any more words, they abort the game and get to see all the words that were left to find.


## Features 

### Existing Features

- __Game Instructions__

  - Before game starts, user is given a walkthrough of the game flow and how to play.
  - When user presses Enter key. Game starts.

![Instructions](#)

- __Puzzle Generator__

  - A 15x15 letter matrix is generated for each started game. This is automatically and pseudo-randomly generated and so the user can always generate a new unique game and word puzzle with some ~25 hidden words in it.
  - At the end of the game, a list of the inserted words are displayed minus the ones that the user found themselves.

![The Word Puzzle](#)

- __Game State Feedback__

  - The game tracks all the users inputs and gives a respones for each of the users input to highlight:
    - Was a point scored?
    - How many words are left to find?
    - How many points does the user have in total?

![Game State Feedback](#)

- __Game Over__

  - As the user exits the game, the user is provided with a list of the words they did not find. 
  - The user is provided the option to play again, with a new puzzle.

![Game Over](#)


### Features Left to Implement

- __Language Choice__

  - Providing the user with the option to create a puzzle and play the game in a different language than English.
    - Perhaps google translate libs can be utilized and/or finding other dictionary sets.


## Testing 

- All game scenarios were tested manualy in local terminal before deployment
- The deployed heroku version was tested by myself and by friends

#### Bugs found and addressed
- The button with id="paper-button" in the players choice area caused the whole players area to expand downwards on hover.

#### PEP8 Linter
- [JSHint](https://jshint.com/) Returned 24 warnings about the JavaScript code. These warnings were all one of the following warnings;
  - 'const' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).
  - 'template literal syntax' is only available in ES6 (use 'esversion: 6').
  - 'let' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).
- In the Configure tab of JSHint under "Assume", I clicked "New JavaScript features (ES6)" which got rid of the warnings. I. e. this website assumes that user browsers support ES6.

## Deployment

### The finalized version of the website was deployed on GitHub pages.
#### Step by step:
- Navigate to to the github repository 'Settings' tab
- Select 'Pages' in the left side menu
- Under "Build and deployment" - "Branch"; Select 'Main' in the 'Select branch' drop-down menu.
- Click Save
- A green banner displays with a live link when deployment and build is finished.

This is the live link for the deployed page - https://jensbrauer.github.io/rockpaperscissors/


## Credits 
A python set of english words
[English Dictionary](https://pypi.org/project/english-words/)


### Content 

- The icons used for buttons and display areas were taken from [Font Awesome](https://fontawesome.com/)