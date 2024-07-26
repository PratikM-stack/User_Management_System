from google.cloud import firestore
import json

credentials_path="./setup/userinfoapp-fe9f2-firebase-adminsdk-feoi6-9144201b7e.json"
with open(credentials_path) as json_file:
    credentials_info = json.load(json_file)
db = firestore.Client.from_service_account_info(credentials_info)