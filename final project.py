#PROJECT ON EMPLOYEE INFORMATION SYSTEM
import mysql.connector
from mysql.connector import Error
conn=mysql.connector.connect(host="localhost",user="root",password="4444",database="EMPLOYEE1")
if conn.is_connected():
    print("SUCCESSFULLY CONNECTED")
C=conn.cursor()
table="""create table emp_data11(
                                EMP_ID CHAR(5) primary key,
                                EMP_NAME CHAR(20),
                                FATHER_NAME CHAR(20),
                                DEPT CHAR(20),
                                DESIGNATION CHAR(20),
                                PHONE_NO INT,
                                SEX CHAR(20),
                                DOJ DATE,
                                ATTENDANCE INT,
                                LEAVES INT,
                                BASIC_SALARY INT,
                                MEDICAL_LEAVES INT,
                                GROSS_SALARY FLOAT  DEFAULT NULL)"""

C.execute(table)

print("TABLE CREATED SUCCESSFULLY")
print()

#FUNCTION TO INSERT RECORDS IN THE TABLE
def INSERT_REC():
    conn=mysql.connector.connect(host="localhost",user="root",password="4444",database="EMPLOYEE1")
    C=conn.cursor()
    choice="y"
    while choice=="y":
        EMP_ID=input("ENTER THE EMPLOYEE ID : ")
        EMP_NAME=input("ENTER THE EMPLOYEE NAME : ")
        FATHER_NAME=input("ENTER THE EMPLOYEE FATHER'S NAME : ")
        DEPT=input("ENTER THE DEPARTMENT : ")
        DESIGNATION=input("ENTER THE DESIGNATION OF EMPLOYEE : ")
        PHONE_NO=int(input("ENTER THE PHONENO OF EMPLOYEE : "))
        SEX=input("ENTER THE SEX OF EMPLOYEE : ")
        DOJ=input("ENTER THE DATE OF JOINING : ")
        ATTENDANCE=int(input("ENTER THE NO. OF DAYS PRESENT : "))
        LEAVES=int(input("ENTER THE NO. OF LEAVES TAKEN : "))
        BASIC_SALARY=int(input("ENTER THE BASIC SALARY="))
        MEDICAL_LEAVES=int(input("ENTER THE NO. OF MEDICAL LEAVES TAKEN : "))
        GROSS_SALARY=0
        QUERY="insert into emp_data11 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        V=(EMP_ID,EMP_NAME,FATHER_NAME,DEPT,DESIGNATION,PHONE_NO,SEX,DOJ,ATTENDANCE,LEAVES,BASIC_SALARY,MEDICAL_LEAVES,GROSS_SALARY)
        C.execute(QUERY,V)
        conn.commit()
        print(C.rowcount,"RECORD INSERTED INTO THE TABLE")
        print()
        choice=input("DO YOU WANT TO INSERT ANY OTHER RECORD? (Y/N) : ")
        if choice!="y":
            C.close();
        print()    


#FUNCTION TO DISPLAY THE RECORDS
def DISPLAY_REC():
    conn=mysql.connector.connect(host="localhost",user="root",password="4444",database="EMPLOYEE1")
    C=conn.cursor()
    QUERY1="select * from emp_data11"
    C.execute(QUERY1)
    REC=C.fetchall()
    for x in REC:
        print("EMP_ID            =",x[0])
        print("EMP_NAME          =",x[1])
        print("FATHER_NAME       =",x[2])
        print("DEPT              =",x[3])
        print("DESIGNATION       =",x[4])
        print("PHONE_NO          =",x[5])
        print("SEX               =",x[6])
        print("DOJ               =",x[7])
        print("ATTENDANCE        =",x[8])
        print("LEAVES            =",x[9])
        print("BASIC_SALARY      =",x[10])
        print("MEDICAL_LEAVES    =",x[11])
        print("______")
    C.close()
              
    

