'''import json
employee={    
    "employee_details":[
        {
         "Name": "bikash",
         "DOB": "13.06.2003",
         "Height": "5.3",
         "City": "Visakhapatnam",
         "State": "andhrapradesh"
        },
       {
         "Name": "anuj",
         "DOB": "04.07.1993",
         "Height": "5.7",
         "City": "hydrabad",
         "State": "telengana"
      },
      {
         "Name": "Ankush",
         "DOB": "01.02.2021",
         "Height": "5.2",
         "City": "noida",
         "State": "delhi"
       },
       {
         "Name": "raju",
         "DOB": "05.12.2009",
         "Height": "5.8",
         "City": "ranchi",
         "State": "jharkhand"
       },
       {
         "Name": "Ganesh",
         "DOB": "22.09.1997",
         "Height": "5.6",
         "City": "cuttack",
         "State": "Odisha"
       }]
}
with open("employee.json","w") as outfile:
    json.dump(employee,outfile,indent=2)
f = open('employee.json', "r")
data = json.loads(f.read())
for i in data["employee_details"]:
    print(i)
f.close()'''

#------------------------------------Task2-----------------------------------------------------------------
# Create a dictionary of any 7 Indian states and their capitals. Write this into a JSON file.
import json

indian_states_capitals = {
    "Andhra Pradesh": "Visakhapatnam",
    "Arunachal Pradesh": "Itanagar",
    "Assam": "Dispur",
    "Bihar": "Patna",
    "Chhattisgarh": "Raipur",
    "Goa": "Panaji",
    "Gujarat": "Gandhinagar"
}

with open('indian_states_capitals.json', 'w') as json_file:
    json.dump(indian_states_capitals,json_file,indent=4)
print("File is Generated")