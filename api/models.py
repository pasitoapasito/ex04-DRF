from django.db import models


class User(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    
    class Meta:
        db_table = 'users'