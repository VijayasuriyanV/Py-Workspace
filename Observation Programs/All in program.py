#All in program 
print("\n\nH4I , H4VE 4 NICE D4Y\n\n")
print("Choose Any one Program\n")
print(" 1.Area of Circle\n 2.Area of Triangle\n 3.Celsius to Fahrenheit\n 4.GCD\n 5.Greater number among the 3 numbers\n 6.Print Hello World\n 7.Multiplication Table\n 8.To check the number is positive or Not\n 9.Sum of two numbers\n 10.Swap two numbers\n\n")
prog=int(input("Enter the number , of which program you want to use : "))
print("\n\n")
if(prog==1):
    import Area_of_circle 
  
elif(prog==2):
    import Area_of_triangle
   
elif(prog==3):
    import Celsius_to_fahrenheit
   
elif(prog==4):
    import GCD
  
elif(prog==5):
    import Greater_among_3
 
elif(prog==6):
    import Hello_world
   
elif(prog==7):
    import Leap_year
elif(prog==8):
    import Multiplication_table
  
elif(prog==9):
    import Number_positive_or_neg
  
elif(prog==10):
    import Sum_of_two_numbers
    
elif(prog==11):
    import Swap_two_variables
else:
    print("Invalid Option")

print("\nThe End of the Program")        
