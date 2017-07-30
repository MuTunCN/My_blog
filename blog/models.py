from django.db import models
from mongoengine import *
connect("ac_data")

class AcUser(Document):
    isFriend = IntField()
    posts = IntField()
    fans = IntField()
    lastLoginIp = StringField()
    nextLevelNeed = IntField()
    regTime = StringField()
    expPercent = IntField()
    avatar = StringField()
    dTime = StringField()
    currExp = IntField()
    uid = IntField()
    stows = IntField()
    follows = IntField()
    verified = IntField()
    comments = IntField()
    level = IntField()
    lastLoginDate = StringField()
    name = StringField()
    followed = IntField()
    views = IntField()
    gender = IntField()
    verifiedText = StringField()
    meta = {
        "collection":"user_info"
    }

# for i in AcUser.objects[:3]:
#     print(i.gender)