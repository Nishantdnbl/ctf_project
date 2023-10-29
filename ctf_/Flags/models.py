from django.db import models

# Create your models here. 
class User(models.Model):
    #uesr_id = models.AutoField(primary_key=True)
    name_id = models.IntegerField()
    name = models.CharField(max_length=50)
    flag1 = models.IntegerField()
    flag2 = models.IntegerField()
    flag3 = models.IntegerField()
    flag4 = models.IntegerField()
    flag5 = models.IntegerField()
    def __str__(self):
        return self.name
class Submit_flag(models.Model):
    
    flag_1 =models.CharField(max_length=1000)
    flag_2 =models.CharField(max_length=1000)
    flag_3 =models.CharField(max_length=1000)
    flag_4 =models.CharField(max_length=1000)
    flag_5 =models.CharField(max_length=1000)
    flag = "Real_Flag"
    def __str__(self):
        return self.flag
class flg4(models.Model):
    flag =models.CharField(max_length=1000)
    def __str__(self):
        return self.flag


