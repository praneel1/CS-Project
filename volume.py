volume = {"yl":1e-24,"zl":1e-21,"al":1e-18,"fl":1e-15,"pl":1e-12,"nl":1e-9,"microl":1e-6,"ml":0.001, "cl":0.01,"dl":0.1, "l":1, "Dl":10, "hl":100,"kl":1000,"cm3":0.001}

def V():

    available_units = volume.keys()
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
                output = val*volume[unit_in]/volume[unit_out]
                print(val,unit_in,"=",output,unit_out)
            else:
                print("Unit not available")
        else:
            print("Unit not available")
    
    except ValueError:
        print("Enter float numbers only")

