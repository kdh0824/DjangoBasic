from django.db import models


# Create your models here.
class User(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50, null=True)
    mobile = models.CharField(max_length=50, null=True)
    username = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'users'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'
