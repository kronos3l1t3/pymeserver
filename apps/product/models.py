from django.db import models
from ..nomenclator.models import ProductType
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    """
        This is the table of the products (Articles and Services)
        """
    name = models.CharField(max_length=70, default="")
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE, related_name="ProductType")
    image = models.FilePathField(blank=False, null=False)
    active = models.BooleanField(default=True)
    description = models.TextField(max_length=2048, default="")
    meta_text = models.TextField(max_length=2048, default="")
    created_at = models.DateTimeField(
        _('action time'),
        auto_now_add=True,
        editable=False
    )
    updated_at = models.DateTimeField(
        _('change time'),
        auto_now=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Producto')
        verbose_name_plural = _('Productos')


class Car(models.Model):
    """
        This is the table of the products car (Services)
        """
    name = models.CharField(max_length=70, default="")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="products",)
    serialized = models.TextField(max_length=4096, default="")
    created_at = models.DateTimeField(
        _('action time'),
        auto_now_add=True,
        editable=False
    )
    updated_at = models.DateTimeField(
        _('change time'),
        auto_now=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Carrito')
        verbose_name_plural = _('Carrito Compra')


class Images(models.Model):
    """
        This is the table of images of products
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

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Imagen')
        verbose_name_plural = _('Imagenes')
