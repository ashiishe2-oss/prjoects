
def caclulator():
    print("--SIMPLE CALCLULATOR--")

    num1=int(input("ENTER NUM1: "))
    num2=int(input("ENTER NUM2: "))
    
    print("PICK A OPERATION")
    print("1.ADD")
    print("2.SUBTARCT")
    print("3.MULTIPLY")
    print("4.DIVIDE")

    


    choice=int(input("YOUR CHOICE: "))
    try:
        if choice==1:
            print(f"{num1}+{num2}={num1+num2}")
        elif choice==2:
            print(f"{num1}-{num2}={num1-num2}")
        elif choice ==3:
            print(f"{num1}x{num2}={num1*num2}")
        elif choice==4:
            if num2==0:
             print("NUM CANNOT BE DIVIDED BY 0 ")
            print(f"{num1}/{num2}={num1/num2}")

    except ValueError:
        print("INVALID")
        
caclulator()

   
