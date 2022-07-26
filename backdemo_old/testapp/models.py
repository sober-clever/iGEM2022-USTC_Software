from django.db import models
from django.utils import timezone


class Article(models.Model):
    title = models.CharField(max_length=100)

    body = models.TextField()

    created = models.DateTimeField(default=timezone.now)

    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Compound(models.Model):
    entiretyflag = models.BooleanField()

    partflag = models.IntegerField()

    # 有机物 smiles 的最大长度是 200
    smiles = models.CharField(max_length=200)

    reactionAtoms = models.JSONField()

    def __str__(self):
        return self.smiles


class Query(models.Model):
    # reactant = models.ForeignKey(Compound, on_delete=models.CASCADE, related_name='Queries1')

    # product = models.ForeignKey(Compound, on_delete=models.CASCADE, related_name='Queries2')

    reactant = models.JSONField()

    product = models.JSONField()

    type = models.CharField(max_length=100)

    # 用于记录这个查询什么时候被创建
    created = models.DateTimeField(auto_now=True)
