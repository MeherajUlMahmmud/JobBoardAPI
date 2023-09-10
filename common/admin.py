from django.contrib import admin

from common.models import BaseModel


class RawIdFieldsAdmin(admin.ModelAdmin):

    def __init__(self, *args, **kwargs):
        super(RawIdFieldsAdmin, self).__init__(*args, **kwargs)
        # make all ForeignKey fields use raw_id_fields
        self.raw_id_fields = [field.name for field in self.model._meta.get_fields() if
                              field.is_relation and field.many_to_one]
        if issubclass(self.model, BaseModel):
            primary_key = self.model._meta.pk.name
            extra_fields = 'extra_fields'
            timestamp_fields = [
                'created_at',
                'updated_at',
            ]
            status_fields = [
                'is_active',
                'is_deleted',
            ]
            self.list_display = [primary_key] + list(self.list_display) + timestamp_fields + status_fields
            self.readonly_fields = list(self.readonly_fields) + timestamp_fields
            self.list_filter = list(self.list_filter) + timestamp_fields + status_fields
            # self.exclude = list(self.exclude) + [extra_fields]
            # self.fieldsets = list(self.fieldsets) + [
            #     ('Extra Fields', {'fields': extra_fields}),
            # ]
            # self.add_fieldsets = list(self.add_fieldsets) + [
            #     ('Extra Fields', {'fields': extra_fields}),
            # ]
