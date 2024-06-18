from django.db import models

from apis.base_models import BaseModelUser

# Create your models here.


class Task(BaseModelUser):
    title = models.CharField(max_length=255, blank=False, null=False)
    child = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.id} : {self.title}"