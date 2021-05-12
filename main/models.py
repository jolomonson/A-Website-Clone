from django.db import models
from datetime import datetime
# Create your models here.
# Tutorial Model is a table in the database and title, content and published are attributes(basically headers)
class Tutorial(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField()
    published = models.DateTimeField('date published', default=datetime.now())
# Basically the __str__ function is to format the information in our Tutorial Table neatly depending on the  object you call
    def __str__(self):
        return self.title