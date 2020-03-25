# ------------------------------------------------- #
# Title: Assignment 07
# Description: A simple example of storing data in a binary file
# ChangeLog: (Who, When, What)
# <Ali Hajisomo>,<3.22.2020>,Created Script
# ------------------------------------------------- #
import pickle 
# Data -------------------------------------------- #
strFileName = 'AppData.dat' 
lstCustomer = [] 


# Processing -------------------------------------- #

def save_data_to_file(file_name, list_of_data):
   
    objFile = open(file_name, "ab") 
    pickle.dump(list_of_data, objFile)
    objFile.close()
    
def read_data_from_file(file_name, list_of_data):

    objFile = open(file_name, "rb") 
    list_of_data = pickle.load(objFile)  
    return (list_of_data)
    objFile.close() 


 # Presentation ------------------------------------ #

while(True): 
 print('''\n ***** MENU *****
 Select an option
 1 = Enter Data
 2 = Store list to binary file
 3 = Display data from binary file 
 4 = Exit
 ''')
 choice = input('Select an Option: ') 
 if choice == '1': 
    print("(Insert Id and Name)")
   
    intId = int(input("Enter an Id: "))
    strName = str(input("Enter a Name: "))
    lstCustomer = [intId, strName] 
    
    print(lstCustomer) 

 elif choice == '2':
     
    save_data_to_file(strFileName, lstCustomer)
    print('list saved to file') 

 elif choice == "3":
    print ("Data redeemed from File")
    
    print(read_data_from_file(strFileName, lstCustomer)) 

 elif choice == '4': 
     print("Until next time!") 
     break 
 else:
    print('Please Enter Choice 1,2,3 or 4') 


