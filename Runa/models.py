from django.db import models

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=100, unique=True)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, blank=True, null=True, related_name='children'
    )

    def __str__(self):
        return self.name