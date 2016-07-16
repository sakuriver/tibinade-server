# coding: utf-8

import logging
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist

class Command(BaseCommand):
    args = '<target_id target_id ...>'
    help = u'カスタムAdminコマンドのテストです'

    def handle(self, *args, **options):

        for content_type in ContentType.objects.all():
            print("find view_{}".format(content_type.model))
            view_codename = "view_{}".format(content_type.model)
            try:
                view_permission = Permission.objects.get(content_type_id=content_type.id, codename=view_codename)
            except ObjectDoesNotExist:
                Permission.objects.create(content_type_id=content_type.id, name="Can view {}".format(content_type.model), codename=view_codename)
