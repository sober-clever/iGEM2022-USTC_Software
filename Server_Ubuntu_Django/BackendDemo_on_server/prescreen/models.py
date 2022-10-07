# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


# class Decarboxylation(models.Model):
#     ec_num = models.CharField(max_length=20, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'decarboxylation'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Elimination(models.Model):
    ec_num = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'elimination'


class Hydrolysis(models.Model):
    ec_num = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hydrolysis'


class Ismerization(models.Model):
    ec_num = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ismerization'


class Ligation(models.Model):
    ec_num = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ligation'


class Mustcontain(models.Model):
    ec_num = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mustcontain'


# class Others(models.Model):
#     ec_num = models.CharField(max_length=20, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'others'


# class Reactions(models.Model):
#     ec_num = models.CharField(primary_key=True, max_length=20)
#     reaction = models.CharField(max_length=255)
#     substrate = models.CharField(max_length=255, blank=True, null=True)
#     product = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'reactions'
#         unique_together = (('ec_num', 'reaction'),)


class Redox(models.Model):
    ec_num = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'redox'


class Transfer(models.Model):
    ec_num = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transfer'


class Query(models.Model):
    # reactant = models.ForeignKey(Compound, on_delete=models.CASCADE, related_name='Queries1')

    # product = models.ForeignKey(Compound, on_delete=models.CASCADE, related_name='Queries2')

    reactant = models.JSONField()

    product = models.JSONField()

    type = models.CharField(max_length=100)

    # 用于记录这个查询什么时候被创建
    created = models.DateTimeField(auto_now=True)


class Query2(models.Model):
    # reactant = models.ForeignKey(Compound, on_delete=models.CASCADE, related_name='Queries1')

    # product = models.ForeignKey(Compound, on_delete=models.CASCADE, related_name='Queries2')

    ph = models.CharField(max_length=100)

    temp = models.CharField(max_length=100)

    substrate_info = models.CharField(max_length=200)

    ec_num = models.CharField(max_length=100)

    organism = models.CharField(max_length=200)

    # 用于记录这个查询什么时候被创建
    created = models.DateTimeField(auto_now=True)


class Enzyme(models.Model):
    ec_num = models.CharField(max_length=20, blank=True, primary_key=True)

    ec_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enzyme'


class Reaction(models.Model):   # Reaction 数据表的补充，添加了辅因子的信息
    ec_num = models.CharField(max_length=20, blank=True)
    reaction = models.CharField(max_length=255)
    substrate = models.CharField(max_length=255, blank=True, null=True)
    product = models.CharField(max_length=255, blank=True, null=True)
    cofactor = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reaction'
        # unique_together = (('ec_num', 'reaction'),)


class Km(models.Model):
    ec_num = models.CharField(max_length=20)
    substrate = models.CharField(max_length=200)
    speciesname = models.CharField(max_length=200)  # 种属
    temp = models.FloatField()
    ph = models.FloatField()
    km = models.FloatField()

    class Meta:
        managed = False
        db_table = 'km'
        indexes = [models.Index([ec_num, soundex])]


class Kcat_Km(models.Model):
    ec_num = models.CharField(max_length=20)
    substrate = models.CharField(max_length=200)    # 底物信息
    speciesname = models.CharField(max_length=200)  # 种属
    temp = models.FloatField()
    ph = models.FloatField()
    kcat_km = models.FloatField()

    class Meta:
        managed = False
        db_table = 'kcat_km'
        indexes = [models.Index([ec_num, soundex])]


class Organism(models.Model):   # 未设主键，需要在数据表 Organism 内添加自增 id
    ec_num = models.CharField(max_length=20, blank=True)
    organism = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'organism'


class Kinetic(models.Model):
    ec_num = models.CharField(max_length=20)
    speciesname = models.CharField(max_length=200)
    ph = models.CharField(max_length=100)
    temp = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'kinetic'


class Phtemp(models.Model):
    ec_num = models.CharField(max_length=20)
    speciesname = models.CharField(max_length=200)
    ph = models.CharField(max_length=100)
    temp = models.CharField(max_length=100)
    literture = models.CharField(max_length=100)
    soundex = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'Phtemp'
        indexes = [models.Index(fields=["soundex"]), models.Index(fields=["ec_num"])]
