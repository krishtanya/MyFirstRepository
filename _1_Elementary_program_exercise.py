#Math module is required for pi value constant
import math

def gross_sal():
    '''
    1)  John’s  basic salary is  input through the key board.
        His dearness allowance is 40% of his basic salary and
        house rent allowance is 20% of basic salary.
        Write a  Python  program to calculate his Gross salary.

    Formula:  Gross_salary =   basic_salary + Dearness_Allowance + House_rent_allowance
    '''
    basic_sal = int(input("Enter John's basic salary:"))
    dear_allowance = basic_sal * 0.4
    hra = basic_sal * 0.2
    gross = basic_sal + dear_allowance + hra
    print("John's gross salary is: ", int(gross))

#gross_sal()

def perct_marks():
    '''
    (2)  If the marks obtained by the student in 5 different subjects are input through the keyboard.
    Write a Python -  Program to find out the aggregate marks and percentage marks obtained by the student.
    Assume that, maximum marks that can be obtained by student in each subject is 100.
   '''
    try:
        #User input will be captured into a list
        marks = list(map(int, input("Enter marks for student subjects(separated by comma):").split(",")))
        if list(x for x in marks if x > 100):
            print("Note: Marks > 100 are ignored")        
        
        #Initializing variables
        total = 0
        cnt = 0

        #Calculate user inputs only if marks <= 100
        for i in marks:
            if i <= 100:
                total = total + i
                cnt = cnt + 1
                i=i+1
            else:
                break
            
        print("Total Marks:", total)
        print("No.of Subjects", cnt)
        pcent_marks = total/cnt
        print("Percentage of Marks: ", pcent_marks)

    except ValueError:
        print("Input was not a digit - please try again.")

#perct_marks()

def area_perimeter_rect_cir():
    '''
    (3) The length and breadth of a rectangle as well as radius of circle is input through
         the key board. Write a Python  program to calculate the area and perimeter of the rectangle,
          and the area of circle.
    '''

    #Calculate Rectangle area & Perimeter
    height = int(input("Enter rectangle height: "))
    width = int(input("Enter rectangle width: "))
    r_area = height * width
    r_perimeter = (2*height) + (2 * width)
    print("Rectangle area is : ",r_area)
    print("Rectangle perimeter is : ",r_perimeter)

    #Calculate Circle area
    radius = int(input("Enter Circle radius: "))
    pi = math.pi
    c_area = pi * (2 * radius)
    print("Circle area is : ",c_area)

#area_perimeter_rect_cir()

def interchange_num():
    '''
    (4) Two numbers are input through the key board into  2 locations  A  and B. 
    Write a Python  program to interchange the contents of A and B

    Example:
        Input from key board  A = 10 ;   B = 25
        output on the monitor A = 25  ;  B = 10

    HINT:  use third variable temp.

    '''
    
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("numbers before interchange: ", a, "and ", b)

    #interchange logic using a temp variable
    temp = a
    a = b
    b = temp
    
    print("numbers before interchange: ", a, "and ", b)

#interchange_num()

def sum_of_digits():
    '''
    (5) A five digit number is input through the keyboard. 
    Write a Python program to calculate the sum of its digits.

    Example:    input   ===>    12345
    output ===>   15  which is sum of 1+2+3+4+5
 
    '''

    try:
        #Load user input into a list
        val = list(map(int,input("Enter a five digit number: ")))

        if len(val) != 5:
            print("Its not a 5 digit number. Please enter 5 digit number")

        else:
            #Iterate the list and sum the values in a single statement - Python is very flexible :)
            total = sum(list(x for x in val)) 
            print("Sum of all the digits is : ", total)

    except ValueError:
        print("Input was not a digit - please try again.")


#sum_of_digits()

def reverse_str():
    '''
    (6A) A five digit number is input through the keyboard. 
    Write a Python program to reverse the number.

        Example:  input ==>    12345
        output ==>   54321

    '''
    try:
        #Load user input into a list
        #Note - Input is taken in String datatype to make use of reverse function below.
        val = list(map(str,input("Enter a five digit number: ")))

        if len(val) != 5:
            print("Its not a 5 digit number. Please enter 5 digit number")

        else:
            #below method reverses list elements
            val.reverse()

            #concatenate list elements
            r_str = ''.join(val)
            print("Reverse of entered number is : ", r_str)

    except ValueError:
        print("Input was not a digit - please try again.")


#reverse_str()

