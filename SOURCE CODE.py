# FUNCTIONS
def Acc():
    L=[]
    a=input("Enter your name:")
    b=int(input("Enter phone number:"))
    c=input("Enter password:")
    d=input("Enter E-mail:")
    xp='*'*(len(c))
    L.append(a)
    L.append(b)
    L.append(d)
    L.append(xp)
    return L

def Sel():
    L1=[['Department Charges'],
        [1,'Harappan Gallery-200'],
        [2,'Anthropology Department-150'],
        [3,'Historic Period Gallery-100'],
        [4,'Medival Arts Gallery-50'],
        [5,'Decorative Arts Gallery-75'],
        [6,'Miniature Paintings-75'],
        [7,'Other Faciities'],
        [8,'Exit']]
    T1=tabulate(L1,headers ='firstrow',tablefmt='grid')
    return T1

def Hap():
    L2=[["Scluptures","Period"],
        ["Dancing Girl","2700BC-2100BC"],
        ["Bull","2700BC-2100BC"],
        ["Mother Goddess","2700BC-2100BC"],
        ["Toy Cart","2700BC-2100BC"],
        ["Passupati Setu","2700BC-2100BC"],
        ["Climbing Monkey","2700BC-2100BC"]]
    T2=tabulate(L2,headers ='firstrow',tablefmt='grid')
    return T2

def Ant():
    L3=[['Categories'],
        ['Tribal Lifestye Of North East India Gallery'],
        ['Sharan Rani Balkiwal Instrument Gallery']]
    T3=tabulate(L3,headers='firstrow',tablefmt='grid')
    return T3

def His():
    L4=[['Galleries','Period'],
        ['Maurya,Shunga And Satvahana Arts','1-4 Century BCE'],
        ['Khushana Gallery','1-3 Century BCE'],
        ['Gupta Gallery','4-6 Century BCE']]
    T4=tabulate(L4,headers='firstrow',tablefmt='grid')
    return T4

def Med():
    L5=[['Section','Time Period'],
        ['Early Medieval Aretefacts','7-10 th Century'],
        ['Late Medieval Artefacts','11 th Century']]
    T5=tabulate(L5,headers='firstrow',tablefmt='grid')
    return T5

def Dec():
    L6=[['Artefacts'],
        ['Ivory Card Dashavtra Shine'],
        ['Jahangir Jade Hookah'],
        ['Gyan Chauper'],
        ['Indu Surahi From Mughal Era'],
        ['Wodden Garud Vahana(Tamil Nadu)'],
        ['Wodden Horse(Tanjore)']]
    T6=tabulate(L6,headers='firstrow',tablefmt='gird')
    return T6

def Min():
    L7=[['Types Of Miniature Paintings'],
        ['Mughal Minature Paintings'],
        ['Central India Miniature Paintings'],
        ['Rajasthan Mianiature Paintings'],
        ['Pahari Miniature Paintings']]
    T7=tabulate(L7,headers='firstrow',tablefmt='grid')
    return T7

def Oth():
    L8=[['Departments'],
        [1,'Canteen'],
        [2,'Kids Play Zone'],
        [3,'Exit']]
    T8=tabulate(L8,headers='firstrow',tablefmt='grid')
    return T8


def Can():
    L9=[['Items','Charges'],
        ['Tea',50],
        ['Coffee',150],
        ['Samosa',35],
        ['Sandwiches',120],
        ['Patties',125],
        ['Patries',130]]
    T9=tabulate(L9,headers='firstrow',tablefmt='grid')
    return T9

def Kid():
    L10=[['Games'],
         ['Puzzles'],
         ['Minecraft'],
         ['Rocke'],
         ['Mario'],
         ['Animal Crossing'],
         ['Pokemon Shield'],
         ['Other Video Games']]
    T10=tabulate(L10,headers='firstrow',tablefmt='grid')
    return T10


def Pay():
    e=int(input("Enter Account number:"))
    f=input("Enter name:")
    g=input("IFSC Code:")
    h=input("Enter pin:")
    print("PAYMENT SUCCESSFUL")
    return ('YES')

def Log():
    L11=[['Select any one:'],
         [1,'Update Profile'],
         [2,'Check Status'],
         [3,'Feedback'],
         [4,'Exit']]
    T11=tabulate(L11,headers='firstrow',tablefmt='pretty')
    return T11

