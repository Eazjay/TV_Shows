from django.db import models

class ShowsManager(models.Manager):
    def shows_validator(self, shows_data):
        errors = {}
        if len(shows_data['title']) < 2:
            errors['title'] = "Title should be at least 5 characters"
        if len(shows_data['network']) < 2:
            errors['network'] = "Network should be at least 5 characters"
        if len(shows_data['release_date']) < 5:
            errors['release_date'] = "Add a release date"
        if len(shows_data['desc']) < 10:
            errors['desc'] = "Description should be at least 10 characters"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowsManager()