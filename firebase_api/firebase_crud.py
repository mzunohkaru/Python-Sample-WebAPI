import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import datetime

cred = credentials.Certificate("./serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

users_ref = db.collection("users")
docs = users_ref.stream()


############################# READ

users = []

for doc in docs:
    users.append(doc.to_dict())

    # print(f"{doc.id} => {doc.to_dict()}")
    # 結果 : JwyUnXZg4tIpCk8EL6Ae => {'age': 23,
    #                          'birthday': DatetimeWithNanoseconds(2001, 1, 7, 4, 35, 36, 619000,tzinfo=datetime.timezone.utc),
    #                          'sns': {'followers': 1000, 'following': 1600},
    #                          'location': <google.cloud.firestore_v1._helpers.GeoPoint object at 0x109ffea10>,
    #                          'username': 'hikaru'}

firstUser = users[0]

age = firstUser["age"]

birthday = firstUser["birthday"]

sns = firstUser["sns"]
followers = sns["followers"]
following = sns["following"]

location = firstUser["location"]
latitude = location.latitude
longitude = location.longitude

username = firstUser["username"]

print(username)
print(age)
print(birthday)
print(f"Followers: {followers}, Following: {following}")
print(f"Latitude: {latitude}, Longitude: {longitude}")


############################# CREATE

# パターン 1
doc_ref = db.collection("users").document()
doc_ref.set({
    "age": 30,
    "birthday": datetime.datetime(1991, 1, 1),
    "sns": {
        "followers": 0,
        "following": 0
    },
    "location": firestore.GeoPoint(38.6593, 137.7006),
    "username": "Ado"
})

# パターン 2
doc_ref = db.collection("users").add(
    {
        "age": 30,
        "birthday": datetime.datetime(1991, 1, 1),
        "sns": {"followers": 0, "following": 0},
        "location": firestore.GeoPoint(38.6593, 137.7006),
        "username": "Ado",
    }
)


############################# UPDATE

user_ref = db.collection("users").document("RbyKk6VaZtgDlGsVTwYJ")
user_ref.update({"age": 117, "birthday": datetime.datetime(1815, 8, 22)})


############################# DELETE

# フィールド削除
user_ref = db.collection("users").document("UIKkUnEpVG11uT3gjTTx")
user_ref.update({"location": firestore.DELETE_FIELD})

# ドキュメント削除
user_ref = db.collection("users").document("UIKkUnEpVG11uT3gjTTx").delete()