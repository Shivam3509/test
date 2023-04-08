from django.db import models

# Create your models here.
POSTION_CHOICES = (
    ("worker", "worker"),
    ("superwiser", "superwiser"),
    ("production_manager", "production_manager"),
    ("qwality_head", "qwality_head"),
    ("plant_head", "plant_head"),
    ("Director", "Director"),
)

class Employe(models.Model):
    
    name = models.CharField(max_length=100)
    emp_id = models.IntegerField()
    position = models.CharField(max_length=50, choices=POSTION_CHOICES, default="worker")
    email = models.EmailField(max_length=100, null=True, blank=True)
    mobile = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name