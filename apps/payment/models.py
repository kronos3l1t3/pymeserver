from django.db import models
from ..product.models import Product
from django.utils.translation import gettext_lazy as _


class Payment(models.Model):
    """
        This is the table of the products (Articles and Services)
        """
    name = models.CharField(max_length=70, default="")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="ProductType")
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
        verbose_name = _('Pago')
        verbose_name_plural = _('Pagos')
