from django.db import models
from datetime import date



# Job history classes
class Job(models.Model):
    company = models.CharField(max_length=200)
    job_title = models.CharField(max_length=100)
    begin_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    d1 = models.TextField(blank=True, null=True)
    d2 = models.TextField(blank=True, null=True)
    d3 = models.TextField(blank=True, null=True)
    d4 = models.TextField(blank=True, null=True)
    d5 = models.TextField(blank=True, null=True)
    d6 = models.TextField(blank=True, null=True)
    d7 = models.TextField(blank=True, null=True)
    d8 = models.TextField(blank=True, null=True)
    d9 = models.TextField(blank=True, null=True)
    d10 = models.TextField(blank=True, null=True)

    def publish(self):
        self.save()
        self.publish()

    def __str__(self):
        return u'%s - %s' % (self.company, self.job_title)