from distutils.command.upload import upload
from django.db import models

class GeeksModel(models.Model):
    # Fields of the models
    title = models.CharField(max_length=100)
    desc = models.TextField()
    lst_mdf = models.DateTimeField(auto_now_add= True)
    img = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title
    
