import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import os
from datetime import datetime

class GoogleFireBase:
    
    @staticmethod
    def delete_collection(coll_ref, batch_size):
        docs = coll_ref.limit(batch_size).stream()
        deleted = 0

        for doc in docs:
            # print(f'Deleting doc {doc.id} => {doc.to_dict()}')
            doc.reference.delete()
            deleted = deleted + 1

        if deleted >= batch_size:
            return GoogleFireBase.delete_collection(coll_ref, batch_size)

    @staticmethod
    def initialize_firestore():
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "CS246 Scheduler-834a5324ec7b.json"

        # Use the application default credentials
        cred = credentials.ApplicationDefault()
        firebase_admin.initialize_app(cred, {
        'projectId': 'cs246-scheduler',
        })

        db = firestore.client()

        return db

    @staticmethod
    def set_employee(db, employee):
        db.collection("employee").document(employee.name).set(employee.__dict__)

    @staticmethod
    def set_punchIn(db, pi, emp):
        db.collection("employee").document(emp.name).collection("punchInOut").document().set(pi.__dict__)

    @staticmethod
    def get_last_punchIn(db, emp):
        query = db.collection("employee").document(emp.name).collection("punchInOut").where("clockedOutAt", "==", None)
        result = query.get()[0]
        db.collection("employee").document(emp.name).collection("punchInOut").document(result.id).update({"clockedOutAt" : datetime.now()})
        
    @staticmethod
    def delet_account(db, emp):
        GoogleFireBase.delete_collection(db.collection("employee").document(emp.name).collection("punchInOut"), 5)
        db.collection("employee").document(emp.name).delete()




    @staticmethod
    def find_player(db, employee):

        result = db.collection("employee").document(employee.name).get()
        if result.exists:
            location = result.to_dict()
            return location
        else:
            return None

