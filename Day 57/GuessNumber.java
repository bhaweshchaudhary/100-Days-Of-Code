// import java.util.Random;
// import java.util.Scanner;

// public class GuessNumber {

//     private static void checkInput(int takingInput, int randomNumber){
//         if(takingInput!=randomNumber){
//             Scanner takeMyInput = new Scanner(System.in); // CREATING SCANNER OBJECT
//             System.out.println("Guess a number between 1 and 100"); // ASKING USER TO GUESS
//             takingInput = takeMyInput.nextInt(); // TAKING USER INPUT
//         }

//         if(takingInput==randomNumber){
//             System.out.println("congrats number matched.");
//         }
//     }
//     public static void main(String args[]){
//         Random randomObject = new Random(); // CREATING RANDOM OBJECT
//         int randomNumber = randomObject.nextInt(101); // GENERATING AND STORING RANDOM NUMBER
//         System.out.println("random generated number is "+ randomNumber);
//         Scanner takeMyInput = new Scanner(System.in); // CREATING SCANNER OBJECT
//         System.out.println("Guess a number between 1 and 100"); // ASKING USER TO GUESS
//         int takingInput = takeMyInput.nextInt(); // TAKING USER INPUT

//         boolean notExit = true; // BOOLEAN HELPS IN TERMINATING WHILE LOOP
//         while(notExit){
//             checkInput(takingInput, randomNumber);
//             notExit = false;

//         }

//         System.out.println("You guessed " + takingInput);

//     }
// }



/*
ALGORITHM

1. GENERATE RANDOM NUMBER AND STORE IN A VARIABLE.
2. TAKE USER INPUT AND STORE IN A VARIABLE
3. RUN WHILE LOOP
4. INSIDE, CALL A FUNCTION, IF RANDOM NUMBER != USER INPUT, THEN ASK AGAIN FOR USER INPUT.
5. IF RANDOM NUMBER = USER INPUT, THEN WHILE LOOP TERMINATES.
*/



