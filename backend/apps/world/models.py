from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.
class World(models.Model):
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.name

class Folder(MPTTModel):
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField()
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = 'name'