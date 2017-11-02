from django.db import models

class Steps(models.Model):
    """
    This class represents the class mode.
    """
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

    def __str__(self):
        return self.owner.username + ' took ' + str(self.steps) + ' between ' + self.date_start.strftime("%H") + ' and ' + self.date_end.strftime("%H, %B %d, %Y")

    def __repr__(self):
        return str(self.steps) + ' on ' + self.date_start.strftime("%H, %B %d, %Y") + ' added.'

    def get_steps(self):
        return self.steps
