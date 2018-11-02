def login():				
	default_user_name="admin"
	default_password="123"

	print()
	print()
	print("            *************************************************************************************         ")
	print()
	print("                                     HOSTEL ALLOTMENT SYSTEM")
	print()
	while 1:	
		print("                         enter user name:",end=" ")
		user_name=input()	
		print()
		print("                         enter password:",end=" ")
		password=input()

		if password!=default_password or user_name!=default_user_name:
			print()
			print("incorrect user name or password")
			print()
		if password==default_password and user_name==default_user_name:
			break

	print()
	print("successfull logged in...")
	print()

def regnumber():
	print('                      registration number:',end="")
	reg_number=input()
	print()
def fathername():
	print('                      Father\'s Name:',end="")
	father_Name=input()
	print()
def name():
	print('                      Name:',end="")
	name=input()
	print()
def mobilenumber():
	print('                      Mobile Number:',end="")	
	mobile_number=input()
	print()
def fathernumber():
	print('                      Father\' Mobile Number:',end="")	
	father_mobile_number=input()
	print()
def email():
	print('                      Email:',end="")
	email=input()
	print()
def state():
	print('                      State:',end="")
	state=input()
	print()	
def hostelblock():
	print("                    ",end="")
	hostel_number=input()
	print()
def roomnumber():
	print("                    ",end="")
	room_number=input()

def add_student():
	print()
	print()
	print()
	print('               *********************HOSTEL ALLOTMENT FORM****************************           ')
	print()
	print()
	name()
	regnumber()
	mobilenumber()
	email()
	fathername()
	fathernumber()
	state()
	print('                    choose your Hostel block and Room number from the following: ')
	print()
	print('                 BH1 : Single Rooms for Boys')
	print()
	print('                 BH2 : Double Rooms for Boys')
	print()
	print('                 GH1 : Single Rooms for Girls')
	print()
	print('                 GH2 : Double Rooms for Girls')
	print()
	hostelblock()
	roomnumber()

def edit_profile():
	print()
	print()
	print("Enter registration number")
	reg_number=input()







	print('             #########################PLEASE ENTER WHAT YOU WANT TO EDIT##########################')
	print()
	print()
	print('                1.Name')
	print('                2.Father\'s Name')
	print('                3.mobile_number')
	print('                4.email')
	print('                5.Father\'s mobile number')
	print('                6.state')
	var=int(input())
	if var==1:
		name()
	if var==2:
		fathername()
	if var==3:
		mobilenumber()
	if var==4:
		email()
	if var==5:
		fathernumber()
	if var==6:
		state()

def student_detail():
	print()
	print("                ##############################STUDENT DETAIL##############################")
	print()
	print("		enter registration number of the student",end=" ")
	reg_number=input()




def menu():
	flag=0
	while 1:
		print()
		print()
		print("            ***********************************************************************************")
		print()
		print("                                            MENU")
		print()
		print("		1-NEW ADMISSION")
		print("		2-EDIT/UPDATE INFO")
		print("		3-STUDENT DETAIL ")
		print("		4-EXIT")
		print()
		print("		choose required option ",end=" ")

		op=int(input())

		if op!=1 and op!=2 and  op!=3 and op!=4:
			print("	incorrect input")
		else:
			flag=1	
			break
	if flag==1:
		switch(op)
				

def switch(op):
	if op==1:
		add_student(),
	if op==2:	
		edit_profile(),
	if op==3:	
		student_detail(),
	if op==4:	
		exit(0)
		
def main():
	login()
	menu()



if __name__=='__main__':
	main()
