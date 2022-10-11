from django.contrib import admin

# Register your models here.
from agmp.models import Variantagmp, Drugagmp, Geneagmp
class VariantagmpAdmin(admin.ModelAdmin):
    list_display = ['id']

    # pass
class DrugagmpAdmin(admin.ModelAdmin):
    list_display = ['id']

class GeneagmpAdmin(admin.ModelAdmin):
    list_display = ['id']



admin.site.register(Drugagmp, DrugagmpAdmin)
admin.site.register(Variantagmp, VariantagmpAdmin)
admin.site.register(Geneagmp, GeneagmpAdmin)