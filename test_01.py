import json , sys , hashlib , os , time , marshal, getpass





reload (sys)
sys . setdefaultencoding ( 'utf8' )

def banner():
	print '''
	 ,gggg,       ,gggg,       ,a8a, 
   ,88"""Y8b,   ,88"""Y8b,    ,8" "8,
  d8"     `Y8  d8"     `Y8    d8   8b
 d8'   8b  d8 d8'   8b  d8    88   88
,8I    "Y88P',8I    "Y88P'    88   88
I8'          I8'              Y8   8P
d8           d8               `8, ,8'
Y8,          Y8,         8888  "8,8" 
`Yba,,_____, `Yba,,_____,`8b,  ,d8b, 
  `"Y8888888   `"Y8888888  "Y88P" "Y
	'''
banner()

print"{ ------------------------------------------ }".center(45)	
print""
print"{CYBER CRIME INVESTAGTION JORDAN}".center(45)
print""


def show_program():

	print '''

		         ,                             (
*                           )   *
              )     *      (
    )        (                   (
   (          )     (             )
    )    *           )        )  (
   (                (        (      *
    )          H     )        )
              [ ]            (
       (  *   |-|       *     )    (
 *      )     |_|        .          )
       (      | |    .  
 )           /   \     .    ' .        *
(           |_____|  '  .    .  
 )          | ___ |  \~~~/  ' .   (
        *   | \ / |   \_/  \~~~/   )
            | _Y_ |    |    \_/   (
*     MBA   |-----|  __|__   |      *
            `-----`        __|__

 ------------------------------------------------------
    Author     Mohammed Banyamer
    Name       CCI-JO 'CYBER CRIME INVESTAGTION JORDAN'
    CodeName   NASHMI01
    version    TRAIL version
    Date       15/12/2019 09:35:12
    Team       N4SHMI-JO
    Email      BANI8193@gmail.com
    Instagram  @mbani3amer
    Phone      +962781008061 
     
* CONTACT ME IF YOU FIND ERRORS OR TO GIVE ME FEEDBACK 
'''



def maiMenu():
	print("1. Image MetaData ")
	print("2. vioce MetaData ")
	print("3. About ")
	print("4. Exit ")
	selection=int(input("\n N4SHMI>>"))
	if selection ==1:
		image()
	elif selection==2:
		vioce()
	elif selection==3:
		show_program()
maiMenu()	

def image():
	print"Write The Image Path"
	path=str(input("N4SHMI>>"))
	











