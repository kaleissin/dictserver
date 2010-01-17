from django.contrib import admin

from dictserver.models import *

class DatabaseAdmin(admin.ModelAdmin):
    model = Database 
    list_display = ('name', 'description')
admin.site.register(Database, DatabaseAdmin)

class StrategyAdmin(admin.ModelAdmin):
    model = Strategy 
    list_display = ('name', 'description')
admin.site.register(Strategy, StrategyAdmin)

class DictServerAdmin(admin.ModelAdmin):
    model = DictServer 
    list_display = ('server',)
admin.site.register(DictServer, DictServerAdmin)
