from django.db import models

# Create your models here.
class Doggo(models.Model):
    dog_name = models.CharField(primary_key=True, max_length=100)
    job_title = models.CharField(max_length=50)
    job_desc  = models.CharField(max_length=200)
    profile_picture = models.ImageField(upload_to='images/',max_length=100)

    def __str__(self):
        return str(self.dog_name)
