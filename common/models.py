from django.db import models


class BaseModel(models.Model):
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        'user_control.UserModel', related_name='%(class)s_created_by',
        on_delete=models.SET_NULL, null=True, blank=True,
    )
    updated_by = models.ForeignKey(
        'user_control.UserModel', related_name='%(class)s_updated_by',
        on_delete=models.SET_NULL, null=True, blank=True,
    )
    extra_fields = models.JSONField(null=True, blank=True)

    class Meta:  # This is an abstract class and will not be created in the database
        abstract = True
