import re

romanos = input('Escriba un número romano')
validar = 'true'

pattern = r"^(?=[MDCLXVI])(M{0,3})(C[DM]|D?C{0,3})(X[LC]|L?X{0,3})(I[XV]|V?I{0,3})$"

if re.match(pattern, romanos):

    print(validar)

else:

    validar = 'false'
    print(validar)
