from django.db import models
from django.db.models import Model
from django.db.models import CharField


class Category(Model):
    name = CharField(max_length=255)
