from django.db import models


# Create your models here.

class Friends(models.Model):
    friend1 = models.BigIntegerField(db_index=True)
    friend2 = models.BigIntegerField(db_index=True)
    class Meta:
        unique_together = (('friend1', 'friend2'),)


