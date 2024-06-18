from django.db import models
from django.contrib.auth.models import User
from django_softdelete.models import SoftDeleteModel


class BaseModel(SoftDeleteModel):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseModelUser(BaseModel):
    created_by = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE,related_name='created_by_%(class)s')
    updated_by = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE,related_name='updated_by_%(class)s')

    class Meta:
        abstract = True