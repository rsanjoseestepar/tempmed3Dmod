from django.db import models
from django.contrib.auth.models import User

# Create your models here.



def upload_to(instance, filename):
    return instance.get_upload_path(filename)

class Organ(models.Model):
    organ = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    def __str__(self):
        return self

    def __repr__(self):
        return 'Organ ID: ' + str(self.organ)

class BodyPart(models.Model):
    body_part = models.CharField(max_length=20)
    #organ = models.ManyToManyField(Organ)
    def __str__(self):
        return self

class ImgContainer(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    #tentative_body_part = models.ManyToManyField(BodyPart, default=None, null=True)
    #tentative_img_type = models.CharField(max_length=10, default=None, null=True)
    active = models.BooleanField(default = True)
    created = models.DateTimeField(auto_now_add=True)
    deleted = models.DateTimeField(auto_now=True)
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
    def __str__(self):
        return self
    def get_upload_path(self,filename):
        return str(self.user.id) + "/medimg/" + str(self.img_type) + filename



class Model(models.Model):
    user = models.ForeignKey(User)
    medimg = models.ForeignKey(MedImg, null=True)
    organ = models.ForeignKey(Organ, null=True)
    name = models.CharField(max_length=100)
    model_file = models.FileField(upload_to = upload_to, default = 'None/no_file')
    active = models.BooleanField(default = True)
    created = models.DateTimeField(auto_now_add=True)
    deleted = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self
    def get_upload_path(self,filename):
        return str(self.user.id) + "/model/" + filename

    def __repr__(self):
        return 'Mesh ID: ' + str(self.name)


class Roi(models.Model):
    imgcontainer = models.ForeignKey(ImgContainer)
    x1 = models.IntegerField()
    y1 = models.IntegerField()
    x2 = models.IntegerField()
    y2 = models.IntegerField()
    def __str__(self):
        return self
