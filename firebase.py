import firebase_admin

cred_obj = firebase_admin.credentials.Certificate('fb_pk.json')
databaseURL = "https://months-dbe00-default-rtdb.firebaseio.com/"

default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL':databaseURL
	})

from firebase_admin import db

ref = db.reference("/")
