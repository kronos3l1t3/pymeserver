from django.db import models
from django.utils.translation import gettext_lazy as _


class Coin(models.Model):
    """
        This is the table of coins
        """
    name = models.CharField(max_length=70, default="")
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
        verbose_name = _('Moneda')
        verbose_name_plural = _('Monedas')


class Country(models.Model):
    """
        This is the table of countries
        """
    name = models.CharField(max_length=70, default="")
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
        verbose_name = _('Pais')
        verbose_name_plural = _('Paises')


class Location(models.Model):
    """
        This is the table of locations inside countries
        """
    models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name="countries",
    )
    name = models.CharField(max_length=70, default="")
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
        verbose_name = _('Localizacion')
        verbose_name_plural = _('Localizaciones')


class Gateway(models.Model):
    """
        This is the table of gateways to control payments methods
        """
    models.ForeignKey(
        Coin,
        on_delete=models.CASCADE,
        related_name="coins",
    )
    name = models.CharField(max_length=70, default="")
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
        verbose_name = _('Pasarela')
        verbose_name_plural = _('Pasarelas')


class ProductType(models.Model):
    """
        This is the table of Products Types
        """
    name = models.CharField(max_length=50, default="")
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
        verbose_name = _('Tipo de Producto')
        verbose_name_plural = _('Tipos de Productos')

