speed = {"km/h":0.277778, "m/s":1, "km/s":1000 ,"cm/s":0.01, "knot":0.514}

def S():
    available_units = speed.keys()
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
                output = val*speed[unit_in]/speed[unit_out]
                print(val,unit_in,"=",round(output,2),unit_out)
            else:
                print("Unit not available")
        else:
            print("Unit not available")
    
    except ValueError:
        print("Enter float numbers only")