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
    

class BallonMaster(models.Model):
    """吹き出しの座標とか設定するマスタ.
    """
    class Meta:
        verbose_name = '吹き出しマスタ'
        verbose_name_plural = '吹き出しマスタ'
    name = models.CharField('名称', max_length=255)
    pos_x = models.IntegerField('X座標')
    pos_y = models.IntegerField('Y座標')
    
class CharaPauseMaster(models.Model):
    """キャラクターのポーズマスタ.
    """
    class Meta:
        verbose_name = 'キャラポーズマスタ'
        verbose_name_plural = 'キャラポーズマスタ'
    chara_id = models.ForeignKey(CharaMaster)
    release_goodfirend = models.IntegerField('解放される仲良し度')
    serif_number = models.IntegerField('セリフ番号')
    face_number = models.IntegerField('顔番号')
    item_id = models.ForeignKey(ItemMaster)
    pause_number = models.IntegerField('ポーズ番号')
    ballon_id = models.IntegerField('吹き出し番号')
    