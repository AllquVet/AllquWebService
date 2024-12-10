import streamlit as st
import datetime as dt
from google_calendar import GoogleCalendarManager

calendar = GoogleCalendarManager()

calendar.list_upcoming_events()

una_fecha=st.date_input("Digite la fecha")
hora=dt.timedelta(hours=1)
calendar.list_today_events(fecha=una_fecha)
otrafehca=una_fecha-hora
una_fecha = str(una_fecha)
otrafehca=str(otrafehca)
una_hora=str(st.time_input("Digite hora"))#2024.11.07
st.write(una_fecha+"T"+una_hora+"-05:00")
print(una_fecha)



#


#start_time=datetime.datetime(fecha.year, fecha.month,fecha.day,hours1+1,minutes1).astimezone()
#end_time=datetime.datetime(fecha.year, fecha.month,fecha.day,end_hour+1,end_hour.minute())
#calendar.create_event("Hola youtube","2023-08-08T16:30:00+02:00","2023-08-08T17:30:00+02:00","Europe/Madrid",["antonio@gmail.com","pedro@gmail.com"])