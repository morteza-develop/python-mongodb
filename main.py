import pymongo


####################### insert
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]

# mylist = [
#   { "name": "morteza", "address": "Apple st 652"},
# ]

# x = mycol.insert_many(mylist)

# #print list of the _id values of the inserted documents:

# print(x.inserted_ids)

########################### find
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]

# myquery = { "name": "morteza" }

# mydoc = mycol.find(myquery)

# for x in mydoc:
#   print(x)

########################### sort
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]

# mydoc = mycol.find().sort("name")

# for x in mydoc:
#   print(x)

########################### update
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "name": "morteza" }
newvalues = { "$set": { "address": "mashhad" } }

mycol.update_one(myquery, newvalues)

#print "customers" after the update:
for x in mycol.find():
  print(x)