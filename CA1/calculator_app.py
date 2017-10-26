import math

from calculator import Calculator

def menu():
  print
  print
  print "******************************"
  print "ASSIGNMENT 1 - CALCULATOR TOOL"
  print "******************************"
  print
  print
  print "YOU CAN SELECT FROM THE FOLLOWING OPTIONS: - "
  print "ADDITION, SUBTRACTION, MULTIPLICATION, DIVISION,"
  print "EXPONENTIAL, SQUARE, CUBE, TANGENT, SINE AND COSINE"
  print
  print "Select 1 FOR ADDITION"
  print "Select 2 FOR SUBTRACTION"
  print "Select 3 FOR MULTIPLICATION"
  print "Select 4 FOR DIVISION"
  print "Select 5 FOR EXPONENTIAL"
  print "Select 6 FOR SQUARE"
  print "Select 7 FOR CUBE"
  print "Select 8 FOR TANGENT"
  print "Select 9 FOR SINE"
  print "Select 10 FOR COSINE"      
  print "SELECT Q TO QUIT"
  print
  print

  selection = raw_input("Input option choice between 1 and 10: ")


  if selection == '1':
    def main():
      num1 = int(raw_input('Enter your first number: '))
      num2 = int(raw_input('Enter your second number: '))
      selection = Calculator()
      print 'Result = ', selection.add(num1,num2)
    main ()
  
  elif selection == '2':
    def main():
      num1 = int(raw_input('Enter your first number: '))
      num2 = int(raw_input('Enter your second number: '))
      selection = Calculator()
      print 'Result = ', selection.subtract(num1,num2)
    main ()   

  elif selection == '3':
    def main():
      num1 = int(raw_input('Enter your first number: '))
      num2 = int(raw_input('Enter your second number: '))
      selection = Calculator()
      print 'Result = ', selection.multi(num1,num2)
    main ()  

  elif selection == '4':
    def main():
      num1 = int(raw_input('Enter your first number: '))
      num2 = int(raw_input('Enter your second number: '))
      selection = Calculator()
      print 'Result = ', float(selection.div(num1,num2))
    main ()  

  elif selection == '5':
    def main():
      num1 = int(raw_input('Enter your first number: '))
      num2 = int(raw_input('Enter your second number: '))
      selection = Calculator()
      print 'Result = ', selection.expo(num1,num2)
    main ()  
  
  elif selection == '6':
    def main():
      num1 = int(raw_input('Enter a number: '))
      selection = Calculator()
      print 'Result = ', selection.sqr(num1)
    main ()  
  
  elif selection == '7':
    def main():
      num1 = int(raw_input('Enter a number: '))
      selection = Calculator()
      print 'Result = ', selection.cbe(num1)
    main ()  

  elif selection == '8':
    def main():
      num1 = int(raw_input('Enter a number: '))
      selection = Calculator()
      print 'Result = ', selection.tan(num1)
    main ()  
  
  elif selection == '9':
    def main():
      num1 = int(raw_input('Enter a number: '))
      selection = Calculator()
      print 'Result = ', selection.sin(num1)
    main ()  

  elif selection == '10':
    def main():
      num1 = int(raw_input('Enter a number: '))
      selection = Calculator()
      print 'Result = ', selection.cos_calc(num1)
    main ()  
  
  else:
    print("Invalid input")

  again()

def again():
  calc_again = raw_input('Do you want to calculate again? Please type Y for YES or N for NO.')
# Accept 'y' or 'Y' by adding str.upper()
  if calc_again.upper() == 'Y':
    menu()
  elif calc_again.upper() == 'N':
    print('See you later.')
  else:
    again()
    
menu()