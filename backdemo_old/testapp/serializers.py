from rest_framework import serializers
from testapp.models import Compound, Query
# 序列化器和表单非常相似


class ArticleListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(allow_blank=True, max_length=100)
    body = serializers.CharField(allow_blank=True)
    created = serializers.DateTimeField()
    updated = serializers.DateTimeField()


class CompoundSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Compound
        fields = ['entiretyflag',
                  'partflag',
                  'smiles',
                  'reactionAtoms']


class QuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Query
        fields = ['product',
                  'reactant',
                  'type',
                  'created']
