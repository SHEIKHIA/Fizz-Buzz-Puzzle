
let num = Number("Enter a number: ")
function fizzBuzz(num){
    if (num % 3 === 0 && num % 5 === 0 ){
    console.log("FizzBuzz");
  } else if (num % 3 === 0) {
    console.log("Fizz");
  } 
  else {
    console.log(num);
  }

};

fizzBuzz(num);