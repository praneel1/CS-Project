currency = {"rs":1, "$":81.71, "gbp":99.41 ,"euro":87.84, "yen":0.62, "rub":1.17}

def C():
    available_units = currency.keys()
    try:
        val = float(input("Enter Value: "))   # Input Value
        for unit in available_units:
            print(unit,end="  ")              
        unit_in = input("\n unit: ")      #Input Unit
        if unit_in in available_units:
            print("convert ", val , unit_in, "to? ")
            for unit in available_units:
                print(unit, end=" ")    #Output Unit
            unit_out = input("\n ====>")
            if unit_out in available_units:
                print("Converting",val,unit_in, "to", unit_out)
                output = val*currency[unit_in]/currency[unit_out]
                print(val,unit_in,"=",round(output,2),unit_out)
            else:
                print("Unit not available")
        else:
            print("Unit not available")
    
    except ValueError:
        print("Enter float numbers only")