#!/usr/bin/python3
from Classes import *
creds = Credentials()
method = Methods()

form = cgi.FieldStorage()

file_item = form['filename']

project = method.StablishConnection()
upload_object = method.UploadObject(project,file_item)

