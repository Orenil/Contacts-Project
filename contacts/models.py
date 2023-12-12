from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    first_name = models.CharField(max_length=50, default='Null')
    last_name = models.CharField(max_length=50, default='Null')
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    title = models.CharField(max_length=100, default='No Title')
    company = models.CharField(max_length=100, default='No Company')
    type = models.CharField(max_length=100, default='None')
    location = models.CharField(max_length=100)
    level = models.CharField(max_length=100, default='None')

    campaigns = models.ManyToManyField('Campaign', related_name='contacts', blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Campaign(models.Model):
    name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50, default='Null')
    last_name = models.CharField(max_length=50, default='Null')
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    title = models.CharField(max_length=100, default='No Title')
    company = models.CharField(max_length=100, default='No Company')
    type = models.CharField(max_length=100, default='None')
    location = models.CharField(max_length=100)
    level = models.CharField(max_length=100, default='None')

    def __str__(self):
        return self.name

class SelectedContacts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact_ids = models.TextField()  # Store contact IDs as a comma-separated list or JSON string
    created_at = models.DateTimeField(auto_now_add=True)


