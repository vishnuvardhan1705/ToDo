from django.db import models

class tasks(models.Model):
    task = models.CharField(max_length=250)
    iscompleted = models.BooleanField(default=False)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.task