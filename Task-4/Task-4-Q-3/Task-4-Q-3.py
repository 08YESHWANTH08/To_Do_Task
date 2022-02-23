from tabulate import tabulate
list1=[["Roll No","Name","Marks"]] #Yeshwanth A CH.EN.U4CSE21263
l=[]
cond='Y'
dup=1
while (cond.lower()=='y'):
    print("Enter 1 to Add A Row\nEnter 2 to Display The Table\nEnter 3 to Display A single Row")
    choice=int(input("Enter Your Choice:"))
    if choice==1:
        list1.append([int(input("Enter The Roll No.:")),input("Enter The Student Name:"),int(input("Enter The Marks:"))])
    elif choice==2:
        print(tabulate(list1,headers='firstrow',tablefmt='grid'))
    elif choice==3:
        element = int(input("Enter The Roll No:"))
        for i in range(len(list1)):
            if element == list1[i][0]:
                l=[list1[i]]
                print(l)
                print(tabulate(l,headers=["Roll No","Name","Marks"],tablefmt='grid'))
        if l==[]:
            print("No Data Found")
    else:
        print("Enter A Valid Option\n")
    cond=input("Do You Want To Continue ? (Y/N):\n")
