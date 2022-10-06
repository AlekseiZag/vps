import uuid

from django.db import models

VPS_STATUS = (
    ("started", "started"),
    ("blocked", "blocked"),
    ("stopped", "stopped"),
)


class VPS(models.Model):
    """VPS Model"""
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cpu = models.IntegerField(verbose_name="Количество ядер")
    ram = models.IntegerField(verbose_name="Объем RAM")
    hdd = models.IntegerField(verbose_name="Объем HDD")
    status = models.CharField(max_length=7, choices=VPS_STATUS, default="started", verbose_name="Статус сервера")

    class Meta:
        abstract = True
        ordering = ['-created_at', '-updated_at']
