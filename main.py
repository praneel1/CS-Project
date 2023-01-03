## Input type of conversion
## Types of COnversions - length, weight, volume, imperial, currency, temperature, speed, angles
## Input VALUE
## Input SI UNIT FOR INPUT
## Input SI UNIT FOR OUTPUT
##SI INPUT / SI OUTPUT

from length import *

while True:
    convert_type = input("Enter type: L(Length), W(Weight), V(Volume), C(Currency), T(Temperature), S(Speed), A(Angles)")



    if convert_type == "L":
        val = float(input("Enter Value: "))
        for unit in length.keys():
            print(unit)
        unit_in = input("unit: ")
        if unit_in in length.keys:
            print("convert ", val , unit_in, "to? ")
        else:
            print("Unit not acceptable")
