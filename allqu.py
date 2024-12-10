import streamlit as st
import datetime as dt

import uuid
from google_calendar import GoogleCalendarManager
from google_sheets import  GoogleSheet

import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv
st.set_page_config(page_title="ALLQ'U Veterinaria",page_icon="🐕",layout="centered")
def main ():
    """Generación de la webapp con streamlit"""
    # Definir título
    left_co, cent_co,last_co = st.columns(3)
    with cent_co:
        with st.container(): 
            st.image(image="images/logotry.jpg",width=196)
    st.title("ALLQ'U Veterinaria")
    # Definir Header/Subheader
    st.header("Av. Manco Capac 175")
    # Definir un Texto
    # st.text("Algún texto a añadir preguntar cris")
    
    #Pestañas
    titulos_pestanas = ['Reservar atención', 'Galería', 'Reseñas','Nosotros']
    pestaña1, pestaña2, pestaña3,pestaña4 = st.tabs(titulos_pestanas)
    with pestaña1:
        st.header("Nombre")
        nombre=st.text_input("Escriba su nombre (obligatorio):")
        st.write("La atención es para:",nombre)
        
        st.header("Correo")
        correo=st.text_input("Escriba su correo (obligatorio):")
        st.write("Su correo es:",correo)
        
        st.header("Celular")
        celular=st.text_input("Digite su celular (obligatorio):")
        st.write("Su celular es:",celular)
        st.subheader("Elija el servicio:")
        # SelectBox
        servicio = st.selectbox("Seleccione", 
                                ["Corte de pelo", "Baño", "Corte y baño", "Consulta"])
        st.write("Opción seleccionada:", servicio)
        # MultiSelect
        st.subheader("Fecha")
        
        calendar=GoogleCalendarManager()
        d = st.date_input("Fecha de ateción",min_value=dt.datetime.now(),max_value=dt.datetime.now()+dt.timedelta(days=8))
        st.write("La fecha seleccionada es:", d)
        #Seleccionar hora comprobar calendar
        st.subheader("Hora")
        #print("Inicio____________")

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
        hora=st.selectbox("Seleccione una hora",horas_service)
        print("Hora")
        print(hora)
        print(horas_service)
        print("#")
        
        #Boton reservar
        reservar=st.button("Reservar")
        if reservar:
            if not nombre or not correo or not celular or not servicio or hora=="":
                st.warning("Debe rellenar los campos requeridos o no hay horarios disponibles para este día")
            else:
                #mandar calendrio 
                aux=['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']
                eventoTitle=servicio
                eventoInicio=str(d)+"T"+hora+":00-05:00"
                if   hora=="10:00":
                    eventoFin=str(d)+"T11:00:00-05:00"
                elif hora=="11:00":
                    eventoFin=str(d)+"T12:00:00-05:00"
                elif hora=="12:00":
                    eventoFin=str(d)+"T13:00:00-05:00"
                elif hora=="13:00":
                    eventoFin=str(d)+"T14:00:00-05:00"
                elif hora=="14:00":
                    eventoFin=str(d)+"T15:00:00-05:00"
                elif hora=="15:00":
                    eventoFin=str(d)+"T16:00:00-05:00"
                elif hora=="16:00":
                    eventoFin=str(d)+"T17:00:00-05:00"
                elif hora=="17:00":
                    eventoFin=str(d)+"T18:00:00-05:00"
                elif hora=="18:00":
                    eventoFin=str(d)+"T19:00:00-05:00"
                elif hora=="19:00":
                    eventoFin=str(d)+"T20:00:00-05:00"
                work=""
                code_event=calendar.create_event(eventoTitle,eventoInicio,eventoFin,"America/Lima",work)
                
                #mandaer bd
                file_name_gs = "sheetsallqu-0cedd2560319.json"
                google_sheet = "AllquReservas"
                sheet_name = "bd_services"


                # --------------------------------------


                def generate_uid():
                    # Generate a UUID
                    unique_id = uuid.uuid4()
                    # Convert the UUID to a string
                    unique_id_str = str(unique_id)
                    return unique_id_str


                #Generate uid
                uid = generate_uid()
                #Init
                google = GoogleSheet(file_name_gs, google_sheet, sheet_name)


                value =[[nombre,correo,celular,servicio,str(d),str(hora),uid]]
                range = google.get_last_row_range()
                google.get_all_values()
                google.write_data(range,value)
                
                #Enviar correo
                load_dotenv()

                my_mail=os.getenv("username")
                yourpassword=os.getenv("gmail_password")
                email_receiver=correo

                subject="Confirmación de reserva para "+servicio
                body="Estmad@ "+nombre+"\nSe confirma la reserva de su atención a las..."

                em=EmailMessage()
                em["From"]=my_mail
                em["To"]=email_receiver
                em["Subject"]=subject
                em.set_content(body)
                with smtplib.SMTP_SSL('smtp.gmail.com',465) as connection:
                    connection.login(user=my_mail,password=yourpassword)
                    connection.sendmail(from_addr=my_mail,
                                        to_addrs=email_receiver,
                                        msg=em.as_string())
                
                st.write("UID event: "+code_event)
                st.success("Su reserva se ha registrado con éxito")
                
                
                                
        
    '''
    with pestaña2:
        st.header('Tema B')
        st.write('Contenido del tema B')
    
    with pestaña3:
        st.header('Tema C')
        st.write('Contenido del tema C')
    with pestaña4:
        st.header('Tema D')
        st.write('Contenido del tema D')
    
    '''
    
if __name__ == "__main__":
    main()
