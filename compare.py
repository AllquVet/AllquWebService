import datetime as dt


fecha_hoy=dt.datetime.now().date()

fecha_hoy_to=(dt.datetime.now()+dt.timedelta(days=1)).date()


print(dt.datetime.utcnow().isoformat() + "Z")
print(fecha_hoy)
print(fecha_hoy_to)


lot=fecha_hoy_to
if lot<=fecha_hoy:
    print("Es hoy")
else:
    print("Es mañana")