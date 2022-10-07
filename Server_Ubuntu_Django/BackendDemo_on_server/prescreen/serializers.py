from rest_framework import serializers
from .models import Query, Query2
# 序列化器和表单非常相似


class QuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Query
        fields = ['product',
                  'reactant',
                  'type',
                  'created']


class Query2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Query2
        fields = [
            'ph',
            'temp',
            'ec_num',
            'organism',
            'substrate_info',
            'created'
        ]
