from django.db import models

# Create your models here.
class UserProfile(models.Model):
    email = models.EmailField(max_length=254)
    n_tickets = models.IntegerField(
                        # default = 0,
                        # validators = [
                            # MaxValueValidator(5),
                            # MinValueValidator(0)
                            # ]
                        )
    requesting = models.NullBooleanField()
    def __str__(self):
        return (self.email + '____Requesting? ' + str(self.requesting) + '_____' + str(self.n_tickets) + 'tickets.')
