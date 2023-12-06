from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse
from CBS_manage import encode
from CBS_manage import models
from django.shortcuts import render


def home(request):
    bob = models.User(first_name='dfdf', last_name='dfdf2')
    return JsonResponse(bob, safe=False, encoder=encode.UserEncoder)


class Person:

    def __init__(self, name, age):
        self.name = name  # имя человека
        self.age = age  # возраст человека


class PersonEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Person):
            return {"name": obj.name, "age": obj.age}
            # return obj.__dict__
        return super().default(obj)
# Create your views here.
