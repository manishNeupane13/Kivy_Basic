import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Setup
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

database = firestore.client()
def create_firestore_db(collection_name,document_name,field_dict):
    database.collection(f'{collection_name} Bus Route List').document(
        document_name).set(field_dict, merge=True)
def fetech_firestore_db(collection_name):
    print(f'{collection_name} Bus Route List')
    return database.collection(f'{collection_name} Bus Route List').get()
    # database_result = database.collection(f'{collection_name}Bus Route List').get()
    # return database.collection(f'{collection_name}Bus Route List').get()


def fetech_firestore_doc_db(collection_name,field_name):
    print(f'{collection_name} Bus Route List')
    return database.collection(f'{collection_name} Bus Route List').document(field_name).get()
def update_firestore_db(collection_name, document_name, field_dict):
        database.collection(f'{collection_name} Bus Route List').document(
        document_name).update(field_dict)
   


def delete_firestore_db(collection_name, document_name,field_name):
    def delete_field():
        database.collection(f'{collection_name} Bus Route List').document(
            document_name).update(field_name,firestore.DELETE_FIELD)

    def delete_document():
        database.collection(collection_name).document(document_name).delete()
        

# result1 = fetech_firestore_db("Kathmandu")
# result = fetech_firestore_doc_db("Kathmandu", "Godawari-Machhapokhari")
# print("resutl=", result)
# if result.exists:
#     print(result.to_dict())
# for x in result1:
#     print(x.id == "Kalanki-TIA ")

