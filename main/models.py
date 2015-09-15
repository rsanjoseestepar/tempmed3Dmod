from django.db import models
from django.contrib.auth.models import User

# Create your models here.



def upload_to(instance, filename):
    return instance.get_upload_path(filename)

class Organ(models.Model):
    organ = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    def __unicode__(self):
        return self

class BodyPart(models.Model):
    body_part = models.CharField(max_length=20)
    organ = models.ManyToManyField(Organ)
    def __unicode__(self):
        return self

class ImgContainer(models.Model):
    user = models.ForeignKey(User)
    tentative_body_part = models.ManyToManyField(BodyPart, default='0')
    tentative_img_type = models.CharField(max_length=10, default='0')
    active = models.BooleanField(default = True)
    created = models.DateTimeField(auto_now_add=True)
    deleted = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to = upload_to, default = 'no_file')
    def __str__(self):
        return self
    def get_upload_path(self,filename):
        return str(self.user.id) + "/medimg/" + filename




class MedImg(models.Model):
    user = models.ForeignKey(User)
    body_part = models.ManyToManyField(BodyPart)
    file = models.FileField(upload_to = upload_to, default = 'no_file')
    img_type = models.CharField(max_length=10)
    active = models.BooleanField(default = True)
    created = models.DateTimeField(auto_now_add=True)
    deleted = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return self
    def get_upload_path(self,filename):
        return str(self.user.id) + "/medimg/" + str(self.img_type) + filename



class Model(models.Model):
    user = models.ForeignKey(User)
    medimg = models.ForeignKey(MedImg, default='0')
    organ = models.ForeignKey(Organ, default='0')
    name = models.CharField(max_length=100)
    model_file = models.FileField(upload_to = upload_to, default = 'None/no_file')
    active = models.BooleanField(default = True)
    created = models.DateTimeField(auto_now_add=True)
    deleted = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self
    def get_upload_path(self,filename):
        return str(self.user.id) + "/model/" + filename


class Roi(models.Model):
    imgcontainer = models.ForeignKey(ImgContainer)
    x1 = models.IntegerField()
    y1 = models.IntegerField()
    x2 = models.IntegerField()
    y2 = models.IntegerField()
    def __str__(self):
        return self
