from pymongo import MongoClient

client = MongoClient()
client = MongoClient("localhost", 27017)

# client = MongoClient('mongodb://localhost:27017/')

db = client['employee_record']  # create database

# db=client.employee_record

employees = db.employees  # create collections or table

# employee = {"id": "103",
# "name": "graham bell",
# "profession": "Mecanical Engineer",
#  }

# rec=employees.insert_one(employee)


# print(db.employees.find({"profession":"Software Engineer"}).count())


# for i in db.employees.find({"id": "103"}):
#  print(i)

# print("First employee is: {}".format(result.inserted_id))
# db.list_collection_names()
#

# insert many employees:
employee = [{"id": "105",
             "name": "abrham",
             "profession": "civil Engineer",
             },
            {"id": "106",
             "name": "abrham",
             "profession": "civil Engineer",
             },

            {"id": "107",
             "name": "johny",
             "profession": "civil Engineer",
             },
            {"id": "108",
             "name": "dawell",
             "profession": "Software Engineer",
             },

            {"id": "110",
             "name": "ureneyu",
             "profession": "Electrical Engineer",
             }]

rec = employees.insert_many(employee)

for i in db.employees.find({}):  # Read a database
    print(i)

x = employees.update_many({"id": "103"}, {"$set": {"name": "abrahamlinlon"}}, upsert=True)

# print("The new article IDs are {}".format(new_articles.inserted_ids))
