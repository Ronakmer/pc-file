
# python3 manage.py shell


from pos_admin.models import *
from super_admin.models import *



user_details_instance = country.objects.get(id=1) 

states=[
    
  {"country_id":1,"state_name": "Andhra Pradesh","status": "True","created_by": "admin","createDate": " ","updateDate": " " },
  {"country_id":1,"state_name": "Arunachal Pradesh","status": "True","created_by": "admin","createDate": " ","updateDate": " " },
  {"country_id":1,"state_name": "Assam","status": "True","created_by": "admin","createDate": " ","updateDate": " " },
  {"country_id":1,"state_name": "Bihar","status": "True","created_by": "admin","createDate": " ","updateDate": " " },
  {"country_id":1,"state_name": "Chandigarh","status": "True","created_by": "admin","createDate": " ","updateDate": " " },
  {"country_id":1,"state_name": "Chhattisgarh","status": "True","created_by": "admin","createDate": " ","updateDate": " " },
  {"country_id":1,"state_name": "Goa","status": "True","created_by": "admin","createDate": " ","updateDate": " " },
  {"country_id":1,"state_name": "Gujarat","status": "True","created_by": "admin","createDate": " ","updateDate": " " },
  {"country_id":1,"state_name": "Haryana","status": "True","created_by": "admin","createDate": " ","updateDate": " " },
  {"country_id":1,"state_name": "Himachal Pradesh","status": "True","created_by": "admin","createDate": " ","updateDate": " " },
  {"country_id":1,"state_name": "Jammu and Kashmir","status": "True","created_by": "admin","createDate": " ","updateDate": " " },
  {"country_id":1,"state_name": "Jharkhand","status": "True","created_by": "admin","createDate": " ","updateDate": " " },
  {"country_id":1,"state_name": "Karnataka","status": "True","created_by": "admin","createDate": " ","updateDate": " " },
  {"country_id":1,"state_name": "Kerala","status": "True","created_by": "admin","createDate": " ","updateDate": " " },
  {"country_id":1,"state_name": "Madhya Pradesh","status": "True","created_by": "admin","createDate": " ","updateDate": " " },
  {"country_id":1,"state_name": "Maharashtra","status": "True","created_by": "admin","createDate": " ","updateDate": " " },
  {"country_id":1,"state_name": "Manipur","status": "True","created_by": "admin","createDate": " ","updateDate": " " },
  {"country_id":1,"state_name": "Meghalaya","status": "True","created_by": "admin","createDate": " ","updateDate": " " },
  {"country_id":1,"state_name": "Mizoram","status": "True","created_by": "admin","createDate": " ","updateDate": " " },
  {"country_id":1,"state_name": "Nagaland","status": "True","created_by": "admin","createDate": " ","updateDate": " " },
  {"country_id":1,"state_name": "Odisha","status": "True","created_by": "admin","createDate": " ","updateDate": " " },
  {"country_id":1,"state_name": "Puducherry","status": "True","created_by": "admin","createDate": " ","updateDate": " " },
  {"country_id":1,"state_name": "Punjab","status": "True","created_by": "admin","createDate": " ","updateDate": " " },
  {"country_id":1,"state_name": "Rajasthan","status": "True","created_by": "admin","createDate": " ","updateDate": " " },
  {"country_id":1,"state_name": "Tamil Nadu","status": "True","created_by": "admin","createDate": " ","updateDate": " " },
  {"country_id":1,"state_name": "Telangana","status": "True","created_by": "admin","createDate": " ","updateDate": " " },
  {"country_id":1,"state_name": "Tripura","status": "True","created_by": "admin","createDate": " ","updateDate": " " },
  {"country_id":1,"state_name": "Uttar Pradesh","status": "True","created_by": "admin","createDate": " ","updateDate": " " },
  {"country_id":1,"state_name": "Uttarakhand","status": "True","created_by": "admin","createDate": " ","updateDate": " " },
  {"country_id":1,"state_name": "West Bengal","status": "True","created_by": "admin","createDate": " ","updateDate": " " },
  {"country_id":1,"state_name": "Delhi","status": "True","created_by": "admin","createDate": " ","updateDate": " " },
  {"country_id":1,"state_name": "Andaman and Nicobar Islands","status": "True","created_by": "admin","createDate": " ","updateDate": " " },
  {"country_id":1,"state_name": "Dadra and Nagar Haveli and Daman and Diu","status": "True","created_by": "admin","createDate": " ","updateDate": " " },
  {"country_id":1,"state_name": "Ladakh","status": "True","created_by": "admin","createDate": " ","updateDate": " " },
  {"country_id":1,"state_name": "Lakshadweep","status": "True","created_by": "admin","createDate": " ","updateDate": " " },


  



]

for data in states:
    state.objects.create(
        country_id=user_details_instance,
        state_name=data["state_name"],
        createDate=timezone.now(),
        updateDate=timezone.now(),
        created_by=data["created_by"]
    )










