from django.db import models

class Database(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name

class Strategy(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=128)
    is_default = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'strategies'

    def __unicode__(self):
        return self.name

class DictServer(models.Model):
    server = models.CharField(max_length=64)
    port = models.PositiveIntegerField(default=2628)
    databases = models.ManyToManyField(Database, blank=True, null=True, related_name='servers')
    strategies = models.ManyToManyField(Strategy, blank=True, null=True, related_name='servers')

    def __unicode__(self):
        return self.server

