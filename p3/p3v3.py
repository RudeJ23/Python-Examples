""" This program handles various computations with vectors while being
    menu-driven. The user will select an option from the menu to perform
    the operation and will enter values to use in the computation. The results
    will be displayed.
"""
__author__= "Joe Rude"
__date__= "1/30/2017"

def addVectors(v1,v2):
    """Description: Takes two lists of numbers of the same length and returns
           a new list of the sums of the corresponding elements of each
       Preconditions: both v1 and v2 must be the same length
                   both v1 and v2 must contain ONLY numbers
    """
    #initialize output and index location
    newVector = []
    ind = 0
    for eachEle in v1:
        #append the result of an addition to the output
        newVector.append(v1[ind]+v2[ind])
        ind += 1
    return newVector
        
def scalarMult(s, v):
    """Takes a number (s) and a list (v) and returns the scalar
       multiple of (v) by (s).
       Preconditions: (s)must be a number and (v) must be a list of numbers
    """
    #initialize output
    newVector = []
    for eachEle in v:
        #multiply each element in the list by the scalar and append the output
        eachEle = eachEle * s
        newVector.append(eachEle)
    return newVector

def dotProduct(v1,v2):
    """Takes two lists of numbers of the same length, and returns the sum
    of the products of the corresponding elements of each
       Preconditions: v1 and v2 must be the same length of ONLY numbers
    """
    #initialize output and index
    dotProduct = 0
    index = 0
    for eachEle in v1:
        #multiply each item in v1 by its corresponding item in v2
        #add this result to the running total for output
        eachEle = eachEle*(v2[index])
        index += 1
        dotProduct += eachEle
    return dotProduct

def cross_product(v1,v2):
    """Takes two lists of numbers of length 3 and returns their cross product    
       Precondition: both lists must have 3 numbers
    """
    #compute cross product and return as a list
    cx = v1[1]*v2[2] - v1[2]*v2[1]
    cy = v1[2]*v2[0] - v1[0]*v2[2]
    cz = v1[0]*v2[1] - v1[1]*v2[0]
    answer = [cx,cy,cz]
    return answer

def createMenu(optionList):
    """Creates a menu for the user to pick an option from. The menu will
    be displayed each time a choice is selected
    """
    #initialize empty string
    resStr = "" 
    ct = 0
    #for-loop iterate over optionList (grabbing one string at a time)
    for eachOption in optionList:
        #increment ct
        ct += 1
        #concatenate the ct onto resStr
        resStr = resStr + str(ct)
        #concatenate the ") " onto resStr
        resStr = resStr + ") "
        #concatenate the element(string) onto resStr
        resStr = resStr + eachOption
        #concatenate the newline character onto resStr \n
        resStr = resStr + "\n"
    return resStr

