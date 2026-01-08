from datetime import date, time, datetime, timedelta

# Fecha actual
hoy = date.today()
print("Fecha actual:", hoy)

# Crear una fecha específica. Tiene que estar totalmente especificada
mi_fecha = date(2025, 1, 3)
print("Fecha específica:", mi_fecha)

# Crear un tiempo específico. No tiene que estar especificado completamente
mi_hora = time(14, 30, 45)
print("Hora específica:", mi_hora)
mi_hora = time(14)
print("Hora específica:", mi_hora)

#no existe un time.now()
# hora_actual = time.now()

# pero si un Fecha y hora actual
ahora = datetime.now()
print("Fecha y hora actual:", ahora)

# Crear una fecha y hora específicas. No tiene que estar especificada completamente
especifico = datetime(2025, 1, 3, 14, 30)
print("Fecha y hora específicas:", especifico)
especifico = datetime(2025, 1, 3)
print("Fecha y hora específicas:", especifico)

# formatear una fecha
# todos los valores numéricos con un - delante eliminan el padding de ceros a la izquierda
formateado = ahora.strftime("%a %d-%-m-%y (%j) %H:%M")
print("Fecha y hora formateadas 1:", formateado)
# la diferencia entre U y W es que con el primero se empieza a contabilizar las semana con el domingo como primer día
# y en W es el lunes
# w es el número del día de la semana. empieza siempre por domingo que es el 0
formateado = ahora.strftime("%A(%w) %-d-%b-%-y (%U) %H:%M")
print("Fecha y hora formateadas 2:", formateado)
formateado = ahora.strftime("%A %-d-%b-%-y (%W) %H:%M")
print("Fecha y hora formateadas 3:", formateado)
formateado = ahora.strftime("%d-%B-%Y %H:%M")
print("Fecha y hora formateadas 4:", formateado)
formateado = ahora.strftime("%d-%B-%Y %-H:%-M")
print("Fecha y hora formateadas 5:", formateado)
# I para horas en formato 12
formateado = ahora.strftime("%d-%B-%Y %I:%M:%S")
print("Fecha y hora formateadas 6:", formateado)
# p es am/pm.
formateado = ahora.strftime("%d-%B-%Y %-I:%M:%-S %p")
print("Fecha y hora formateadas 7:", formateado)

# formatos compactos usando la información de locale
formateado = ahora.strftime("%c")
print("Fecha y hora con locale:", formateado)
formateado = ahora.strftime("%x")
print("Fecha con locale:", formateado)
formateado = ahora.strftime("%X")
print("Hora con locale:", formateado)

# convertir cadena en objeto de fecha
cadena = "2025-01-03 14:30:00"
formato = "%Y-%m-%d %H:%M:%S"
objeto_datetime = datetime.strptime(cadena, formato)
print("Objeto datetime:", objeto_datetime)

# podemos obtener individualmente los elementos: day, month, year, hour, minute, second...
print(objeto_datetime.year)

# el objeto timedelta me permite hacer operaciones sencillas con fechas
hoy = datetime.now()
haceTiempo = hoy - timedelta(days=7, hours=5, weeks=3)
print("Hace tiempo:", haceTiempo)

# Y compararmos como con cualquier otro dato
if haceTiempo < hoy:
    print(haceTiempo, "es anterior a", hoy)


