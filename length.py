
length = {"pm":1e-12,"angstrom":1e-10,"nm":1e-9,"microm":1e-6,"mm":0.001, "cm":0.01,"dm":0.1, "m":1, "Dm":10, "hm":100,"km":1000, "inch":0.0254, "feet":0.3048, "mile":1609.34, "yard":0.9144}
 
def L():

    available_units = length.keys()
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
                output = val*length[unit_in]/length[unit_out]
                print(val,unit_in,"=",round(output,3),unit_out)
            else:
                print("Unit not available")
        else:
            print("Unit not available")
    
    except ValueError:
        print("Enter float numbers only")

