from django.db import models

class Shows_Manager(models.Manager):
    def shows_validator(self, shows_data):
        errors = {}
        if len(shows_data['title']) < 2:
            errors['title'] = "Title should be at least 2 characters"
        if len(shows_data['title']) == 0:
            errors['title'] = "Enter a title"
        if len(shows_data['network']) < 2:
            errors['network'] = "Network should be at least 2 characters"
        if len(shows_data['network']) == 0:
            errors['network'] = "Enter a network"
        if len(shows_data['release_date']) < 5:
            errors['release_date'] = "Add a date"
        if len(shows_data['release_date']) == 0:
            errors['release_date'] = "Enter a date"
        if len(shows_data['desc']) < 10:
            errors['desc'] = "Description should be at least 10 characters"
        if len(shows_data['desc']) == 0:
            errors['desc'] = ""
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Shows_Manager()