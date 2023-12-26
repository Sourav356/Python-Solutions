print("Please choose between pounds and kg")
n = float(input("Enter the number of the unit you have with decimal value: "))
from_unit = input("Enter the base unit: ")
to_unit = input("Enter the unit you want to convert: ")

if (from_unit.lower() == 'kg' or from_unit.lower() == 'kilo' or from_unit.lower() == 'kilograms') and (to_unit.lower() == 'pounds' or to_unit.lower() == 'lb' or to_unit.lower() == 'pounds'):
    unit_convert = n * 2.205
    print(f"After converting {n} {from_unit} to {to_unit}, the result is: {unit_convert:.2f} lb")
    
elif (from_unit.lower() == 'pounds' or from_unit.lower() == 'lb' or from_unit.lower() == 'pounds') and (to_unit.lower() == 'kg' or to_unit.lower() == 'kilo' or to_unit.lower() == 'kilograms'):
    unit_converted = n / 2.205
    print(f"After converting {n} {from_unit} to {to_unit}, the result is: {unit_converted:.2f} kg")

else:
    print("Not found or conversion not supported")
