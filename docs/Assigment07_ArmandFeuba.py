# ------------------------------------------------- #
# Title: Assignment7
# Description: A simple example of storing data in a binary file
# ChangeLog: (Who, When, What)
# <Armand feuba Baweu>,<09.02.2023>,Created Script
# ------------------------------------------------- #
import pickle  # This imports code from another code file!
Demo = input(" which demo you want to see: "+ "choice '1' for Error handle or choice '2' for Pickel")
choice = Demo

if(choice == "1"):
    #   Error Handling
    # Using try
    try:
        quotient = 5/0
        print(quotient)
    except:
        print("There was an error! <<< Custom Message!\n")

elif(choice == "2"):

    #Pickling
    import pickle  # This imports code from another code file!

    intId = int(input("Enter an Id: "))
    strName = str(input("Enter a Name: "))
    lstCustomer = [intId, strName]

    # Now we store the data with the pickle.dump method
    objFile = open("AppData.dat", "ab")
    pickle.dump(lstCustomer, objFile)
    objFile.close()

    # And, we read the data back with the pickle.load method
    objFile = open("AppData.dat", "rb")
    objFileData = pickle.load(objFile) #load() only loads one row of data.
    objFile.close()

    print(objFileData)
else:
    print("sorry your choice is non correct !!!")
