from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Coin(models.Model):
    """
    This is the table of coins
    """
    coin_name = models.CharField(max_length=70)
    base = models.BooleanField(default=False)
    first = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    value_change = models.FloatField(default=1.00)
    created_at = models.DateTimeField(
        _('action time'),
        auto_now_add=True,
        editable=False
    )
    updated_at = models.DateTimeField(
        _('change time'),
        auto_now=True
    )

    class Meta:
        verbose_name = _('Coin')
        verbose_name_plural = _('Coins')


class Country(models.Model):
    """
    This is the table of countries
    """
    country_name = models.CharField(max_length=70)
    iso3 = models.CharField(max_length=4)
    iso_numeric = models.IntegerField()
    continent_code = models.CharField(max_length=3)
    currency_code = models.ForeignKey(Coin, on_delete=models.CASCADE, related_name="coins",)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(
        _('action time'),
        auto_now_add=True,
        editable=False
    )
    updated_at = models.DateTimeField(
        _('change time'),
        auto_now=True
    )

    class Meta:
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')


class Location(models.Model):
    """
    This is the table of locations inside countries
    """
    models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name="countries",
    )
    location_name = models.CharField(max_length=70)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(
        _('action time'),
        auto_now_add=True,
        editable=False
    )
    updated_at = models.DateTimeField(
        _('change time'),
        auto_now=True
    )

    class Meta:
        verbose_name = _('Location')
        verbose_name_plural = _('Locations')


class Gateway(models.Model):
    """
    This is the table of gateways to control payments methods
    """
    models.ForeignKey(
        Coin,
        on_delete=models.CASCADE,
        related_name="coins",
    )
    gateway_name = models.CharField(max_length=70, default="")
    secret_key = models.CharField(max_length=1024, default="")
    user_code = models.CharField(max_length=1024, default="")
    ecommerce_code = models.CharField(max_length=50, default="")
    first = models.BooleanField(default=False)
    cards = models.BooleanField(default=True)
    charge = models.FloatField(default=1)
    url = models.CharField(max_length=256, default="")
    url_response = models.CharField(max_length=256, default="")
    description = models.TextField(max_length=2048, default="")
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(
        _('action time'),
        auto_now_add=True,
        editable=False
    )
    updated_at = models.DateTimeField(
        _('change time'),
        auto_now=True
    )

    class Meta:
        verbose_name = _('Gateway')
        verbose_name_plural = _('Gateways')
