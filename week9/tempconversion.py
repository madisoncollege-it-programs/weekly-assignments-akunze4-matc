#!/usr/bin/env python3
#Purpose: Importing conversion functions

import c2f
import f2c

inputVarFormat = (input("(1)Fahrenheit to Celsius?\n\
(2)Celsius to Fahrenheit?\n→ "))

if inputVarFormat == "1":
    inputVar = float(input("Starting Temperature F°\n→ "))
    print(f"Converted to C° {f2c.F2C(inputVar):^.1f}")
elif inputVarFormat == "2":
    inputVar = float(input("Starting Temperature C°\n→ "))
    print(f"Converted to F° {c2f.C2F(inputVar):^.1f}")
