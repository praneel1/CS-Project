## Input type of conversion
## Types of COnversions - length, weight, volume, imperial, currency, temperature, speed, angles
## Input VALUE
## Input SI UNIT FOR INPUT
## Input SI UNIT FOR OUTPUT
##SI INPUT / SI OUTPUT

from length import *
from weight import *
from volume import *

while True:
    convert_type = input("Enter type: L(Length), W(Weight), V(Volume), C(Currency), T(Temperature), S(Speed), A(Angles)")



    if convert_type == "L":      #FOR LENGTH CONVERSIONS
        L()
    elif convert_type == "W":
        W()
    elif convert_type == "V":
        V()
    else:
        continue

