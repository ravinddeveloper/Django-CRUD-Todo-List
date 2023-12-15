from django.db import models

# Create your models here.
class To_do_list(models.Model):
    text=models.CharField(max_length=100)
    date_of_posted=models.DateTimeField(auto_now=True)
    due_date=models.DateField(auto_now=False, auto_now_add=False)
    completed=models.BooleanField(default=False)
