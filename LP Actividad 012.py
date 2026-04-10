TpCls_frio = 0
TpCls_bueno = 0
TpCls_calor = 0

for i in range(12):
    print("día", i + 1)
    TpCls_dia = float(input("Ingrese la temperatura: "))
    if TpCls_dia < 11.5:
        TpCls_frio = TpCls_frio + 1
    elif TpCls_dia > 11.5 and TpCls_dia < 28.5:
        TpCls_bueno = TpCls_bueno + 1
    else:
        TpCls_calor = TpCls_calor + 1
Porcentaje_frio = (TpCls_frio * 100) / 12
Porcentaje_bueno = (TpCls_bueno * 100) / 12
Porcentaje_calor = (TpCls_calor * 100) / 12
print("El porcentaje de días fríos es de:", Porcentaje_frio, "%")
print("El porcentaje de días buenos es de:", Porcentaje_bueno, "%")
print("El porcentaje de días calurosos es de:", Porcentaje_calor, "%")