def reverse_int():
    '''
    (6B) A five digit number is input through the keyboard. 
    Write a Python program to reverse the number.

        Example:  input ==>    12345
        output ==>   54321

    '''
    try:
        #Take user input - str format by default
        val = input("Enter a five digit number: ")

        if  int(val) >= 10000 and int(val) <= 99999:
            s = val[::-1]  #How Python is able to provide the list, even though a list is not defined?
            i = int(s)
            print("Reverse of entered number is {} and its datatype is {}".format(i,type(i)))

        else:
            print("Input was not a 5 digit number. Please enter 5 digit number")

    except ValueError:
        print("Input was not a digit - please try again.")


#reverse_int()


def sum_of_first_last_digit():
    '''
        (7) A four digit number is input through the keyboard.  
        Write a Python  program to obtain the sum of first and last digits of this number.

        Example:   input ==>  4567
        output ==>  11 ==> which is the sum first digit 7 and last digit 4.

    '''
    try:
        #Take user input into a list in int format
        val = list(map(int,input("Enter a four digit number: ")))

        if len(val) == 4: # Used ==. Throws error for = . Why?
            first_digit = val[0]
            last_digit = val[-1]
            print("Sum of First and Last digit is : ", first_digit+last_digit)
        else:
            print("Input was not a 4 digit number. Please enter 4 digit number")

    except ValueError:
        print("Input was not a digit - please try again.")


#sum_of_first_last_digit()

def monthly_emi_amortization():
    '''
    (8)   Formula to calculate Monthly installment on a Loan.

    Monthly Payment = P (r(1+r)^n)/((1+r)^n-1).
    
    r: Interest rate. This is the monthly interest rate associated with the loan. 
        Your annual interest rate (usually called an APR or annual percentage rate) is listed 
        in the loan documents. To get the monthly interest rate that you need, simply divide 
        the annual interest rate by 12.
        For example, an 8% annual interest rate would be divided by 12 to get a monthly 
        interest rate of 0.67%. This would then be expressed as a decimal for the equation 
        by dividing it by 100 as follows: 0.67/100=0.0067. So 0.0067 will be the monthly 
        interest rate used in these calculations.
    
    n: Number of Payments. This is the total number of payments made over the life of the loan. 
        For example, in a three year loan paid monthly n = 3 x 12 = 36.

    P: Principal. The amount of the loan is called the principal. 
        This is typically the final price after tax of the asset purchased less any down payment
    

    Write a program to calculate equal monthly installments using above formula.
    Input Loan amount, monthly interest rate, and number of years  through the key board.

    (11) Write a program that calculates loan amount and interest for monthly payments,
    for entire loan term. Also calculate Amortization.

    '''

    try:
        princple = input("Enter Loan amount : ")
        p = int(princple)

        interest = input("Enter Yearly Interest % : ")
        r = (float(interest)/(12 * 100))

        timeframe = input("Enter no of years : ")
        n = int(timeframe) * 12

        emi = ((p*r*pow(1+r,n))/(pow(1+r,n)-1))

        print ("Monthly EMI for {} loan amount for {} years with interest rate {} is {}".format(p,n/12,r*12*100,int(emi)))
        print ("You will pay {} as interest for the entire loan term.".format(int((emi*n)-p)))

        i = 1 #represent first month

        while i <= n:
            mi = p*r
            p = p-(emi-mi)
            print("Month : {}    Principal : {} Interest : {}".format(i,round(emi-mi,2),round(mi,2)))
            i = i + 1            

    except ValueError:
        print("Loan amount/time must be in numbers and interest can be a decimal value")

#monthly_emi_amortization()

def tax():
    '''
    (9) Write a program that asks the use to enter a dollars-and-cents amount, then displays
    the amount with 5% tax added.

    Input: Enter dollars and cents : 100.00
    Output: Total amount with 5% tax is 105.00

    '''

    try:
        amt = input("Enter dollars and cents (e.g., 100.05) : ")
        amt = float(amt)
        print("Total amount with 5% tax is : ",amt+(amt*0.05))
    
    except ValueError:
        print("Amount is not in dollars and cents format")

#tax()

def denomination():
    '''
     (10)   Write a program that asks the user to enter a US dollar amount and
     then shows how to pay using that amount using the smallest number of $20,$10,$5, and $1 bills.

     Input: Enter a dollar amount : 93
     Output:
        $20 bills : 4
        $10 bills : 1
         $5 bills : 0
         $1 bills : 3

    '''

    try:
        amt = input("Enter a dollar amount : ")
        amt = int(amt)

        #a temp variable to hold values
        div = 0
        reminder = 0

        denomination = (20,10,5,1)  #created a tuple with denominations

        for i in denomination:
            div = amt // i #to get division in integer value
            reminder = amt % i
            amt = reminder   # balance amount is reassigned to amt variable         
            print("\n ${} bills : {}".format(i,div))
    
    except ValueError:
        print("Input must be a number")

#denomination()