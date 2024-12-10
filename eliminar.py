from google_calendar import GoogleCalendarManager

#=rm0tmnmn91jsfkvl7e495ini9s
calender_delete=GoogleCalendarManager()
lista_eventos=calender_delete.list_upcoming_events()
#print(lista_eventos)
eventId=("0kb044du7dp2pjspmr6o3nuvrr")
calender_delete.delete_event(eventId)