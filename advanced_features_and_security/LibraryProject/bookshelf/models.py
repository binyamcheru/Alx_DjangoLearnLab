from django.db import models

# Create your models here.
class Book(models.Model):
       title = models.CharField(max_length=200)
       author = models.CharField(max_length=100)
       publication_year = models.IntegerField()
       isbn = models.CharField(max_length=13)

       class Meta:
          permissions = [
            ('can_view', 'Can view book'),
            ('can_create', 'Can create book'),
            ('can_edit', 'Can edit book'),
            ('can_delete', 'Can delete book'),
        ]
       def __str__(self):
        return self.title

#________________________week11__________
'''Objective: Customize Django’s user model to suit the specific needs of your application, demonstrating an understanding of extending Django’s
 authentication system.

Task Description:
For this task, you will replace Django’s default user model with a custom user model that includes additional fields and functionality.
 This is a critical feature for applications that require user attributes beyond Django’s built-in user model.

Step 1: Set Up the Custom User Model
Duplicate the previous Django project directory django-models and rename it to advanced_features_and_security
Create a custom user model by extending AbstractUser, adding custom fields that are relevant to your application’s needs.

Fields to Add:

date_of_birth: A date field.
profile_photo: An image field.
Step 2: Update Settings to Use the Custom User Model
Configure Django to use this custom user model for all user-related functionalities.

Settings Configuration:
In your project’s settings.py, set the AUTH_USER_MODEL to point to your new custom user model.
Step 3: Create User Manager for Custom User Model
Implement a custom user manager that handles user creation and queries, ensuring it can manage the added fields effectively.

Custom Manager Functions to Implement:
create_user: Ensure it handles the new fields correctly.
create_superuser: Ensure administrative users can still be created with the required fields.
Step 4: Integrate the Custom User Model into Admin
Modify the Django admin to support the custom user model, ensuring that administrators can manage users effectively through the Django admin
 interface.

Admin Modifications Required:
Define a custom ModelAdmin class that includes configurations for the additional fields in your user model.
Step 5: Update Your Application to Use the Custom User Model
Adjust any part of your application that references the user model to use the new custom model.

Application Updates:
Update all foreign keys or user model references in your other models to use the custom user model.
Deliverables:
models.py: Include your custom user model and custom user manager.
admin.py: Set up the admin interface to manage the custom user model effectively.
settings.py: Modify to specify the custom user model as the default for the project.'''



from django.contrib.auth.models import AbstractUser, BaseUserManager #> has built-in functions to control users 'staff or superuser'
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields): #to create new user , extra_fields to be added such as profile_photo and date_of_birth
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email) #to clean the email from spaces and turn it to lowercase
        user = self.model(username=username, email=email, **extra_fields) #create user object'from CustomUser' within entered data
        user.set_password(password) #to hash the password with pbkdf2_sha256 algorithm
        user.save(using=self._db) #to save the object in database
        return user 

    def create_superuser(self, username, email, password=None, **extra_fields): #to create an user who has all permissions 'admin'
        extra_fields.setdefault("is_staff", True) #to access the control panel
        extra_fields.setdefault("is_superuser", True) # to have all permissions

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(username, email, password, **extra_fields) #to create user with predefined extra_fields

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    objects = CustomUserManager() #attaching to 'CustomUserManager' manager to use its functions instead of the default ones

    def __str__(self):
        return self.username

#____________________________________  to attach every ForeignKey to settings.AUTH_USER_MODEL
from django.conf import settings

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  #
