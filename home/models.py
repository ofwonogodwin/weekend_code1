from django.db import models

# Create your models here.
class trial(models.Model):
    title =models.CharField(max_length=225)
    author =models.CharField(max_length=45)
    fname =models.CharField(max_length=50)
    lname =models.CharField(max_length=50,)
    email =models.EmailField(max_length=100,default='example@gmil.com')
    age =models.IntegerField()
    content =models.TextField()
    thumbnail =models.ImageField(upload_to="thumbnail/",default="default.png")
    dateCreated =models.DateTimeField(auto_now_add=True)

    ## The attributes are like the colmns on the tables.

    ## This Def string thing is just to give direct identity to the objects back in the database

    def __str__(self):
        return self.author