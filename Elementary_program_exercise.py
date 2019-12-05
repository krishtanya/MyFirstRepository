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

