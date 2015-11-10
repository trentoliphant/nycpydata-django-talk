from django.db import Models
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.model import ContentType

class UIPermissionManager(models.Manager):
    def get_queryset(self):
        return super(UIPermissionManager,
            self).get_queryset().filter(
            content_type__model='uipermission'
        )


class UIPermission(Permission):

    objects = UIPermissionManager()

    class Meta:
        proxy = True
        verbose_name = 'ui_permission'

        def save(self, *args, **kwargs):
            ct, create = ContentType.objects.get_or_create(
                model=self._meta.model_name,
                app_label=self._meta.app_label,
            )
            self.content_type = ct
            super(UIPermission, self).save(*args)