#FUNCTION TO SEARCH ANY RECCORD
def SEARCH_REC():
    conn=mysql.connector.connect(host="localhost",user="root",password="4444",database="EMPLOYEE1")
    C=conn.cursor()
    found=False
    A=int(input("To search w.r.t EMP_ID,Type 1 or to search w.r.t EMP_NAME,Type 2"))
    if A==1:
        ID=input("ENTER THE EMPLOYEE ID OF THE EMPLOYEE YOU WANT TO SEARCH : ")
        print()
        QUERY2="select * from emp_data111 where EMP_ID=%s"
        VALUE=(ID,)
        C.execute(QUERY2,VALUE)
        print()
        D=C.fetchall()
        for x in D:
            print("____ DETAILS OF THE EMPLOYEE ID :",ID,"ARE :")
            print("____")
            print("EMP_ID            =",x[0])
            print("EMP_NAME          =",x[1])
            print("FATHER_NAME       =",x[2])
            print("DEPT              =",x[3])
            print("DESIGNATION       =",x[4])
            print("PHONE_NO          =",x[5])
            print("SEX               =",x[6])
            print("DOJ               =",x[7])
            print("ATTENDANCE        =",x[8])
            print("LEAVES            =",x[9])
            print("BASIC_SALARY      =",x[10])
            print("MEDICAL_LEAVES    =",x[11])
            found=True
            if found==False:
                print()
                print("___SEARCHED RECORD DOESN'T EXIST___")
            else:
                print()
                print("___RECORD FOUND SUCCESSFULLY___")    
    elif A==2:
        NAME=input("ENTER THE EMPLOYEE NAME OF THE EMPLOYEE YOU WANT TO SEARCH : ")
        print()
        QUERY3="select * from emp_data11 where EMP_NAME=%s"
        VALUE=(NAME,)
        C.execute(QUERY3,VALUE)
        print()
        P=C.fetchall()
        for x in P:
            print("____ DETAILS OF THE EMPLOYEE NAME :",NAME,"ARE :")
            print("____")
            print("EMP_ID            =",x[0])
            print("EMP_NAME          =",x[1])
            print("FATHER_NAME       =",x[2])
            print("DEPT              =",x[3])
            print("DESIGNATION       =",x[4])
            print("PHONE_NO          =",x[5])
            print("SEX               =",x[6])
            print("DOJ               =",x[7])
            print("ATTENDANCE        =",x[8])
            print("LEAVES            =",x[9])
            print("BASIC_SALARY      =",x[10])
            print("MEDICAL_LEAVES    =",x[11])
            found=True
            if found==False:
                print()
                print("___SEARCHED RECORD DOESN'T EXIST___")
            else:
                print()
                print("___RECORD FOUND SUCCESSFULLY___")
        C.close()



#FUNCTION FOR UPDATING RECORDS IN THE TABLE
def UPDATE_REC():
    R=input("ENTER THE ID OF THE EMPLOYEE TO BE UPDATED : ")
    ans="y"
    while ans=="y":
        print()
        print("___SELECT THE FIELD YOU WANT TO UPDATE___")
        print("1. PHONE_NO")
        print("2. ATTENDANCE")
        print("3. LEAVES")
        print("4. ALL DETAILS")
        print("5. NO UPDATION")
        print()
        x=int(input("___ENTER YOUR CHOICE FOR UPDATION___"))
        if x==1:
            conn=mysql.connector.connect(host="localhost",user="root",password="4444",database="EMPLOYEE1")
            C=conn.cursor()
            DT=input("___INPUT THE NEW PHONE NUMBER___")
            query="update emp_data11 set phone_no=%s where emp_id=%s"
            data1=(DT,R)
            C.execute(query,data1)
            conn.commit()
            print()
            print("___PHONE NUMBER OF ID = ",R," IS UPDATED SUCCESSFULLY___")
        elif x==2:
            conn=mysql.connector.connect(host="localhost",user="root",password="4444",database="EMPLOYEE1")
            C=conn.cursor()
            ATT=int(input("___INPUT THE NEW ATTENDANCE___"))
            query="update emp_data11 set attendance=%s where emp_id=%s"
            data2=(ATT,R)
            C.execute(query,data2)
            conn.commit()
            print()
            print("___ATTENDANCE OF ID = ",R," IS UPDATED SUCCESSFULLY___")
        elif x==3:
            conn=mysql.connector.connect(host="localhost",user="root",password="4444",database="EMPLOYEE1")
            C=conn.cursor()
            LV=int(input("___INPUT THE NEW LEAVES___"))
            query="update emp_data11 set leaves=%s where emp_id=%s"
            data3=(LV,R)
            C.execute(query,data3)
            conn.commit()
            print()
            print("___LEAVES OF ID = ",R," IS UPDATED SUCCESSFULLY___")
        elif x==4:
            conn=mysql.connector.connect(host="localhost",user="root",password="4444",database="EMPLOYEE1")
            C=conn.cursor()
            DT=input("___INPUT THE NEW PHONE NUMBER___")
            ATT=int(input("___INPUT THE NEW ATTENDANCE___"))
            LV=int(input("___INPUT THE NEW LEAVES___"))
            query="update emp_data11 set phone_no=%s,attendance=%s,leaves=%s where emp_id=%s"
            data=(DT,ATT,LV,R)
            C.execute(query,data)
            conn.commit()
            print()
            print("___DETAILS OF EMPLOYEE ID = ",R," IS UPDATED SUCCESSFULLY___")
            print()
        elif x==5:
            conn=mysql.connector.connect(host="localhost",user="root",password="4444",database="EMPLOYEE1")
            C=conn.cursor()
            query="select * from emp_data11 where emp_id=%s"
            data=(R,)
            print("NO UPDATION IS DONE")
            C.execute(query,data)
            D=C.fetchone()
            EMP_ID=D[0]
            EMP_NAME=D[1]
            FATHER_NAME=D[2]
            DEPT=D[3]
            DESIGNATION=D[4]
            PHONE_NO=D[5]
            SEX=D[6]
            DOJ=D[7]
            ATTENDANCE=int(D[8])
            LEAVES=int(D[9])
            BASIC_SALARY=int(D[10])
            MEDICAL_LEAVES=int(D[11])
            print("EMP_ID            =",EMP_ID)
            print("EMP_NAME          =",EMP_NAME)
            print("FATHER_NAME       =",FATHER_NAME)
            print("DEPT              =",DEPT )
            print("DESIGNATION       =",DESIGNATION)
            print("PHONE_NO          =",PHONE_NO)
            print("SEX               =",SEX)
            print("DOJ               =",DOJ)
            print("ATTENDANCE        =",ATTENDANCE)
            print("LEAVES            =",LEAVES)
            print("BASIC_SALARY      =",BASIC_SALARY)
            print("MEDICAL_LEAVES    =",MEDICAL_LEAVES)
            print()
        ans=input("DO YOU WANT TO DO MORE UPDATION? (Y/N)= ")
        if ans!="y":
            C.close()


