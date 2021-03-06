from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class DayView(models.Model):
    date = models.DateTimeField()
    arti_views = models.PositiveIntegerField(default=0)
    proj_views = models.PositiveIntegerField(default=0)
    o_aViews = models.PositiveIntegerField(default=0)
    o_pViews = models.PositiveIntegerField(default=0)
    running_time = models.PositiveIntegerField(default=0)


class Post(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User)
    pic = models.CharField(max_length=200, default="https://semantic-ui.com/images/wireframe/image.png")
    views = models.PositiveIntegerField(default=0)

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={"pk": self.pk})
#from mongoengine import *
# mongoDB
# class AcUser(Document):
#     isFriend = IntField()
#     posts = IntField()
#     fans = IntField()
#     lastLoginIp = StringField()
#     nextLevelNeed = IntField()
#     regTime = StringField()
#     expPercent = IntField()
#     avatar = StringField()
#     dTime = StringField()
#     currExp = IntField()
#     uid = IntField()
#     stows = IntField()
#     follows = IntField()
#     verified = IntField()
#     comments = IntField()
#     level = IntField()
#     lastLoginDate = StringField()
#     name = StringField()
#     followed = IntField()
#     views = IntField()
#     gender = IntField()
#     verifiedText = StringField()
#     meta = {
#         "collection":"ac_user_info"
#     }
#
# # for i in AcUser.objects[:3]:
# #     print(i.gender)