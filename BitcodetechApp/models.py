from django.db import models

# Create your models here.
class Email_Soon(models.Model):
    eMail = models.EmailField()

    def __inti__(self):
        return self.eMail