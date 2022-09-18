from rest_framework import serializers
from .models import Query
# 序列化器和表单非常相似


class QuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Query
        fields = ['product',
                  'reactant',
                  'type',
                  'created']
