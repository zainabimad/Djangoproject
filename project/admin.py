from django.contrib import admin
from project import models
from Orphans import models as orph
from Guarantor import models as Gua
# Register your models here.
admin.site.register(models.Authentic)
admin.site.register(models.AddAc)
admin.site.register(orph.AddOr)
admin.site.register(orph.AddRe)
admin.site.register(Gua.AddGu)
