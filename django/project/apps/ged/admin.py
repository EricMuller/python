from django.contrib import admin
from ged.models import Document
from ged.models import Basket
from ged.models import UploadFile


class DocumentAdmin(admin.ModelAdmin):

    list_display = [
        'name', 'path', 'contentType', 'created_at', 'updated_at',
        'version', 'basket']
    search_fields = ['name']


class BasketAdmin(admin.ModelAdmin):

    list_display = [
        'code', 'libelle', 'description', 'created_at', 'updated_at']
    search_fields = ['libelle']


class UploadFileAdmin(admin.ModelAdmin):

    list_display = ['name', 'created_at', 'updated_at']
    search_fields = ['libelle', 'created_at', 'updated_at']


admin.site.register(Document, DocumentAdmin)
admin.site.register(Basket, BasketAdmin)
admin.site.register(UploadFile, UploadFileAdmin)