def userChoice(userSelection):
    """Gathers input from the user to use for vectors and computations.
       Depending on the choice, instructions are given for what to enter
       as input information.
       Preconditions: All input will be integers
    """
    #if user chooses to addVectors
    if userSelection == 1:
        print("To add vectors, lists must contain only numbers and be "
              "the same length")
        lengthOfList = input("Enter the length of the lists: ")
        while not lengthOfList.isdigit():
            lengthOfList = input("Invalid number. Enter the length of the lists: ")
        lengthOfList = int(lengthOfList)
        #initialize lists and prepare to let user enter list values
        firstList = []
        secondList = []
        for items in range(lengthOfList):
            userInput = input("Enter a number for first list: ")
            while not userInput.isdigit():
                userInput = input("Invalid number. Enter a number for first list: ")
            userInput = int(userInput)
            firstList.append(userInput)
        for items in range(lengthOfList):
            userInput = input("Enter a number for second list: ")
            while not userInput.isdigit():
                userInput = input("Invalid number. Enter a number for second list: ")
            userInput = int(userInput)
            secondList.append(userInput)
        #return output as a list
        answer = [firstList,secondList]
        return answer
    
    #if user chooses to scalarMult
    elif userSelection == 2:
        scalar = input("Enter a number to be the scalar multiple: ")
        while not scalar.isdigit():
            scalar = input("Invalid number. Enter a number to be the scalar multiple: ")
        scalar = int(scalar)
        #initialize lists and prepare to let user enter list values
        userList = []
        lengthOfList = input("Enter the length of the lists: ")
        while not lengthOfList.isdigit():
            lengthOfList = input("Invalid number. Enter the length of the lists: ")
        lengthOfList = int(lengthOfList)
        
        for items in range(lengthOfList):
            userInput = input("Enter a number to put into the list: ")
            while not userInput.isdigit():
                userInput = input("Invalid number. Enter a number to put into the list: ")
            userInput = int(userInput)
            userList.append(userInput)
        #return output as a list
        answer = [scalar,userList]
        return answer
    
    #if user chooses to dotProduct
    elif userSelection == 3:
        print("To multiply vectors, lists must be the same "
              "length and contain all numbers")
        lengthOfList = input("Enter the length of the lists: ")
        while not lengthOfList.isdigit():
            lengthOfList = input("Invalid number. Enter the length of the lists: ")
        lengthOfList = int(lengthOfList)
        #initialize lists and prepare to let user enter list values
        firstList = []
        secondList = []
        for items in range(lengthOfList):
            userInput = input("Enter a number for first list: ")
            while not userInput.isdigit():
                userInput = input("Invalid number. Enter a number for first list: ")
            userInput = int(userInput)
            firstList.append(userInput)
        for items in range(lengthOfList):
            userInput = input("Enter a number for second list: ")
            while not userInput.isdigit():
                userInput = input("Invalid number. Enter a number for second list: ")
            userInput = int(userInput)
            secondList.append(userInput)
        #return output as a list
        answer = [firstList,secondList]
        return answer

    #if user chooses to cross_product
    elif userSelection == 4:
        print("To compute cross product, both lists of numbers "
              "must have a length of 3")
        #initialize lists and prepare to let user enter list values
        firstList = []
        secondList = []
        for items in range(3):
            userInput = input("Enter a number for first list: ")
            while not userInput.isdigit():
                userInput = input("Invalid number. Enter a number for first list: ")
            userInput = int(userInput)
            firstList.append(userInput)
        for items in range(3):
            userInput = input("Enter a number for second list: ")
            while not userInput.isdigit():
                userInput = input("Invalid number. Enter a number for second list: ")
            userInput = int(userInput)
            secondList.append(userInput)
        #return output as a list
        answer = [firstList,secondList]
        return answer
            
                            
def main():
    #create a menu
    strList = ['Add','Scalar Multiplication','Dot Product',
               'Cross Product','Quit']
    menuStr = createMenu(strList)
    print(menuStr)
    #Ask user for their choice
    choice = input("Please select a menu option: ")
    while not choice.isdigit():
        choice = input("Invalid number. Please select a menu option: ")
    choice = int(choice)
    #depending on choice, select an option and call functions accordingly
    #all choices that compute functions will also call the userChoice function
    while choice != len(strList):
        if choice == 1:
            output = userChoice(1)
            print(output[0],"+",output[1],"=",addVectors(output[0],output[1]))
        elif choice == 2:
            output = userChoice(2)
            print(output[0]," * ",output[1],"=",scalarMult(output[0],output[1]))
        elif choice == 3:
            output = userChoice(3)
            print("The Dot Product of",output[0],"and",output[1],"=",
                  dotProduct(output[0],output[1]))
        elif choice == 4:
            output = userChoice(4)
            print("The Cross Product of",output[0],"and",output[1],"=",
                  cross_product(output[0],output[1]))
        else:
            print("Invalid menu choice")
        print(menuStr)
        #ask user for their choice
        choice = input("Please select a menu option: ")
        while not choice.isdigit():
            choice = input("Invalid number. Please select a menu option: ")
        choice = int(choice)

  
if __name__ == "__main__":
    main()
