import neomodel

# подключение к базе данных Neo4j
# модель для neomodel
from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
    UniqueIdProperty, RelationshipTo, RelationshipFrom)

config.DATABASE_URL = 'bolt://db_glossary:ibrae@localhost:7687'



class Country(StructuredNode):
    code = StringProperty(unique_index=True, required=True)
    inhabitant = RelationshipFrom('Person', 'IS_FROM')

class Person(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True)
    age = IntegerProperty(index=True, default=0)
    country = RelationshipTo(Country, 'IS_FROM')
