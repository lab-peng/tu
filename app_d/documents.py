# elastic search file
from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry

from .models import SampleModel

@registry.register_document
class SampleModelDocument(Document):
    class Index:
        name = 'samplemodel'
    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }
    class Django:
         model = SampleModel
         fields = [
             'char',
             'longer_char',
         ]

