from models import *

db.connect()
db.create_table(UserStories, safe= True)