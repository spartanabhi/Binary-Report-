import pickle
d = {}


with open("records.dat" , "wb") as f:
    chh = "y"
    while True :
        print("0. Create Records ")
        print("1. Add Records")
        print("2. Search Records")
        print("3. Update Records")
        print("4. Delete Records")
        print("5. Display Records")
        chh = input("Wanna initialize : ")
        if chh == "n":
            break
        rec = int(input("Enter your choice : "))
        if rec == 0:
                
            def create():
                ch = "y"
                s = int(input("How many records u wanna enter : "))
                for i in range(s) :
                    print("------------------------------------")
                    roll = int(input("Enter the Roll Number : "))
                    d[roll] = {}
                    name = input("Enter the Name : ")
                    clas = input("Enter the Class : ")
                    add   = input("Enter the Address : ")
                    print("------------------------------------")
                    d[roll]["Name"] = name
                    d[roll]["Class"] = clas
                    d[roll]["Address"] = add
                    
                    pickle.dump(d , f)
            
            create()
        elif rec == 1 :
            def add():
                ch = "y"
                s = int(input("How many records u wanna add : "))
                for i in range(s) :
                    print("------------------------------------")
                    roll = int(input("Enter the Roll Number : "))
                    d[roll] = {}
                    name = input("Enter the Name : ")
                    clas = input("Enter the Class : ")
                    add   = input("Enter the Address : ")
                    print("------------------------------------")
                    d[roll]["Name"] = name
                    d[roll]["Class"] = clas
                    d[roll]["Address"] = add
                    ch = input("wanna continue : ")
                    pickle.dump(d , f)
            
            add()
        elif rec == 2 :
            def search():
                s = int(input("Enter the Roll Number to be searched : "))
                for i in d :
                    if i == s :
                        print("------------------------------------")
                        print("Roll    :  " , i)
                        print("Name    :  " , d[i]["Name"])
                        print("Class   :  " , d[i]["Class"])
                        print("Address :  " , d[i]["Address"])
                        print("------------------------------------")
                        
                
            search()
            
        elif rec == 3:
            def update():
                s = int(input("Enter the Roll Number to be Updated : "))
                for i in d :
                    if i == s :
                        print("------------------------------------")
                        print("Roll    :  " , i)
                        print("Name    :  " , d[i]["Name"])
                        print("Class   :  " , d[i]["Class"])
                        print("Address :  " , d[i]["Address"])
                        print("------------------------------------")
                        print(" 1. Name \n 2. Class \n 3. Address")
                        o = int(input("Enter the choice : "))
                        
                        if o == 1 :
                            Nname = input("Enter the New Name : ")
                            
                            d[i]["Name"] = Nname
                            print("Name Updated!")
                        elif o == 2 :
                            Nclass = input("Enter the New Class : ")
                            
                            d[i]["Class"] = Nclass
                            print("Class Updated!")
                        elif o == 3 :
                            Nadd = input("Enter the New Address : ")
                            d[i]["Address"] = Nadd
                            print("Address Updated!")
                        pickle.dump(d , f)    
            update()    
            
        elif rec == 4 :
            def delete():
                rno = int(input("Enter the Roll Number to be Deleted : "))
                del d[rno]
                print()
                print("Roll Number Deleted!")
                print()
                pickle.dump(d , f)
            delete()    
        elif rec == 5:
            def display():
                t = int(input(" 1.All Records \n 2.Individual Records "))
                if t == 1 :
                    for i in d :
                        print("------------------------------------")
                        print("Roll    :  " , i)
                        print("Name    :  " , d[i]["Name"])
                        print("Class   :  " , d[i]["Class"])
                        print("Address :  " , d[i]["Address"])
                        print("------------------------------------")
                elif t == 2 :
                    s = int(input("Enter the Roll Number to be searched : "))
                    for i in d :
                        if i == s :
                            print("------------------------------------")
                            print("Roll    :  " , i)
                            print("Name    :  " , d[i]["Name"])
                            print("Class   :  " , d[i]["Class"])
                            print("Address :  " , d[i]["Address"])
                            print("------------------------------------")
    
                
            
            display()    
            
            
            
