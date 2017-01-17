# -*- coding: utf-8 -*-

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuditHistory(models.Model):
    id = models.BigIntegerField(primary_key=True)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    data_version = models.IntegerField()
    state = models.IntegerField()
    status = models.IntegerField()
    comment = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)

    # class Meta:
    #     managed = False
    #     db_table = 'audit_history'


class Information(models.Model):



    id = models.BigIntegerField(primary_key=True)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    data_version = models.IntegerField()
    state = models.IntegerField()
    status = models.IntegerField()
    order_no = models.CharField(max_length=255)
    user_id = models.BigIntegerField()
    title = models.CharField(max_length=255)
    body = models.TextField()
    lable = models.IntegerField()
    contacts = models.CharField(max_length=20)
    contacts_mobile = models.CharField(max_length=20, blank=True, null=True)
    pics_id = models.BigIntegerField(blank=True, null=True)
    city_id = models.BigIntegerField()
    # choices = CITYS
    # ...
    # def __str__(self):  # __unicode__ on Python 2
    #     return self.title

    # class Meta:
    #     managed = False
    #     db_table = 'information'


class InformationPic(models.Model):
    id = models.BigIntegerField(primary_key=True)
    pic_url = models.CharField(max_length=255)
    information_id = models.BigIntegerField()
    state = models.IntegerField()

    # class Meta:
    #     managed = False
    #     db_table = 'information_pic'


class User(models.Model):
    id = models.BigIntegerField(primary_key=True)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    data_version = models.IntegerField()
    name = models.CharField(max_length=255)
    openid = models.CharField(max_length=255)
    union_id = models.CharField(max_length=255, blank=True, null=True)

    # class Meta:
    #     managed = False
    #     db_table = 'user'
