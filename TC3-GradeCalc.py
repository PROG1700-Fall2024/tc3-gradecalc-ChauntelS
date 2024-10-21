# Grade Point Calculator

# Create a console-based program that will take a letter grade, such as B+ or C, and convert it to its 
# corresponding numeric value. It will use two prompts, one for the letter grade and a second for the
# modifier, if any (+ or -), and calculate, then output the proper number grade.

# •	Possible letter grades are A, B, C, D, and F
# •	Possible numeric values are 4, 3, 2, 1, and 0, respective to the letters listed above.
# •	Possible modifiers are a plus (+), a minus (–) or nothing. 
# •	There is no F+ or F–. 
# •	Using the + sign increases the numeric value by 0.3, using the – sign decreases it by 0.3. However, an A+ has 
#       still has a value of only 4.0. 
# •	A valid letter grade can be either uppercase or lowercase.
# •	If an invalid value is entered, display a warning message.


def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    
    grade = 0
    a = 4
    b = 3
    c = 2
    d = 1
    f = 0 
    s = 0.3

    

    mark = input("Please enter your grade: ")
    modifier = input("Please enter your modifier + or - : ")

    
    if mark.lower() == "a" and (modifier == "-"):
        grade = a - s
    elif mark.lower() == "a" and (modifier == "+"):
        grade = a + s
    elif mark.lower() == "a":
        grade = a
        
        
        if mark.lower() == "b" and (modifier == "-"):
            grade = b - s
        elif mark.lower() == "b" and (modifier == "+"):
            grade = b + s
        elif mark.lower() == "b":
            grade = b
        
            
            if mark.lower() == "c" and (modifier == "-"):
                grade = c - s
            elif mark.lower() == "c" and (modifier == "+"):
                grade = c + s
            elif mark.lower() == "c":
                grade = c
            
                
                if mark.lower() == "d"  and (modifier == "-"):
                    grade = d - s
                elif mark.lower() == "d" and (modifier == "+"):
                    grade = d + s
                if mark.lower() == "d":
                    grade = d
                
    
                    if mark.lower() == "f":
                        grade = f
                   

    print("your grade is:", (grade))





    # YOUR CODE ENDS HERE

main()
