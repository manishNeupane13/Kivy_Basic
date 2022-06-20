

import pyrebase

def configure():
    firebaseConfig = {'apiKey': "AIzaSyA2MSOdXR_eL120E70fBV1IDHYzEzcwdVk",
                  'authDomain': "bus-tracking-9720b.firebaseapp.com",
                  'databaseURL': "https://bus-tracking-9720b-default-rtdb.asia-southeast1.firebasedatabase.app",
                  'projectId': "bus-tracking-9720b",
                  'storageBucket': "bus-tracking-9720b.appspot.com",
                  'messagingSenderId': "309426687559",
                  'appId': "1:309426687559:web:11a08c6e5d8aa28032ab62",
                  'measurementId': "G-FCQ26QWTSW"
                  }

    firebase = pyrebase.initialize_app(firebaseConfig)
    return firebase.database()
database=configure()
def create_db(location_name,route_name,bus_stops):
    database.child("Bus Route List").child(location_name).child(route_name).set(bus_stops)
def fetch_db(location_name,route_name):
    return database.child("Bus Route List").child(location_name).child(route_name).get()
def update_db(location_name,route_name,bus_stops):
    database.child("Bus Route List").child(location_name).child(route_name).update(bus_stops)
def delete_db(location_name,route_name,bus_stop):
    return database.child("Bus Route List").child(location_name).child(route_name).child(bus_stop).remove()


# total_number_of_bus_stand=int(input("Enter the total number of bus stand in that route :: "))
# location_name=input("Enter the Location name :: ")
# route_name=input("Enter the name of the route :: ")
# bus_stand_dict={}
# for i in range(1,total_number_of_bus_stand+1):
#     bus_stand_name=input(f'Enter the name of Bus stand [{i}] :: ')
#     bus_stand_dict[f'Bus Stop {i}']=bus_stand_name

# real_time_db=configure()
# print(bus_stand_dict)
# create_db(location_name,route_name,bus_stand_dict)
# # data_list = fetch_db(real_time_db, location_name,route_name)
# # for task in data_list.each():
# #     print(task.key(),task.val())
# delete_db(real_time_db,location_name,route_name,bus_stop="Bus Stop 3")
