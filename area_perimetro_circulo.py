import math

# input 
r = input("Ingrese el radio del circulo:")
r = int(r)

# processing
a = math.pi * r**2
p = 2 * math.pi * r

# output
print("el área es: " + str(a))
print("el área perimetro es: " + str(p))
