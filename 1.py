students=[[]]
def addstudents(inv,i):
    n=input("enter the name of student")
    s=int(input("enter id"))
    c=input("enter class")
    l=input("enter grades")
    inv['name']=n
    inv['studentid']=s
    inv['class']=c
    inv['listofgrades']=l
    students[i]=inv
    i=i+1
    print(students)

def update_grades(students):
    id=int(input('enter the id you want to edit'))
    for i in students:
        if(i==inv[s]):
            new=input("enter the upgraded list")
            inv['listofgrades']=new
def calculate_average(students):
    id=int(input('enter the id you want to edit'))
    for i in students:
        if(i==inv[s]):
            cnt=0
            sumi=0
            for j in inv['listofgrades']:
                cnt++
            for q in inv['listofgrades']:
                sumi=sumi+inv['listofgrades'][q]
                avg=sum/cnt
                return avg
            
                
                
inv=dict()
i=0
addstudents(inv,i)
    
        
    
    
    

    
    
