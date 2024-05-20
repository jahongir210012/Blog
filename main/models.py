from django.db import models
from django.urls import reverse


class About(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    image = models.ImageField(upload_to='media/',blank=True)

    def str(self):
        return self.title

class Blog(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    image = models.FileField(upload_to='media/',blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.title
    def get_absolute_url(self):
        return reverse('main:Blog', args=[self.title])

    class Meta:
        ordering = ('-date',)

class Protain(models.Model):
    page_title = models.CharField(max_length=250, default='You will find a best protain in our shop')
    page_info = models.CharField(max_length=250, default='The best protain is here')
    title = models.CharField(max_length=250)
    body = models.TextField()
    image = models.ImageField(upload_to='media/',blank=True)

    def str(self):
        return self.title

class Contact(models.Model):
    phone_number = models.CharField(max_length=250)
    location = models.TextField()
    email = models.TextField()

    def str(self):
        return self.phone_number
