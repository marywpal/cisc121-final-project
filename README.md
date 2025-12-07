# cisc121-final-project

Application Name: Number Guessing Game

<img width="1887" height="547" alt="Screenshot 2025-12-06 134326" src="https://github.com/user-attachments/assets/28851e1e-465a-4e25-b806-5bc5e66967e3" />
<img width="1915" height="565" alt="Screenshot 2025-12-06 134340" src="https://github.com/user-attachments/assets/450143cf-7ca6-4c17-a315-650ddd9335a2" />
<img width="1908" height="583" alt="Screenshot 2025-12-06 134353" src="https://github.com/user-attachments/assets/c00b22d0-5ee0-43f5-87ee-a979921b1994" />
<img width="1903" height="540" alt="Screenshot 2025-12-06 134402" src="https://github.com/user-attachments/assets/5372b26c-98bb-4dd4-9409-506dd700a24a" />
<img width="1912" height="554" alt="Screenshot 2025-12-06 134415" src="https://github.com/user-attachments/assets/947b5ff2-03cb-4865-a946-af56c1393ada" />
<img width="1902" height="563" alt="Screenshot 2025-12-06 134428" src="https://github.com/user-attachments/assets/91859a5c-fc4e-4736-b9e1-05401a2e7a3a" />
<img width="1908" height="506" alt="Screenshot 2025-12-06 134436" src="https://github.com/user-attachments/assets/2ac7c115-b912-4f7a-b514-81e5d80c164f" />

____________________________________________________________________________________________________________________________________________________________________________________________________________________


Chosen algorithm: Binary Searching
For my program, I am making a small interactive game that consists of the user choosing a number between 1-100 in their heads, and then making the program figure out what number it is by the user either telling it that the number it chose is higher or lower than the number it had given them. For this program, I chose binary searching as it makes the most sense of the two searching algorithms to use, considering it is a program that involves eliminating series of numbers before or after the given midpoints. 

____________________________________________________________________________________________________________________________________________________________________________________________________________________


Decomposition: 
In terms of planning out my breakdown for how this program is to be built, I will first need to set a limit of the numbers that can be chosen from 1 to 100. I then want my program to choose a random number 1-100 each time it is used, so that the process can end up taking different amounts of steps each time depending on the starting number and the user’s chosen number. My next step is to prompt the user to either tell the program whether their chosen number was higher, lower, or equal to their chosen number. From then, the searching algorithm will start up, using that first randomly chosen number as one of the endpoints to be used to find the midpoint. This will continue, on, asking the user after every midpoint whether their number is higher, lower, or equal to it, until the list is refined to the point of getting their number. After the number is found, the program will have kept track of the number of guesses it needed to find the user’s number, then telling the user. The game will end once the number has been found, prompting the user to play again if they would like to.

Pattern Recognition: 
In terms of pattern recognition for the binary searching algorithm being used in this game, the list of numbers gets cut in half from the midpoint for every single time that the user tells the program that their number is higher or lower than the current given number. The game keeps this going until the number that is guessed is correct. These are patterns that are seen when using a binary searching algorithm.


Abstraction: 
This program, despite being built to guess a number of which the user is thinking of, does not actually care what exactly the number the user is thinking of is. The only think that the program really cares about in terms of the number itself, is whether the user claims that the number they have chosen is higher or lower than what the program had guessed. The abstraction allows the program to only have to focus on the portions which have to be inserted into variables -- like high, low, guess, guess_count, and first_guess -- as well as the general rules of the game. An example of the rules portion is how the program gives a certain response if there is no possible way, given the responses from the user, that their number was consistent throughout the entire game. When this happens, the program is prompted to tell them that they should do so, making it so that the game does not continue on or break.


Algorithm Design:
The algorithm for this number guessing game starts by confirming and setting the lower and upper limits (low = 1, high = 100) and setting the guess count to one. For the first guess, the program will select a random number within the range and prompts the user. After receiving the user's response, which is either higher, lower, or correct, the program will update the upper and lower limits accordingly. For example, if the user tells the system that the number is higher, the lower limit is increased to one above the current guess. Similarily if it is lower, the upper limit is decreased to one below the current guess. If the user responds 'correct', then the game will end, and the total number of guesses is displayed as the final message. For every guess afer the primary randomply generated one, the computer uses binary search by getting the midpoint of the current range as the next guess, increasing the guess count by one with each midpoint chosen. The program is also able to check for inconsistencies, such as when the lower limit ends up being greater than the upper limit, indicating that the user’s responses are inconsistent, and can not be narrowed down to a single number anymore. This process repeats -- updating the limits and calculating new midpoints until the user states that the correct number is found.

____________________________________________________________________________________________________________________________________________________________________________________________________________________

Steps to Run:

1. Press the 'Start Game' button once you have thought of a number.
2. Depending on whether your chosen number is higher or lower than the given guess, select an option from the multiple choice menu accordingly.
3. Once you have selected the accurate response, click the 'Submit Response' button for the next guess to appear, refer back to step 2 to continue.
4. Once the computer has successfully figured out your secret number, choose the 'correct' option from the multiple choice menu.
5. The game will end, telling you the amount of guesses it took.
6. Press the 'Start Game' button again if you wish to continue playing another round. 


____________________________________________________________________________________________________________________________________________________________________________________________________________________

Hugging Face: https://huggingface.co/spaces/marywp/searching_project

____________________________________________________________________________________________________________________________________________________________________________________________________________________

Mary Palumbo
