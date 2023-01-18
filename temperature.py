output = 0

def T():
    
    try:
        a=float(input("Enter temperature\n: "))
        print("Celcius (C),Fahrenheit (F),Kelvin (K)?")
        b=input("Unit\n: ")
        print("convert ", a , b, "to?")
        d=input(": ")
        if b=="C" and d=="F":
            output=(9/5*a)+32
        # print(a,"f")
        elif b=="C" and d=="K":
            output=a+273
        # print(a,"kelvin")
        elif b=="F" and d=="C":
            output=(5/9*a)+32
            #print(a,"degree celcius")
        elif b=="F" and d=="K":
            output=((a-32)*5/9)+273
            #print(a,"kelvin")	
        elif b=="K" and d=="C":
            output=a-273
            #print(a,"degree celcius")
        elif b=="K" and d=="F":
            output=1.8*(a-273.15)+32
            #print(a,"f")
        else:
            output = -999999999999999999999999999999999999999999999
            

        
        print(a,b,"=",round(output,3),d)
    except ValueError:
        print("Not a number")