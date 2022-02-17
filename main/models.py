from django.db import models

class Task(models.Model):
    title = models.CharField('Title', max_length=50)
    date = models.DateTimeField('Date')
    description = models.CharField('Description', max_length=200)
    complete = models.BooleanField('Complete')

    def __str__():
        return self.title