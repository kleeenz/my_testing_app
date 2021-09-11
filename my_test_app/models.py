from django.db import models


class table_data(models.Model):
    gender = models.CharField(max_length=100)
    full_name = models.CharField(max_length = 100)
    
