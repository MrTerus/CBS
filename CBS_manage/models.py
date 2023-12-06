from django.db import models


class User(models.Model):
    id = models.IntegerField(
        auto_created=True,
        primary_key=True
    )
    first_name = models.CharField(
        max_length=255,
    )
    last_name = models.CharField(
        max_length=255,
    )

    def __str__(self):
        return ' '.join([
            self.first_name,
            self.last_name,
        ])


class Post(models.Model):
    name = models.CharField(
        max_length=255,
    )
    text = models.CharField(
        max_length=255,
    )

    def __str__(self):
        return ' '.join([
            self.name,
            self.text,
        ])


