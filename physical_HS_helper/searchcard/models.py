from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    username = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cards(models.Model):
    '''
    Card data.
    '''
    db_index = models.IntegerField(blank=True, null=True)
    artist = models.TextField(blank=True, null=True)
    attack = models.TextField(blank=True, null=True)
    cardclass = models.TextField(db_column='cardClass', blank=True, null=True)  # Field name made lowercase.
    classes = models.TextField(blank=True, null=True)
    collectible = models.IntegerField(blank=True, null=True)
    collectiontext = models.TextField(db_column='collectionText', blank=True, null=True)  # Field name made lowercase.
    cost = models.TextField(blank=True, null=True)
    dbfid = models.TextField(db_column='dbfId', blank=True, null=True)  # Field name made lowercase.
    durability = models.TextField(blank=True, null=True)
    elite = models.TextField(blank=True, null=True)
    entourage = models.TextField(blank=True, null=True)
    faction = models.TextField(blank=True, null=True)
    flavor = models.TextField(blank=True, null=True)
    health = models.TextField(blank=True, null=True)
    hidestats = models.TextField(db_column='hideStats', blank=True, null=True)  # Field name made lowercase.
    howtoearn = models.TextField(db_column='howToEarn', blank=True, null=True)  # Field name made lowercase.
    howtoearngolden = models.TextField(db_column='howToEarnGolden', blank=True, null=True)  # Field name made lowercase.
    id = models.TextField(primary_key=True, blank=True, null=False)
    mechanics = models.TextField(blank=True, null=True)
    multiclassgroup = models.TextField(db_column='multiClassGroup', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(blank=True, null=True)
    overload = models.TextField(blank=True, null=True)
    playrequirements = models.TextField(db_column='playRequirements', blank=True, null=True)  # Field name made lowercase.
    playerclass = models.TextField(db_column='playerClass', blank=True, null=True)  # Field name made lowercase.
    race = models.TextField(blank=True, null=True)
    rarity = models.TextField(blank=True, null=True)
    referencedtags = models.TextField(db_column='referencedTags', blank=True, null=True)  # Field name made lowercase.
    card_set = models.TextField(blank=True, null=True)
    spelldamage = models.TextField(db_column='spellDamage', blank=True, null=True)  # Field name made lowercase.
    targetingarrowtext = models.TextField(db_column='targetingArrowText', blank=True, null=True)  # Field name made lowercase.
    card_text = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cards'

    def __str__(self):
        display = self.name + ' (Text: ' + self.card_text + ' Mechanics: ' + self.mechanics + ')'
        return str(display)


class CardsZhcn(models.Model):
    '''
    Card data in Chinese
    '''
    db_index = models.IntegerField(blank=True, null=True)
    artist = models.TextField(blank=True, null=True)
    attack = models.TextField(blank=True, null=True)
    cardclass = models.TextField(db_column='cardClass', blank=True, null=True)  # Field name made lowercase.
    classes = models.TextField(blank=True, null=True)
    collectible = models.IntegerField(blank=True, null=True)
    collectiontext = models.TextField(db_column='collectionText', blank=True, null=True)  # Field name made lowercase.
    cost = models.TextField(blank=True, null=True)
    dbfid = models.TextField(db_column='dbfId', blank=True, null=True)  # Field name made lowercase.
    durability = models.TextField(blank=True, null=True)
    elite = models.TextField(blank=True, null=True)
    entourage = models.TextField(blank=True, null=True)
    faction = models.TextField(blank=True, null=True)
    flavor = models.TextField(blank=True, null=True)
    health = models.TextField(blank=True, null=True)
    hidestats = models.TextField(db_column='hideStats', blank=True, null=True)  # Field name made lowercase.
    howtoearn = models.TextField(db_column='howToEarn', blank=True, null=True)  # Field name made lowercase.
    howtoearngolden = models.TextField(db_column='howToEarnGolden', blank=True, null=True)  # Field name made lowercase.
    id = models.TextField(primary_key=True, blank=True, null=False)
    mechanics = models.TextField(blank=True, null=True)
    multiclassgroup = models.TextField(db_column='multiClassGroup', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(blank=True, null=True)
    overload = models.TextField(blank=True, null=True)
    playrequirements = models.TextField(db_column='playRequirements', blank=True, null=True)  # Field name made lowercase.
    playerclass = models.TextField(db_column='playerClass', blank=True, null=True)  # Field name made lowercase.
    race = models.TextField(blank=True, null=True)
    rarity = models.TextField(blank=True, null=True)
    referencedtags = models.TextField(db_column='referencedTags', blank=True, null=True)  # Field name made lowercase.
    card_set = models.TextField(blank=True, null=True)
    spelldamage = models.TextField(db_column='spellDamage', blank=True, null=True)  # Field name made lowercase.
    targetingarrowtext = models.TextField(db_column='targetingArrowText', blank=True, null=True)  # Field name made lowercase.
    card_text = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cards_zhCN'

    def __str__(self):
        return str(self.name)




class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
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
