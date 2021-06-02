from django.db import models

class JustTest(models.Model):
    mom = models.CharField("mom", max_length = 250)
    dad = models.CharField("dad", max_length = 250)
    sisterStuckedUnderTheTable = models.CharField("sisterStucked", max_length = 250)

    def __str__(self):
        return self.mom