from google_sheets import GoogleSheet
import datetime
import uuid

file_name_gs = "sheetsallqu-ec0eae26d374.json"
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


value =[["Alejandro","test@gamil.com","987654321","Serv",str(datetime.date.today()),str(datetime.datetime.now().time()),uid]]
range = google.get_last_row_range()
google.get_all_values()
google.write_data(range,value)