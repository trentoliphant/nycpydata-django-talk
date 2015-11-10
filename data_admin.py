from django.contrib import admin
from django.apps import apps

for model in apps.get_app_config('data').get_models():
    admin.site.register(model)


for model in apps.get_app_config('data').get_models():
    field_names = [f.name for f in model._meta.get_fields()
                   if f.concrete]
    cls_nm = "{}_admin".format(model._meta.model_name)
    options = {'list_display': field_names}
    cls = type(cls_nm, (admin.ModelAdmin,), options)

    admin.site.register(model, cls)

class ExampleModelAdmin(admin.ModelAdmin):
    list_display('field1','field2','field3')

admin.site.register(ExampleModel, ExampleModelAdmin)