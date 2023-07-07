from django.db import models

# Create your models here.



# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Addresses(models.Model):
    state = models.CharField(max_length=50)
    town = models.CharField(max_length=25)
    commune = models.IntegerField()
    neighbourhood = models.CharField(max_length=25)
    street = models.IntegerField()
    number = models.CharField(max_length=20)
    complement = models.CharField(max_length=200)
    postal_code = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'addresses'


class AdrList(models.Model):
    id = models.IntegerField(primary_key=True)
    id_adress = models.ForeignKey(Addresses, models.DO_NOTHING, db_column='id_adress')
    id_user = models.ForeignKey('Users', models.DO_NOTHING, db_column='id_user')

    class Meta:
        managed = False
        db_table = 'adr_list'


class Post(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)


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


class Designs(models.Model):
    name = models.CharField(max_length=106)
    img = models.CharField(max_length=106)
    ai = models.CharField(max_length=106)

    class Meta:
        managed = False
        db_table = 'designs'


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


class PackingColors(models.Model):
    color = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'packing_colors'


class PucharseOrders(models.Model):
    id_wine = models.IntegerField()
    id_design = models.ForeignKey(Designs, models.DO_NOTHING, db_column='id_design', blank=True, null=True)
    id_real_design = models.IntegerField(blank=True, null=True)
    msg = models.CharField(max_length=255, blank=True, null=True)
    id_packing_color = models.IntegerField()
    id_secondary_packing_color = models.IntegerField()
    delivery_date = models.DateField()
    id_delivery_place = models.CharField(max_length=255)
    id_user = models.BigIntegerField()
    id_vaucher = models.CharField(max_length=100)
    amount = models.IntegerField()
    paid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pucharse_orders'


class RealDesigns(models.Model):
    name = models.CharField(max_length=45)
    img = models.CharField(max_length=114)
    dxf = models.CharField(max_length=114)

    class Meta:
        managed = False
        db_table = 'real_designs'


class SecondaryPackingColors(models.Model):
    color = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'secondary_packing_colors'


class TagList(models.Model):
    id = models.IntegerField(primary_key=True)
    id_design = models.ForeignKey('Tags', models.DO_NOTHING, db_column='id_design')
    id_tag = models.ForeignKey(Designs, models.DO_NOTHING, db_column='id_tag')

    class Meta:
        managed = False
        db_table = 'tag_list'


class Tags(models.Model):
    name = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'tags'


class Users(models.Model):
    id = models.BigIntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.BigIntegerField()
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class Vouchers(models.Model):
    file = models.TextField()

    class Meta:
        managed = False
        db_table = 'vouchers'


class WineKinds(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'wine_kinds'