#FUNCTION FOR DELETION OF RECORDS
def DELETE_REC():
    conn=mysql.connector.connect(host="localhost",user="root",password="4444",database="EMPLOYEE1")
    C=conn.cursor()
    print("___YOU HAVE ENTERED IN DELETE SECTION___")
    print()
    print("___HERE YOU ARE HAVING 3 OPTIONS___")
    print()
    print("1. TO DELETE ANY ONE DESIRED RECORD")
    print("2. TO DELETE ALL THE RECORDS")
    print("3. TO DELETE NO RECORD")
    print()
    choice=int(input("___ENTER YOUR CHOICE___"))
    print()
    if choice==1:
        R=input("__ENTER THE EMPLOYEE ID OF THE EMPLOYEE WHOSE RECORD IS TO BE DELETED__")
        data=(R,)
        query="delete from emp_data11 where emp_id=%s"
        C.execute(query,data)
        conn.commit()
        print()
        print("___RECORD OF ID ",R," IS DELETED___")              
    elif choice==2:
        query="delete from emp_data11"
        C.execute(query)
        conn.commit()
        print()
        print("___RECORDS DELETED SUCCESSFULLY.___")
    elif choice==3:
        print("DON'T WANT TO DELETE ANY RECORD")
        C.close()


#FUNCTION FOR RECORDING ATTENDANCE
def ATTENDANCE():
    conn=mysql.connector.connect(host="localhost",user="root",password="4444",database="EMPLOYEE1")
    C=conn.cursor()
    n=input("ENTER THE NAME OF THE EMPLOYEE")
    found=False
    i=input("ENTER ID OF THE EMPLOYEE:")
    query3="select * from emp_data11 where EMP_ID=%s"
    value=(i,)
    C.execute(query3,value)
    print()
    d=C.fetchall()
    for x in d:
        print("___Attendance record___")
        print()
        print("EMP_ID          =",x[0])
        print("EMP_NAME        =",x[1])
        print("New Attendance  =",x[8]+1)
        found=True
        conn=mysql.connector.connect(host="localhost",user="root",password="4444",database="EMPLOYEE1")
        C=conn.cursor()
        ATT=x[8]+1
        query="update emp_data11 set attendance=%s where emp_id=%s"
        data2=(ATT,i)
        C.execute(query,data2)
        conn.commit()
    if found==False:
        print()
        print("___Record doesn't exist___")
    else:
        print()
        print("___Attendance Recorded___")


