from django.contrib import admin
from .models import *


# Register your models here.


class SourceAdmin(admin.ModelAdmin):
    # you should prevent author field to be manipulated
    readonly_fields = ['user']

    def get_form(self, request, obj=None, **kwargs):
        # here insert/fill the current user name or id from request
        Source.user = request.user
        return super().get_form(request, obj, **kwargs)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.user_id = request.user.id
        obj.last_modified_by = request.user
        obj.save()


class IncomesAdmin(admin.ModelAdmin):
    # you should prevent author field to be manipulated
    readonly_fields = ['user']

    def get_form(self, request, obj=None, **kwargs):
        # here insert/fill the current user name or id from request
        Incomes.user = request.user
        return super().get_form(request, obj, **kwargs)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.user_id = request.user.id
        obj.last_modified_by = request.user
        obj.save()


admin.site.register(Source, SourceAdmin)
admin.site.register(Incomes, IncomesAdmin)
