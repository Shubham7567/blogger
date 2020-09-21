from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if email is None:
            raise TypeError("User must have an email")
        
        user = self.model(
            email = self.normalize_email(email),
        )

        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password):
        if password is None:
            raise TypeError('Password should not be null')

        user = self.create_user(email,password)

        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user

class User(AbstractBaseUser):
    email = models.EmailField(max_length=80,db_index=True,unique=True)
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=20)
    Profile = models.ImageField(upload_to="users/%y/%m/%d",default="defaultuser.png")
    DateOfBirth = models.DateField(blank=True,null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.name
    
    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser
    