#NET SALARY PROGRAM
def NET_SALARY():
    conn=mysql.connector.connect(host="localhost",user="root",password="4444",database="EMPLOYEE1")
    C=conn.cursor()
    found=False
    N1=input("ENTER EMPLOYEE ID=")
    QUERY4="SELECT * FROM emp_data11 WHERE EMP_ID=%s"
    VALUE=(N1,)
    C.execute(QUERY4,VALUE)
    print()
    d1=C.fetchall()
    GS=0
    for x in d1:
        print("__SALARY RECORD__")
        print()
        print("EMP_ID=",x[0])
        print("EMP_NAME=",x[1])
        print("BASIC_SALARY=",x[10])
        print()
        print("There are 2 casual leaves and 4 medical leaves allowed per month")
        print()
        print("LEAVES=",x[9])
        print("MEDICAL LEAVES TAKEN =",x[11])
        found=True
        if x[9]<=2 and x[11]<=4:
            GS=x[10]+((x[10]/30)*(2-x[9]))
            print("As the employee has taken less than 2 leaves, so he will get an increment in his salary")
            print()
            print("GROSS SALARY OF EMPLOYEE=",GS)
            x1="UPDATE emp_data11 SET GROSS_SALARY={} WHERE EMP_ID='{}'". format(GS,N1)
            C.execute(x1)
            conn.commit()
            
        elif x[9]>2:
            if x[11]>4:
                GS=x[10]-((x[10]/30)*(x[11]-4)+(x[10]/30)*(x[9]-2))
                print("as the employee has taken leaves more than casual leaves and medical leaves more than permitted leaves, so there will be decrement in his salary") 
                print()
                print("GROSS SALARY OF EMPLOYEE=",GS)
                x1="UPDATE emp_data11 SET GROSS_SALARY={} WHERE EMP_ID='{}'". format(GS,N1)
                C.execute(x1)
                conn.commit()
            elif x[11]<4:
                GS=x[10]-((x[10]/30)*(x[9]-2))
                print("as the employee has taken leaves more than casual leaves, so there will be decrement in his salary") 
                print()
                print("GROSS SALARY OF EMPLOYEE=",GS)
                x1="UPDATE emp_data11 SET GROSS_SALARY={} WHERE EMP_ID='{}'". format(GS,N1)
                C.execute(x1)
                conn.commit()
        else:
            GS=x[10]-((x[10]/30)*(x[11]-2))
            print("as the employee has taken medical leaves more than permitted, so there will be decrement in his salary") 
            print()
            print("GROSS SALARY OF EMPLOYEE=",GS)
            x1="UPDATE emp_data11 SET GROSS_SALARY={} WHERE EMP_ID='{}'". format(GS,N1)
            C.execute(x1)
            conn.commit()
                
                
    if found==False:
        print()
        print("RECORD DOESN'T EXIST")
#MAIN PROGRAM
        
print("___________________")
print()
print("               EMPLOYEE INFORMATION SYSTEM                  ")
print()
print("___________________")
print()
print("_____LET US START THE MENU ______")
print()
ans="y"
while ans=="y" or ans=="Y":
    print("1.__INSERT RECORDS__")
    print("2.__DISPLAY RECORDS__")
    print("3.__SEARCH RECORDS__")
    print("4.__UPDATE RECORDS__")
    print("5.__DELETE RECORDS__")
    print("6.__ATTENDANCE PROGRAM__")
    print("7.__NET SALARY__")
    print()
    choice=int(input("PLEASE ENTER YOUR CHOICE : "))
    if choice==1:
        INSERT_REC()
    elif choice==2:
        DISPLAY_REC()
    elif choice==3:
        SEARCH_REC()
    elif choice==4:
        UPDATE_REC()
    elif choice==5:
        DELETE_REC()
    elif choice==6:
        ATTENDANCE()
    elif choice==7:
        NET_SALARY()
    else:
        print("CHOICE YOU ENTERED IS INVALID !! ")
        ch=int(input("PLEASE ENTER YOUR CHOICE : "))
    print()
    ans=input("__YOU WANT TO RUN THE MENU AGAIN ? (Y/N)___: ")
    if ans!="y" or ans!="Y":
        print("___THANK YOU FOR ACCESSING THE PROJECT___")
