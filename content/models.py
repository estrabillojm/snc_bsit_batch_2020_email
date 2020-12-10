from django.db import models

# Create your models here.
class BsitEmail(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.fullname