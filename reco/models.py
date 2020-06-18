from django.db import models

# Create your models here.
class upload(models.Model):
    file = models.FileField(null=True,blank=True)

    def __str__(self):
        return self.name
    def delete(self, *args,**kwargs):
        self.file.delete()
        return super().delete(*args,**kwargs)
    