from django.db import models
from ..nomenclator.models import ProductType
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    """
        This is the table of the products (Articles and Services)
        """
    name = models.CharField(max_length=70, default="")
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE, related_name="ProductType")
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
        verbose_name = _('Producto')
        verbose_name_plural = _('Productos')


class Car(models.Model):
    """
        This is the table of the products car (Services)
        """
    name = models.CharField(max_length=70, default="")
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
        verbose_name = _('Carrito')
        verbose_name_plural = _('Carrito Compra')