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


def perct_marks():
    '''
    (2)  If the marks obtained by the student in 5 different subjects are input through the keyboard.
    Write a Python -  Program to find out the aggregate marks and percentage marks obtained by the student.
    Assume that, maximum marks that can be obtained by student in each subject is 100.
   '''
    try:
#        def f(x):
#            if x <= 100:
#                return x
            #lamdba function
        marks = list(map(int, input("Enter marks for student subjects(separated by comma):").split(",")))
        total = sum(list(x for x in marks if x < 100))
        cnt = len(marks)
        print("Total Marks:", total)
        print("No.of Subjects", cnt)
        pcent_marks = total/cnt
        print("Percentage of Marks: ", pcent_marks)
        if list(x for x in marks if x > 100):
            print("Note: Marks > 100 are ignored")
    except ValueError:
        print("Input was not a digit - please try again.")

#perct_marks()