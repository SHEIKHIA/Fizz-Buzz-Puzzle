#Create a function that takes a number as a parameter. 
num=0 # define a veriable
num= input('give an number') # assing variable to the guest given value
def Fizz_buzz( num ): #function defination of fizz_buzz

  for i in range(1,int(num)): #iterate through 1 to given number
    if i % 3 == 0: # condition to check if it divisible by 3
      print('Fizz') # if it is print Fizz
      continue # then ignore the given number because i am printing i at the bottom 
    elif i % 3 and i % 5 ==0: # if it's divisible by 3 and 5 then print Fizzbuzz
      print('FizzBuzz')
      continue # then ignore the given number 
    print(i) #print those number
Fizz_buzz(num) #calling the function to see the action and assing the value by user.
        
    
# This function will print out (console.log()) every number from 1 to the number passed as the parameter, now:
#- if the number is divisible by 3 then the function will print out the word 'Fizz' instead of the number.
#- if the number is divisible by 3 and 5 then the function will print out the word 'Fizz Buzz' instead of the number.


#Submit the github link to the repo containing the code, your reasoning and pseudo code of the solution for the problem (code comments).