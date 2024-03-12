

# add-role
# show-role
# delete-role
# update-role

# add-course
# show-course
# delete-course
# update-course

# add-student
# show-student
# delete-student
# update-student

# add-fee
# show-fee
# delete-fee
# update-fee

# add-holiday
# show-holiday
# delete-holiday
# update-holiday

# add-staff
# show-staff
# delete-staff
# update-staff

# add-permission
# show-permission
# delete-permission
# update-permission

# show-report-list
# show-fee-receipt
# show-fee-report


################################################

# python3 manage.py shell



from homeApp.models import *


permissions_data = [
    {"name": "add-role"},
    {"name": "show-role"},
    {"name": "delete-role"},
    {"name": "update-role"},
    {"name": "add-course"},
    {"name": "show-course"},
    {"name": "delete-course"},
    {"name": "update-course"},
    {"name": "add-student"},
    {"name": "show-student"},
    {"name": "delete-student"},
    {"name": "update-student"},
    {"name": "add-fee"},
    {"name": "show-fee"},
    {"name": "delete-fee"},
    {"name": "update-fee"},
    {"name": "add-holiday"},
    {"name": "show-holiday"},
    {"name": "delete-holiday"},
    {"name": "update-holiday"},
    {"name": "add-staff"},
    {"name": "show-staff"},
    {"name": "delete-staff"},
    {"name": "update-staff"},
    {"name": "add-permission"},
    {"name": "show-permission"},
    {"name": "delete-permission"},
    {"name": "update-permission"},
    {"name": "show-report-list"},
    {"name": "show-fee-receipt"},
    {"name": "show-fee-report"},
]


for data in permissions_data:
    permission.objects.create(
        permission_name=data["name"],
        createDate=timezone.now(),
        updateDate=timezone.now(),
    )