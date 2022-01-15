let num = Number(prompt("Enter a number: ")) //create variable to hold input

function fizzBuzz(num){ //function decleration

  for(i = 1;i<num;i++) // for loop iterate  1 to input number

{    if (i % 3 === 0 && i % 5 === 0 ){ // check the condition, if satisfied print.
    console.log("FizzBuzz");
  } else if (i % 3 === 0) { // check the condition, if satisfied print.
    console.log("Fizz");
  } 
  else { // if not then print the number
    console.log(i);
  }}

};

fizzBuzz(num); //function called and value insert from user.