from django.db import models

class WeightRecord(models.Model):
    weight = models.DecimalField(decimal_places=2, max_digits=5)
    body_fat = models.DecimalField(decimal_places=2, max_digits=5)
    date_recorded = models.DateField()
    slug = models.SlugField()
    time_created = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    class Meta:
        ordering = ["-date_recorded"]
        indexes = [models.Index(fields=["-date_recorded"])]
