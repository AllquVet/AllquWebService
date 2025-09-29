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
st.html('<meta name="google-site-verification" content="umm5S2Dr_JonwHyVpBjIeSwtNc24DAtiT36ewj9HUms" />')
def main ():
    # Definir título
    left_co, cent_co,last_co = st.columns(3)
    with cent_co:
        with st.container(): 
            st.image(image="images/logotry.jpg",width=196)
    st.header("ALLQ'U Consultorio Veterinario")
    # Definir un Texto
    st.text('"'+"Cuidamos a tu mascota con amor y ciencia"+'"')
    # Definir Header/Subheader
    url_to_wsp = "https://wa.link/wc5vh4"
    st.markdown("Contacto: [959403782](%s)"%url_to_wsp)
    st.text("Av. Manco Capac 175-Los Baños del Inca")
    
    
    #Pestañas
    titulos_pestanas = ['Reservar atención', 'Galería','Nosotros']
    pestaña1, pestaña2, pestaña3 = st.tabs(titulos_pestanas)
    with pestaña1:
        st.subheader("¿Cómo se llama su mascota?")
        mascota=st.text_input("Nombre mascota (obligatorio):")
        st.write("La atención es para:",mascota)
        st.subheader("¿Cuál es tu nombre completo?")
        nombre=st.text_input("Nombre (obligatorio):")
        st.write("La atención es para:",nombre)
        st.subheader("¿Cuál es su numero de celular para contactarlo?")
        celular=st.text_input("Celular (obligatorio):")
        st.write("Su celular es:",celular)
        correo_check=st.checkbox("¿Desea agregar un correo?")
        if  correo_check:
            st.subheader("Por pavor escriba su correo")
            correo=st.text_input("Escriba su correo:")
            st.write("Su correo es:",correo)
        st.subheader("¿Qué servicio está requiriendo para su mascota?:")
        # SelectBox
        servicio = st.selectbox("Seleccione:", 
                                [
                                    "Baño medicado (S/. 10.00*)",
                                    "Baño simple razas pequeñas(S/. 25.00*)" ,
                                    "Baño simple razas medianas(S/. 35.00*)" ,
                                    "Baño simple razas grandes(S/. 50.00*)",
                                    "Baño y corte razas pequeñas(S/. 35.00*)",
                                    "Baño y corte razas medianas(S/. 45.00*)", 
                                    "Baño y corte razas grandes(S/. 70.00*)",
                                    "Baño gatos (S/. 30.00*)",
                                    "Reserva baño (S/. 10.00*)",
                                    "Reserva baño y corte (S/. 25.00*)",
                                    "Consulta"],index=None)
        #st.write("Opción seleccionada:", servicio)
        st.write("*El precio puede variar dependiendo del estado en el que se encuentre su mascota")
        motivo_consulta=""
        if servicio=="Consulta":
            
            motivo_consulta=st.text_input("Por favor indique el motivo de la consulta")
        
        #Transporte service
        if servicio!=None:
            bttransporte=st.checkbox("¿Desea agregar el servicio de transporte de mascota? (Tarifa adicional dependiendo de la distancia)")
            if bttransporte:
                transporte=st.selectbox("Seleccione la opción mas conveniente",
                                        ["Recojo de mascota",
                                        "Entrega de mascota",
                                        "Recojo y entrega de mascota"
                                        ])
            else:
                transporte=""
        # MultiSelect
        st.subheader("Qué fecha desea su reserva")
        
        calendar=GoogleCalendarManager()
        hora_global=dt.datetime.now(dt.UTC)
        hora_peru=(hora_global-dt.timedelta(hours=5))
        fecha_actual=dt.datetime.now(dt.UTC)
        fecha_actual_peru=fecha_actual-dt.timedelta(hours=5)
        d = st.date_input("Fecha:",value=fecha_actual_peru,min_value=fecha_actual_peru,max_value=fecha_actual_peru+dt.timedelta(days=8),format="DD/MM/YYYY")
        #st.write("La fecha seleccionada es:", d)
        #Seleccionar hora comprobar calendar
        st.subheader("¿A qué hora desea su reserva")
        #print("Inicio____________")
        print(d)
        

        hora_actual=str(hora_peru.time().replace(minute=0,second=0,microsecond=0))[0:5]
        horas_service=["10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00","18:00"]
        print(fecha_actual)
        print(fecha_actual_peru)
        if d==fecha_actual_peru.date():
            start_day=(str(d)+"T"+str(((fecha_actual_peru.time()).replace(second=0,microsecond=0))))+"-05:00"
            end_day = str(d)+"T23:59:00"+ "-05:00"
            
            if hora_actual=="10:00":
                horas_service=["11:00","12:00","13:00","14:00","15:00","16:00","17:00","18:00"]
            elif hora_actual=="11:00":
                horas_service=["12:00","13:00","14:00","15:00","16:00","17:00","18:00"]
                
            elif hora_actual=="12:00":
                horas_service=["13:00","14:00","15:00","16:00","17:00","18:00"]
                
            elif hora_actual=="13:00":
                horas_service=["14:00","15:00","16:00","17:00","18:00"]
                
            elif hora_actual=="14:00":
                horas_service=["15:00","16:00","17:00","18:00"]
                
            elif hora_actual=="15:00":
                horas_service=["16:00","17:00","18:00"]
                
            elif hora_actual=="16:00":
                horas_service=["17:00","18:00"]
                
            elif hora_actual=="17:00":
                horas_service=["18:00"]
                
            elif hora_actual=="18:00":
                horas_service=[]
            elif hora_actual=="19:00":
                horas_service=[]
            elif hora_actual=="20:00":
                horas_service=[]
            elif hora_actual=="21:00":
                horas_service=[]
            elif hora_actual=="22:00":
                horas_service=[]
            elif hora_actual=="23:00":
                horas_service=[]
            
        else:
            start_day=(str(d)+"T"+str(((fecha_actual.time()).replace(hour=8,minute=0,second=0,microsecond=0))))+"-05:00"
            end_day = str(d)+"T23:59:00"+ "-05:00"
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
        #convertir formato horas
        
        dic_horas1={    '10:00': '10:00 a.m.',
                        '11:00': '11:00 a.m.',
                        '12:00': '12:00 a.m.',
                        '13:00': '1:00 p.m.',
                        '14:00': '2:00 p.m.',
                        '15:00': '3:00 p.m.',
                        '16:00': '4:00 p.m.',
                        '17:00': '5:00 p.m.',
                        '18:00': '6:00 p.m.'}
        horas_service_format=[]
        for q in horas_service:
            horas_service_format.append(dic_horas1.get(q))
        print(horas_service_format)
        hora_aux=st.selectbox("Seleccione una hora:",horas_service_format)
        formato_horas={ '10:00 a.m.': '10:00',
                        '11:00 a.m.': '11:00',
                        '12:00 a.m.': '12:00',
                        '13:00 p.m.': '13:00',
                        '14:00 p.m.': '14:00',
                        '15:00 p.m.': '15:00',
                        '16:00 p.m.': '16:00',
                        '17:00 p.m.': '17:00',
                        '18:00 p.m.': '18:00'}
        hora=formato_horas.get(hora_aux)
        print("Hora")
        print(hora)
        print(horas_service)
        print("FIN")
        
        #Boton reservar
        if not nombre or not correo or not celular or not servicio or hora=="":
                st.warning("Debe rellenar los campos requeridos o no hay horarios disponibles para este día")
        else:
            reservar=st.button("Reservar")
            if reservar:
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


                value =[[mascota,nombre,correo,celular,servicio,str(d),str(hora),str(motivo_consulta),transporte,uid]]
                range = google.get_last_row_range()
                google.get_all_values()
                google.write_data(range,value)
                
                #Enviar correo
                load_dotenv()

                my_mail=os.getenv("username")
                yourpassword=os.getenv("gmail_password")
                if correo!=None:
                    email_receiver=correo
                    #Correo cliente

                    subject="Confirmación de reserva para "+servicio
                    body="Estmad@ "+nombre+"\n\nNos complace informarle que su reserva para el sercicio de "+ servicio +" de su mascota ha sido confirmada."+"\n\nDetalles de la reserva:"+f"\n-Servicio: {servicio}"+f"\n-Fecha: {d}"+f"\n-Hora {hora}"+"\n-Ubicación: Av Manco Capac 175, Los Baños del Inca"+"\n\nPor favor, asegúrese de llegar 10 minutos antes de la hora programada y traiga los documentos o accesorios necesarios (cartilla de vacunación, correa, etc., según aplique).\n\nSi tiene alguna pregunta o necesita modificar la cita, no dude en contactarnos al 959403782 o responder a este correo.\n\n¡Gracias por confiar en nosotros para cuidar de"+ mascota+"!\n\nAtentamente\nAllq'u Pet Barber Shop"
                    
                    

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
                
                subject_to_aq="Reenvío de reservación de cita->"+servicio
                body_to_aq="Estmad@ "+nombre+"\n\nNos complace informarle que su reserva para el sercicio de "+ servicio +" de su mascota ha sido confirmada."+"\n\nDetalles de la reserva:"+f"\n-Servicio: {servicio}"+f"\n-Fecha: {d}"+f"\n-Hora {hora}"+"\n-Ubicación: Av Manco Capac 175, Los Baños del Inca"+"\n\nPor favor, asegúrese de llegar 10 minutos antes de la hora programada y traiga los documentos o accesorios necesarios (cartilla de vacunación, correa, etc., según aplique).\n\nSi tiene alguna pregunta o necesita modificar la cita, no dude en contactarnos al 959403782 o responder a este correo.\n\n¡Gracias por confiar en nosotros para cuidar de"+ mascota+"!\n\nAtentamente\nAllq'u Consultorio Veterinario"
                    
                em=EmailMessage()
                em["From"]=my_mail
                em["To"]=my_mail
                em["Subject"]=subject_to_aq
                em.set_content(body_to_aq)
                with smtplib.SMTP_SSL('smtp.gmail.com',465) as connection:
                    connection.login(user=my_mail,password=yourpassword)
                    connection.sendmail(from_addr=my_mail,
                                            to_addrs=my_mail,
                                            msg=em.as_string())
                
                #st.write("UID event: "+code_event)
                st.success("Su reserva se ha registrado con éxito")
                
                
                                
        
    
    with pestaña2:
        st.header('Nuestros clientes')
        st.image("images/img1.jpeg")
        st.image("images/img2.jpeg")
        st.image("images/img3.jpeg")
        st.image("images/img4.jpeg")
        
    
    with pestaña3:        
        st.write("Consultorio Veterinario Allq'u – Baños del Inca, Cajamarca\nEn Allq'u, nos dedicamos al bienestar de tu mascota con un enfoque profesional y humano. Bajo la dirección del Dr. Cristian Bazán Nureña, ofrecemos atención veterinaria de calidad con un trato cálido y personalizado.")
        st.write('✨ "Cuidamos tu mascota con amor y ciencia." ✨')
    
    
if __name__ == "__main__":
    main()


