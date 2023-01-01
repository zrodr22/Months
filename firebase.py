import firebase_admin

cred_obj = firebase_admin.credentials.Certificate('fb_pk.json')
databaseURL = ""

default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL':databaseURL
	})

from firebase_admin import db

ref = db.reference("/")
