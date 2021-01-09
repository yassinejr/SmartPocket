from django.contrib import admin
from .models import *


# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    # you should prevent author field to be manipulated
    readonly_fields = ['user']

    def get_form(self, request, obj=None, **kwargs):
        # here insert/fill the current user name or id from request
        Category.user = request.user
        return super().get_form(request, obj, **kwargs)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.user_id = request.user.id
        obj.last_modified_by = request.user
        obj.save()


class ExpensesAdmin(admin.ModelAdmin):
    # you should prevent author field to be manipulated
    readonly_fields = ['user']

    def get_form(self, request, obj=None, **kwargs):
        # here insert/fill the current user name or id from request
        Expenses.user = request.user
        return super().get_form(request, obj, **kwargs)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.user_id = request.user.id
        obj.last_modified_by = request.user
        obj.save()


admin.site.register(Category, CategoryAdmin)
admin.site.register(Expenses, ExpensesAdmin)