def Pre():
    L12=[[1,'Create Account'],
         [2,'Login'],
         [3,'Logout'],
         [4,'Contact Us']]
    T12=tabulate(L12,tablefmt='pretty')
    return T12

def Book():
    L13=[['Select'],
         [1,'Book your tour'],
         [2,'Payments'],
         [3,'Exit']]
    T13=tabulate(L13,headers='firstrow',tablefmt='pretty')
    return T13

def more():
    List2=[[1,'Search'],
           [2,'Count no. of employees'],
           [3,'Average Salary'],
           [4,'Maximum joining employee'],
           [5,'Maximum Salary'],
           [6,'Minimum joining date'],
           [7,'Total salary'],
           [8,'Exit']]
    Table2=tabulate(List2)
    return Table2

def tick(X,Q,N):
    print('*'*30)
    print()
    print('\t'"ARTS AND CULTURE MUSEUM")
    print('\t'"    TICKET")
    print('-'*30)
    print()
    print('\t'"Date:",Q)
    print('\t'"Total no. of persons:",N)
    print('\t'"Total mount paid is:",X)
    print()
    print('*'*30)
    return


#CONNECTING PROGRAM
from tabulate import tabulate
import mysql.connector as sql
mycon=sql.connect(host="localhost",user="root",password="aparna",database="aparnadb1")
if mycon.is_connected==False:
    print("Error connecting to mysql database")
my=mycon.cursor()

