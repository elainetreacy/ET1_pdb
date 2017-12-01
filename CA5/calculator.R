
# CA5 R Calculator - Elaine Treacy 10362944
#
# Part 1 - Using pythong calculator produced in CA1
# Create simliar fucntions in R together with associated tests 

# 1 - Addition
addition <- function(numb1, numb2) {
  return(numb1 + numb2)
}

# 1a - Test for Addition Code

addition(3,2)
addition(5,1)
addition(2,-1)

#2 - Subtraction
subtraction <- function(numb1, numb2) {
  return(numb1 - numb2)
}

#2a - Test for Subtraction Code
subtraction(3,2)
subtraction(5,1)
subtraction(2,-1)

#3 - Multiplication
multiply <- function(numb1, numb2){
  return(numb1 * numb2)
}

#3a - Test for Multiplication Code
multiply(3,2)
multiply(5,1)
multiply(2,-1)

#4 - Division

division <- function(numb1, numb2){
  return(numb1 / numb2)
}

#4a - Test for Division Code
division(3,2)
division(5,1)
division(2,-1)

#5 - Exponential

exponential <- function(numb1, numb2){
  return(numb1 ** numb2)}

#5a - Test for Exponential Code
exponential(3, 2)
exponential(5, 1)
exponential(6, 6)

#6 - Square Root
sqrt_func <- function(numb1){
  return(sqrt(numb1))
}

#6a - Test for Square Root Code
sqrt_func(2)
sqrt_func(1)
sqrt_func(6)

#7 - Cube
cube <- function(numb1){
  return(numb1 ** 3)
}

#7a - Test for Cube Code
cube(2)
cube(1)
cube(6)


#8 - Remainder
remainder <- function(num1, num2){
  return(num1 %% num2)
}


#8a Test for Remainder Code
remainder(2, 5)
remainder(2, 3)
remainder(1, 10)


#9 - Cube Root
cube_root <- function(numb1, numb2){
  return(numb1 ** 1. /3)
}

#9a Test for Cube Root Code
cube_root(2, 6)

#10 - Permutations
perm = function(n, x) {
  factorial(n) / factorial(n-x)
}

#10a Test for Permutations
perm (6, 2)
perm (12, 6)