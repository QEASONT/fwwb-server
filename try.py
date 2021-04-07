import uuid
import os
uid = str(uuid.uuid4())
suid = ''.join(uid.split('-'))
file_path  = os.path.dirname(__file__)
os.mkdir(file_path+'/'+suid[0:5])
if os.path.exists(suid[0:5]):
    print(111)