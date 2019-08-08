from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

#MongoDB에 insert 하기

# 'users'라는 collection에 {'name':'bobby','age':21}를 넣습니다.
# db.users.insert_one({'name' : 'bobby', 'age': 21})
# db.users.insert_one({'name' : 'kay', 'age': 27})
# db.users.insert_one({'name' : 'john', 'age': 30})

#MongoDB에서 데이터 모두 보기
all_users = db.users.find()

print(all_users[0])
print(all_users[0]['name'])

for user in all_users:
    print(user)

user = db.users.find_one({'name':'bobby'})
print (user)

# 그 중 특정 키 값을 빼고 보기
user = db.users.find_one({'name':'bobby'},{'_id':0})
print (user)

db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

user = db.users.find_one({'name':'bobby'})
print (user)