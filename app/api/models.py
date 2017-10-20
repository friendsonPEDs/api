from django.db import models

# Create your models here.
class Steps(models.Model):
    """This class represents the class mode."""
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_start = models.DateTimeField()
    # date_end may be redundant if we stick to only 1 hour increments
    date_end = models.DateTimeField()
    steps = models.IntegerField()
    owner = models.ForeignKey(
        'auth.User',
        related_name='steps',
        on_delete=models.CASCADE
    )
