import datetime as dt
from google_calendar import GoogleCalendarManager
import streamlit as st
calendar=GoogleCalendarManager()
d = st.date_input("When's your birthday",min_value=dt.datetime.now(),max_value=dt.datetime.now()+dt.timedelta(days=8))
st.write("Your birthday is:", d)
print("Inicio____________")

hora_actual=str(dt.datetime.now().time().replace(minute=0,second=0,microsecond=0))[0:5]
horas_service=["10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00","18:00","19:00"]
if d==dt.datetime.now().date():
    start_day=(str(d)+"T"+str(((dt.datetime.now().time()).replace(second=0,microsecond=0))))+"-05:00"
    end_day = str(d)+"T23:59:00"+ "-07:00"
    
    if hora_actual=="10:00":
        horas_service=["11:00","12:00","13:00","14:00","15:00","16:00","17:00","18:00","19:00"]
    elif hora_actual=="11:00":
        horas_service=["12:00","13:00","14:00","15:00","16:00","17:00","18:00","19:00"]
        
    elif hora_actual=="12:00":
        horas_service=["13:00","14:00","15:00","16:00","17:00","18:00","19:00"]
        
    elif hora_actual=="13:00":
        horas_service=["14:00","15:00","16:00","17:00","18:00","19:00"]
        
    elif hora_actual=="14:00":
        horas_service=["15:00","16:00","17:00","18:00","19:00"]
        
    elif hora_actual=="15:00":
        horas_service=["16:00","17:00","18:00","19:00"]
        
    elif hora_actual=="16:00":
        horas_service=["17:00","18:00","19:00"]
        
    elif hora_actual=="17:00":
        horas_service=["18:00","19:00"]
        
    elif hora_actual=="18:00":
        horas_service=["19:00"]
    else:
        horas_service=[""]
        
    
else:
    start_day=(str(d)+"T"+str(((dt.datetime.now().time()).replace(hour=8,minute=0,second=0,microsecond=0))))+"-05:00"
    end_day = str(d)+"T23:59:00"+ "-07:00"
#start_day = dt.datetime.utcnow().isoformat() + "-07:00"
#start_day="2024-11-13T08:00:00Z"
#end_day=  "2024-11-13T23:59:00Z"

lista_eventos_hoy=()
print("---------------")
print(start_day)
print(end_day)
print("---------------")
print("###")

lista_horas=[]
lista_eventos_hoy=calendar.list_today_events(Start_day=start_day,End_day=end_day)
for tarea in lista_eventos_hoy:
    start = tarea['start'].get('dateTime', tarea['start'].get('date'))
    lista_horas.append(start[11:16])
    print(start[11:16])
print(hora_actual)
print(lista_horas)
for e in lista_horas:
    if e in horas_service:
        horas_service.remove(e)
st.selectbox("Seleccione una hora",horas_service)
print(horas_service)
print("#")



