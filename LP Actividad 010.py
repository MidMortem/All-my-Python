TpCls = 0
for i in range(12):
    print("día", i + 1)
    TpCls_dia = float(input("Ingrese la temperatura: "))
    TpCls = TpCls + TpCls_dia
TpCls_promedio = TpCls / 12
if TpCls_promedio < 11.5 or TpCls_promedio > 28.5:
    print("MAL CLIMA")
else:
    print("BUEN CLIMA")