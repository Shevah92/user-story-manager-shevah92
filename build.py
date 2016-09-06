from models import *

db.connect()
db.drop_table(UserStories)
db.create_table(UserStories, safe= True)