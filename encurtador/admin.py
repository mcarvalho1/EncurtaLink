from django.contrib import admin
from encurtador.models import EncurtadorModel

# Register your models here.

@admin.register(EncurtadorModel)
class EncurtadorAdmin (admin.ModelAdmin):
    list_display = ('link', 'uid')