#MAIN PROGRAM
print('*'*99)
print('\t\t\t\t'"WELCOME TO OUR AMAZING WORLD OF ECLIPSE")
print('\t\t\t\t'"LET US TAKE YOU TO YOUR IMAGINATION!!!!!!!!!!!")
print('*'*99)
print()
print()
print("Enter 1 to enjoy our services......")
ch=int(input("Enter:"))
if ch==1:
    print("SO,how can we serve you today?????")
    while True:
       print('='*40)
       print('\t'"1.Staff")
       print('\t'"2.Visitor")
       print('\t'"3.Exit")
       print('-'*40)
       st=int(input("Enter your choice(1-3):"))
       box=[]
       if st==1:
              print()
              print()
              print("--------WELCOME!!!!!!!!!!!!!!--------")
              print()
              print("Login to your account")
              IDE=int(input("Enter your login ID:"))
              PASS=input("Enter your password:")
              print("-"*70)
              while True:
                  print("CHOOSE YOUR PREFERENCE....")
                  Table=[[1,'Staff Details'],
                         [2,'Add Staff Member'],
                         [3,'Remove any employee'],
                         [4,'Update details of any employee'],
                         [5,'Customer Details'],
                         [6,'Customer feedback'],
                         [7,'More Details'],
                         [8,'Exit']]
                  List=tabulate(Table)
                  print(List)
                  print()
                  print()
                  dat=int(input("Enter your choice(1,8):"))
                  print()
                  if dat==1:
                      print("-----STAFF DETAILS-----")
                      my.execute("Select*from STAFF")
                      sun=my.fetchall()
                      print(tabulate(sun,headers=('ID','NAME','SEX','DOB',
                                                  'DEPARTEMENT','DOJ','SALARY','CONTACT'),tablefmt='psql'))
                        
                  elif dat==2:
                      print("------Enter details of the new staff member-------")
                      AA=input("Enter Staff ID:")
                      AB=input("Enter Name:")
                      AC=input("Enter Sex(M/F/T):")
                      AE=input("Enter DOB.(YYYY/MM/DD):")
                      AF=input("Enter department:")
                      AG=input("Enter date of joining(YYYY/MM/DD):")
                      AD=int(input("Enter salary:"))
                      AH=int(input("Enter contact number:"))
                      moon="Insert into STAFF Values('{}','{}','{}','{}','{}','{}',{},{})".format(AA,AB,AC,AE,AF,AG,AD,AH)
                      my.execute(moon)
                      mycon.commit()
                  elif dat==3:
                      print("-----Reamove any staff member------")
                      Lake=input("Enter ID:")
                      mt="DELETE From STAFF WHERE ID='{}'".format(Lake)
                      my.execute(mt)
                      mycon.commit()
                  elif dat==4:
                      print("----Update record of an employee----")
                      at=input("Enter ID:")
                      bt=int(input("Enter Salary:"))
                      ct=int(input("Enter contact number:"))
                      dt=input("Enter Department:")
                      Fun="UPDATE STAFF Set Salary={},Contact={},Department='{}' WHERE ID ='{}'".format(bt,ct,dt,at)
                      my.execute(Fun)
                      mycon.commit()
                      print("Records updated successfully")
                  elif dat==5:
                      LIST1=[["NAME","PHONE NUMBER","E-MAIL ID","PASSWORD"]]
                      LISTk=LIST1.extend(box)
                      Table1=tabulate(LIST1,tablefmt='grid')
                      print(Table1)
                  elif dat==6:
                      print("Name of Customer:",a)
                      print("Feedback of",a,"is",v)

                  elif dat==8:
                      break
                    
                  elif dat==7:
                      print("-----------More details----------------")
                      while True:
                          print(more())
                          DJ=int(input("Enter your choice(1,8):"))
                          if DJ==1:
                              while True:
                                  print("1.Search by ID")
                                  print("2.Search by Name")
                                  print("3.Exit")
                                  PJ=int(input("Enter your choice(1,3):"))
                                  if PJ==1:
                                         S1=input("Enter ID:")
                                         S2="SELECT*from STAFF WHERE ID='{}'".format(S1)
                                         my.execute(S2)
                                  elif PJ==2:
                                      S3=input("Enter name:")
                                      S4="SELECT*from STAFF WHERE name LIKE '{}'".format(S3)
                                      my.execute(S4)
                                  elif PJ==3:
                                      break
                                  else:
                                      print("Invaid Choice")
                                  rec=my.fetchall()
                                  print()
                                  print(tabulate(rec,headers=['ID','NAME','SEX','DOB',
                                          'DEPARTEMENT','DOJ','SALARY','CONTACT'],tablefmt='psql'))
                                  print()
                                  print('-'*70)
                          elif DJ==2:
                              S5="SELECT COUNT(ID) 'No.Of Employees' FROM STAFF" 
                              my.execute(S5)
                              print("NUMBER OF EMPLOYEES ARE:")
                          elif DJ==3:
                              S6="SELECT AVG(SALARY) 'Average salary' from STAFF"
                              my.execute(S6)
                              print("AVERAGE SALARY OF STAFF IS:")
                          elif DJ==4:
                               S7="SELECT MAX(DOJ) 'Maximum Joining Date' from STAFF"
                               my.execute(S7)
                               print("OLDEST SERVING STAFF:")
                          elif DJ==5:
                               S8="SELECT MAX(SALARY) 'Maximum Salary' from STAFF"
                               my.execute(S8)
                               print("MAXIMUM SALARY GIVEN:")
                          elif DJ==6:
                               S9="SELECT MIN(SALARY) 'Minimum Salary' from STAFF"
                               my.execute(S9)
                               print("MINIMUM SALARY GIVEN:")

                          elif DJ==7:
                              S10="SELECT SUM(SALARY) 'Total Salary' from STAFF"
                              my.execute(S10)
                              print("TOTAL SALARY OF EMPLOYEES IS:") 

                          elif DJ==8:
                               break
                          else:
                              print('Invalid Choice')
                          sot=my.fetchall()
                          print()
                          print(tabulate(sot,tablefmt='grid'))
                          print()
                          print('-'*70)
                              
       elif st==2:
           print("--------------------------")
           print("Arts and Culture Museum")
           print("--------------------------")
           print()
           print("Choose your preference.......")
           while True:
               print(Pre())
               i=int(input("Enter your choice(1-4):"))
               if i==1:
                   p=Acc()
                   print("Account Created Successfully")
                   print("----------------------------")
                   print("Welcome To Arts And Culture Museum")
                   print("----------------------------------")
                   print()
                   while True:
                       print(Book())
                       j=int(input("Enter your choice(1-3):"))
                       if j==1:
                          print("Select to view.......")
                          while True:
                              print(Sel())
                              k=int(input("Enter your choice(1-8):"))
                              if k==1:
                                 print("--Harappan Galllery-----")
                                 print(Hap())
                              elif k==2:
                                  print("--Anthropology Department-----")
                                  print(Ant())
                              elif k==3:
                                  print("---Historic Period Gallery---")
                                  print(His())
                              elif k==4:
                                  print("----Medeival Art Gallery---")
                                  print(Med())
                              elif k==5:
                                  print("---Decorative Art Gallery---")
                                  print(Dec())
                              elif k==6:
                                  print("---Miniature Paintings----")
                                  print(Min())
                              elif k==7:
                                  print("---Other Facilities---")
                                  while True:
                                      print("Select:")
                                      print(Oth())
                                      l=int(input("Enter your choice(1-3):"))
                                      if l==1:
                                          print("---Canteen----")
                                          print(Can())
                                      elif l==2:
                                          print("--Gaming Zone--")
                                          print(Kid())
                                      elif l==3:
                                          break
                                      else:
                                          print("Invalid choice")
                                          print("-------------------------------------")
                                      input("Press Enter to continue............")
                                      print()
                                      print()
                                      print('_'*70)
                                      print()
                                      print()
                              elif k==8:
                                   break
                              else:
                                  print("Invalid choice")
                              input("ENTER TO CONTINUE........")
                              print()
                              print()
                              print('_'*70)
                              print()
                              print()
                       elif j==2:
                            print("---Book your ticket---")
                            print(Sel())
                            print("All section charge(500)(press 7)")
                            ghj=0
                            while True:
                                  print("Choose sections you want to visit......")
                                  m=int(input("Choose(1,8):"))                                  
                                  if m==1:
                                     ghj=ghj+(200)
                                  elif m==2:
                                       ghj=ghj+(150)
                                  elif m==3:
                                       ghj=ghj+(100)
                                  elif m==4:
                                       ghj=ghj+(50)
                                  elif m==5:
                                       ghj=ghj+(75)
                                  elif m==6:
                                       ghj=ghj+(75)
                                  elif m==7:
                                       ghj=ghj+(500)   
                                  else:
                                      break
                            print("Ticket Amount:",ghj)
                            n=int(input("How many people?"))
                            w=(ghj)*n
                            o=input("Want a guide?(Charge-200)(Y/N):")
                            if o=='Y':
                                x=w+(200)
                            else:
                                pass
                            print("Total Amount to be paid:",x)
                            print('\t'"Now we are taking you to payment gateway")
                            print("--Enter Card Details--")
                            r=Pay()
                            print(r)
                            q=input("Enter Date:")
                            print("YOUR ONLINE TICKET GOT GENERATED......")
                            tick(x,q,n)
                            print("WE ARE GLAD TO HAVE YOU SERVED!")
                       elif j==3:
                           break
                       else:
                           print("Inavalid choice")
                       print()
               elif i==2:
                   print("------WELCOME!------")
                   s=input("Enter name:")
                   t=input("Enter Password:")
                   
                   while True:
                       print(Log())
                       u=int(input("Enter your choice(1-4):"))
                       if u==1:
                             print("Enter new details")
                             p=Acc()
                             print("Account Updated Successfully")
                       elif u==2:
                           if r=='YES':
                               print("Successfully Booked")
                               print("Online Ticket Generated")
                           else:
                               print("Booking Pending")
                       elif u==3:
                           print("------Write A Review------")
                           v=input("Enter here:")
                       elif u==4:
                           break
                       else:
                           print("Invaid choice:")
                       print()
                       print()
                       print('_'*70)
                       print()
                       print()
               elif i==3:
                   print("Logged Out:")
                   print("Successfull!!!!!")
                   break
               elif i==4:
                   print(" For more Details Contact us on: '\n' email: www.eclipsecare@redifffmail.com '\n' PHONE NO: 9875703459")
                   print(" HOW MAY I HELP YOU???????")
                   enq=input("Enter your enquiry:")
                   print("Query saved successfully.......")
                   print("Our team will contact soon!!!!!!")
               else:
                    print("Invalid Choice")
           print()
           print()
           print("-"*90)
           print('\t\t\t'"WE WILL BE WAITING FOR YOUR ARRIVAL....")
           print("x"*90)
       elif st==3:
           
           print('THANK YOU VERY MUCH!!!!!!!!!')
           break

       else:
           print("Sorry,but someting went wrong......")
else:
    print("Thanks for your visit!!!!!!!")
