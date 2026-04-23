import math

cate_oposto = float(input("digite o valor do cateto oposto:"))
cate_adjacente = float(input("digite o valor do cateto adjacente"))

hipotenusa = math.hypot(cate_oposto, cate_adjacente)

print("o valor da hipotenusa vai medir{:.3f}".format(hipotenusa))
