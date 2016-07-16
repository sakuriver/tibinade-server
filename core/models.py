# -*- coding: utf-8 -*-
from django.db import models

class ItemMaster(models.Model):
    """アイテムマスタ.
    """
    class Meta:
        verbose_name = 'アイテムマスタ'
        verbose_name_plural = 'アイテムマスタ'
    chara_id = models.IntegerField('キャラマスタID')
    name = models.CharField('名前', max_length=255)
    image = models.CharField('画像名', max_length=255)
    please_ok_level = models.IntegerField('頼めるレベル')
    please_number = models.IntegerField('頼む回数')
    please_exp = models.IntegerField('お願いでもらえる経験値')

class CharaMaster(models.Model):
    """キャラマスタ.
    """
    class Meta:
        verbose_name = 'キャラマスタ'
        verbose_name_plural = 'キャラマスタ'
    name = models.CharField('名前', max_length=255)
    bg_path = models.CharField('背景画像', max_length=255)
    
