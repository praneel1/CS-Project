## Input type of conversion
## Types of COnversions - length, weight, volume, imperial, currency, temperature, speed, angles
## Input VALUE
## Input SI UNIT FOR INPUT
## Input SI UNIT FOR OUTPUT
##SI INPUT / SI OUTPUT

from length import *

while True:
    convert_type = input("Enter type: L(Length), W(Weight), V(Volume), C(Currency), T(Temperature), S(Speed), A(Angles)")



    if convert_type == "L":      #FOR LENGTH CONVERSIONS
        available_units = length.keys()
        val = float(input("Enter Value: "))   # Input Value
        for unit in available_units:
            print(unit)              
        unit_in = input("unit: ")      #Input Unit
        if unit_in in available_units:
            print("convert ", val , unit_in, "to? ")
            for unit in available_units:
                print(unit, end=" ")    #Output Unit
            unit_out = input()
            if unit_out in available_units:
                print("Converting",val,unit_in, "to", unit_out)
                output = convert_l(val,unit_in,unit_out)
                print(val,unit_in,"=",output,unit_out)
            else:
                continue

            
        else:
            print("Unit not acceptable")
