from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from PIL import Image

class Contact(models.Model):
    first_name = models.CharField(max_length=50, default='None', db_index=True)
    last_name = models.CharField(max_length=50, default='None', db_index=True)
    email = models.EmailField()
    title = models.CharField(max_length=100, default='No Title', db_index=True)
    company = models.CharField(max_length=100, default='No Company', db_index=True)
    type = models.CharField(max_length=100, default='None', db_index=True)
    location = models.CharField(max_length=100, db_index=True)
    level = models.CharField(max_length=100, default='None', db_index=True)
    
    class Meta:
        verbose_name = "Contact"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class SelectedContacts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact_ids = models.TextField()  # Store contact IDs as a comma-separated list or JSON string
    created_at = models.DateTimeField(auto_now_add=True)

#Create Campaign_Emails:
class Campaign_Emails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    email = models.EmailField()
    first_name = models.CharField(max_length=100, default='', db_index=True)
    last_name = models.CharField(max_length=100, default='', db_index=True)
    company = models.CharField(max_length=100, default='', db_index=True)
    type = models.CharField(max_length=100, default='', db_index=True)
    location = models.CharField(max_length=100, default='None', db_index=True)  
    title = models.CharField(max_length=100, default='', db_index=True)
    campaign_name = models.CharField(max_length=255, default='', db_index=True)
    
    def __str__(self):
        return self.email
    
#Create Campaign:
class Campaign(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    phone = PhoneNumberField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.user.username} Profile'

    # def save(self, *args, **kwargs):
    #   super().save(*args, **kwargs)
        
    #    img = Image.open(self.image.path)
        
    #    if img.height > 300 or img.width > 300:
    #        output_size = (300, 300)
    #        img.thumbnail(output_size)
    #        img.save(self.image.path)
        