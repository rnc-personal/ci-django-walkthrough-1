from django.db import models

# Create your models here.

# Define a model for the todo list,field tyoes and attributes


class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

# Overriding the dfault naming convention for the items in the model
    def __str__(self):
        return self.name
