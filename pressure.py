
pressure = {"Pa":1,"bar":100000,"atm":101325,"psi":6894.7572932,"torr":133.32236842}
 
def P():

    available_units = pressure.keys()
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
                output = val*pressure[unit_in]/pressure[unit_out]
                print(val,unit_in,"=",round(output,3),unit_out)
            else:
                print("Unit not available")
        else:
            print("Unit not available")
    
    except ValueError:
        print("Enter float numbers only")