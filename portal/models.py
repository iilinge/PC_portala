# модель для публикации счетчика
from django.db import models


# модель для публикации счетчика
class Question(models.Model):
    questiontext = models.CharField(max_length=200)
    pubdate = models.DateTimeField('дата публикации')

    def __str__(self):
        return self.questiontext


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choicetext = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choicetext

# Модель данных графа
import neomodel
from neomodel import (config, StructuredNode, StringProperty, IntegerProperty, UniqueIdProperty, RelationshipTo, RelationshipFrom, DateProperty)

class Male(StructuredNode):

    print('Class for Male Nodes')
    surname = StringProperty()
    age = IntegerProperty()
    country = StringProperty(default='US')

class Female(StructuredNode):

    print('Class for Male Female Nodes')
    surname = StringProperty()
    age = IntegerProperty()
    country = StringProperty(default='US')


class Movie(StructuredNode):
    print('Class for Movie Nodes')
    movieName = StringProperty(unique_index=True, required=True)
