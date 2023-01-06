
weight = {"yg":1e-24,"zg":1e-21,"ag":1e-18,"fg":1e-15,"pg":1e-12,"ng":1e-9,"microg":1e-6,"mg":0.001, "cg":0.01,"dg":0.1, "g":1, "Dg":10, "hg":100,"kg":1000, "ton":1e+6}
 
def W():

    available_units = weight.keys()
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
                output = val*weight[unit_in]/weight[unit_out]
                print(val,unit_in,"=",output,unit_out)
            else:
                print("Unit not available")
        else:
            print("Unit not available")
    
    except ValueError:
        print("Enter float numbers only")

