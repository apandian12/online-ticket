

from turtle import pd
import mysql.connector

mydb=mysql.connector.connect(host="localhost", user="root", password="Alex@2000",database="batch57_db")
if mydb.is_connected():
    print("successfully connected")

def menu():

    print()
    print("**********************************************")
    print(       "   ONLINE TICKET BOOKING SYSTEM     ")
    print("1. Create table passenger")
    print("2. Add new passenger detail")
    print("3. Create table traindetail")
    print("4. Add new in train details")
    print("5. Show all from train detail")
    print("6. Show all from passenger detail")
    print("7. Shoe PNR NO")
    print("8. Reservation of ticket")
    print("9. Cancellation of resvervation")


menu()

# PNR is the abbervatin of "Passenger Name Record" and
# it is also used as a booking number
def create_passengers():
    c1=mydb.mycursor()
    c1.execute("create table if not exists passengers(pas_name varchar(30),age varchar(25),train_no varchar(30),no_of_pas varchar(25),cls varchar(25),destination varchar(30),amt varchar(20),status varchar(25),pnr_no varchar(25)")
    print("create table passengers")

def add_passengers():
    c1=mydb.mycursor()
    L=[]
    pas_name=input("ENTER YOUR NAME:")
    L.append(pas_name)
    age=input("ENTER YOUR AGE:")
    L.append(age)
    train_no=input("ENTER YOUR TRAIN NO:")
    L.append(train_no)
    no_of_pas=input("ENTER NO OF PASSENGERS:")
    L.append(no_of_pas)
    cls=input("ENTER YOUR CLASS:")
    L.append(cls)
    destination=("ENTER YOUR DESTINATION:")
    L.append(destination)
    amt=("ENTER FARE:")
    L.append(amt)
    status=input("ENTER YOUR STATUS:")
    L.append(status)
    pnr_no=input("ENTER YOUR PNR NO:")
    L.append(pnr_no)
    pas=(L)
    mysql="insert into passenger(pas_name,age,train_no,no_of_pas,cls,destination,amt,status,pnr_no)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    c1.execute(mysql,pas)
    mydb.commit()
    print("Record of passenger inserted")
    df= pd.read_mysql("Select * from passengers", mydb)
    print(df)

def create_traindetail():
    c1=mydb.mycursor()
    c1.execute("create table if not exists traindetail(train_name varchar(30),train_number varchar(25),source varchar(30),fare varchar(10),ac1 varchar(25),ac2 varchar(30), slp varchar(25)")
    print("create table traindetail")

def add_traindetail():
    c1=mydb.mycursor()
    df=pd.read_mysql("select * from traindetail",mydb)
    print(df)
    L=[]
    train_name=input("ENTER YOUR TRAIN NAME:")
    L.append(train_name)
    train_number=input("ENTER YOUR TRAIN_NUMBER:")
    L. append(train_number)
    source=input("ENTER YOUR SOURCE OF TRAIN:")
    L.append(source)
    destination=input("ENTER YOUR DESTINATION OF TRAIN:")
    L.append(destination)
    fare=input("ENTER YOUR FARE OF STATION:")
    L.append(fare)
    ac1=input("ENTER NO OF SEATS FOR AC1:")
    L.append(ac1)
    ac2=input("ENTER NO OF SEATS FOR AC2:")
    L.append(ac2)
    slp=input("ENTER NO OF SEATS FOR SLEEPER:")
    L.append(slp)
    f=(L)
    mysql="insert into traindetail(train_name,train_number,source,destination,fare,ac1,ac2,slp)values(%s,%s,%s,%s,%s,%s,%s,%s,)"
    c1.execute(mysql,f)
    mydb.commit()
    print("Record inserted in train detail")

def showtraindetail():
    print("ALL TRAIN DETAIL")
    df=pd.read_mysql("select * from traindetail",mydb)
    print(df)

def showpassengers():
    print("ALL PASSENGERS DETAIL")
    df=pd.read_mysql("select * from passengers",mydb)
    print(df)

def disp_pnr_no():
    print("PNR STATUS WINDOW")
    a=(input("ENTER TRAIN NO: "))
    qry="select pas_name,status from passengers where train_number=%s;"%(a,)
    df=pd.read_mysql(qry,mydb)
    print(df)

def ticket_reservation():
    print("WE HAVE THE FOLLOWING SEAT TYPES FOR YOU:-")
    print("TRAIN NAME IS 1 FOR CHENNAI EXPRESS FROM CHENNAI_CENTRAL")
    print()
    print("1. FIRST CLASS AC RS 5000 Per PERSON")
    print("2. SECOND CLASSN AC RS 4000 Per PERSON")
    print("3. THIRD CLASS AC RS 3000 Per PERSON")
    print("4. FOR SLEEPER RS 2000 Per PERSON")
    print()
    print("1. TRAIN_NAME IS 2 FOR GOA EXPRESS FROM CHENNAI_CENTRAL:-")
    print()
    print("1. FIRST CLASS AC RS 9000 Per PERSON")
    print("2. SECOND CLASSN AC RS 8000 Per PERSON")
    print("3. THIRD CLASS AC RS 6000 Per PERSON")
    print("4. FOR SLEEPER RS 5000 Per PERSON")
    
    train_name=input("ENTER YOUR CHOICE OF TRAIN NAME PLESE->")
    print(train_name)
    x=int(input("ENTER YOUR CHOICE OF TICKET  PLEASE ->"))
    n=int(input("HOW MANY TICKETS YOU WANT:"))

    if (x==1):
        print("YOU HAVE CHOOSEN FIRST CLASS AC TICKET")
        s=5000*n
    elif(x==2):
        print("YOU HAVE CHOOSEN SECOND CLASS AC TICKET")
        s=4000*n
    elif(x==3):
        print("YOU HAVE CHOOSE THIRD CLASS AC TICKET")
        s=3000*n
    elif(x==4):
        print("YOU HAVE CHOOSEN SLEEPER ")
        s=2000*n    
    else:
        print("INVAILD ID OPTION")

        print("PLEASE CHOOSE THE TRAIN")
        print("your TOTAL TICKET PRICE is =",s,"\n")

    if (x==1):
        print("YOU HAVE CHOOSEN FIRST CLASS AC TICKET")
        s=9000*n
    elif(x==2):
        print("YOU HAVE CHOOSEN SECOND CLASS AC TICKET")
        s=8000*n
    elif(x==3):
        print("YOU HAVE CHOOSE THIRD CLASS AC TICKET")
        s=6000*n
    elif(x==4):
        print("YOU HAVE CHOOSEN SLEEPER ")
        s=5000*n    
    else:
        print("INVAILD ID OPTION")

        print("PLEASE CHOOSE A TRAIN")
        print("your TOTAL TICKET PRICE is =",s,"\n")

def cancle():

    print("before any changes in the STATUS")
    df=pd.read_mysql("select * from passengers",mydb)
    print(df)
    mc=mydb.mycursor()
    mc.execute("update passengers set status='cancelled' where pnr_no='A1001")
    mydb.commit()
    df=pd.read_mysql("select * from passengers",mydb)
    print(df)

opt=""
opt=int(input("ENTER YOUR CHOICE :"))
if opt==1:
    create_passengers()
elif opt==2:
    add_passengers()
elif opt==3:
    create_traindetail()
elif opt==4:
    add_traindetail()
elif opt==5:
    showtraindetail()
elif opt==6:
    showpassengers()
elif opt==7:
    disp_pnr_no()
elif opt==8:
    ticket_reservation()
elif opt==9:
    cancle()

else:
    print("invaild id option") 

