from pymango import MongoClient

class mongoDB_management:
    def __init__(self):
       self.client = mangoclient('localhost',27017)
       self.db = self.client('mongoDatabaseDemo')
       self.Collection_Student=self.db('employees')

#insert one data in databse
def insert_one_employee(self):
        self.collection_student.insert_one({
        "name":"utkarsh",
        "age":21,
        "email":"utkarsht724"
        })

#Insert many data in database
def insert_many_employees(self):
        new_employees=self.Collection_student.insert_many(
        [
                { "name":"rakeshasthana",
                  "age": "45",
                "email":"rakeshasgtahan@#gmail.com"} ,

            { "name":"priyankamehrohtra",
            "age":43,
           "email":"priyankamehrotra34@gmail.com",
            }
        ])

#Update the database
def update_a_Student(self):
         self.collection_student.find_one_and_updte(
         {
            "_id":"101.102.103"
         },

         {"$set":{
            'name':"rajeevmehrohtra"
             }}

#Read a file
def find_all_employees(self):
    all_employees=self.collection_student.find({})
    print("Number of records=" +str(all_employees.count())
          for each_student in  all employees.count())):
             print(each_student)

#delete a record
def delete_an_employee(self):
    self.collection_employee.delete_one({'name':'priyankamehrotra'})

mongoDB = mongoDBmanagement()
#mongoDB = insert_one_employee()
mangoDB = insert_many_employee()


