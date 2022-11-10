# Computer Vision RPS

I have created an image project model on Teachable-machine with four different classes: rock, paper, scissors, and nothing.Each class is trained with images of myself showing each option to the camera. The "Nothing" class represents the lack of option in the image. The more images I train with, the more accurate the model will be. I took around 1000 images for each class in different positions of the same action.

I will later use this model named keras_model.h5 and the text file containing the labels named labels.txt. Which, contain the structure and the parameters of a deep learning model. They are not files that can be run, and they do not contain anything readable if you look inside. Later, I will load them into your Python application in the next milestone. In the project I will use these files to compare against my own code for rock paper scissors.

Firstly, to setup my enviroment I first created a github repository called computer-vision-rock-paper-scissors project. I then created a new virtual enviroment named my_env. Before I could use the model I made in Teachable machine, I had to install the libraries that it depends on using pip install <library>. Making sure I installed installed ipykernel, I ran the given code to sest my model was working, I then proceeded to code the rock, paper, scissors game. The code initialy selects randomly an option from the list rock, paper or scissors. Secondly, I created to functions names get_computer_choice and get_user_choice. The first function will randomly pick an option between "Rock", "Paper", and "Scissors" and return the choice. The second function will ask the user for an input and return it.

Using if-elif-else statements, the script now choose a winner based on the classic rules of Rock-Paper-Scissors. For example, if the computer chooses rock and the user chooses scissors, the computer wins. I wrapped this code in a function called get_winner and returned the winner. This function takes two arguments: computer_choice and user_choice. Subsequently, I created a function called play. Inside this function I called all the other three functions I created (get_computer_choice, get_user_choice, and get_winner). When I run the code, it plays the game of Rock-Paper-Scissors, and it prints whether the computer or you won.

* kjfjf
* hihishihhs
* uhvudhue
* fvis

![Alt text](../../../../../../../C:/Users/haris/Documents/Aicore/rockpaperscissors/computer-vision-rock-paper-scissors/Screenshot%202022-11-09%20233707.png)