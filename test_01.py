  #------ {IMPORT LIB } ------------#




print"                  (   "  
print"   (       (     )\ )  "
print"   )\      )\   (()/(  "
print" (((_)   (((_)   /(_)) "
print" )\___   )\___  (_))   "
print"((/ __| ((/ __| |_ _|  "
print" | (__   | (__   | |   "
print"  \___|   \___| |___|"
print""
print"Coded By : 'Mohammed Bany Amer'"
print""
print" { CYBER CRIME INVESTIGATOR }"


def mainMenu():       ## mainMenu
    print 30 * "-" , "MENU" , 30 * "-"
    print "1. Author"
    print "2. Image Meta Data"
    print "3. Vioce Meta Data"
    print "4. About This Programe"
    print "5. Exit"
    print 67 * "-"
  
loop=True      
  
while loop:          ## While loop which will keep going until loop = False
    print_menu()    ## Displays menu
    choice = input("Enter your choice [1-5]: ")
     
    if choice==1:     
        print "Menu 1 has been selected"
        ## You can add your code or functions here
    elif choice==2:
        print "Menu 2 has been selected"
        ## You can add your code or functions here
    elif choice==3:
        print "Menu 3 has been selected"
        ## You can add your code or functions here
    elif choice==4:
        print "Menu 4 has been selected"
        ## You can add your code or functions here
    elif choice==5:
        print "Menu 5 has been selected"
        ## You can add your code or functions here
        loop=False # This will make the while loop to end as not value of loop is set to False
    else:
        # Any integer inputs other than values 1-5 we print an error message
        raw_input("Wrong option selection. Enter any key to try again..")
	

