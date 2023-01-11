import math
angles = {"degrees":math.pi/180, "radians":1, "gradians":math.pi/200 ,"arcminute":math.pi/(180*60)}

def A():
    available_units = angles.keys()
    try:
        val = float(input("Enter Value: "))   # Input Value
        for unit in available_units:
            print(unit,end="  ")              
        unit_in = input("unit: ")      #Input Unit
        if unit_in in available_units:
            print("convert ", val , unit_in, "to? ")
            for unit in available_units:
                print(unit, end=" ")    #Output Unit
            unit_out = input()
            if unit_out in available_units:
                print("Converting",val,unit_in, "to", unit_out)
                output = val*angles[unit_in]/angles[unit_out]
                print(val,unit_in,"=",round(output,2),unit_out)
            else:
                print("Unit not available")
        else:
            print("Unit not available")
    
    except ValueError:
        print("Enter float numbers only")