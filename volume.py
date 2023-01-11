volume = {"nl":1e-9,"microl":1e-6,"ml":0.001, "cl":0.01,"dl":0.1, "l":1, "Dl":10, "hl":100,"kl":1000,"cm3":0.001, "m3":1000, "gallon":4.54609, "pint":0.568261}

def V():

    available_units = volume.keys()
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
                output = val*volume[unit_in]/volume[unit_out]
                print(val,unit_in,"=",round(output,3),unit_out)
            else:
                print("Unit not available")
        else:
            print("Unit not available")
    
    except ValueError:
        print("Enter float numbers only")

