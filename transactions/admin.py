from django.contrib import admin
from .models import (
    Supplier, 
    PurchaseBill, 
    PurchaseItem,
    PurchaseBillDetails, 
    SaleBill, 
    SaleItem,
    SaleBillDetails
)

admin.site.register(Supplier)
admin.site.register(PurchaseBill)
admin.site.register(PurchaseItem)
admin.site.register(PurchaseBillDetails)
admin.site.register(SaleBill)
admin.site.register(SaleItem)
admin.site.register(SaleBillDetails)


from django.contrib import admin
from transactions.models import PurchaseBillDetails

class HiddenModelAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}

admin.site.unregister(PurchaseBillDetails)
admin.site.register(PurchaseBillDetails, HiddenModelAdmin)



from django.contrib import admin
from transactions.models import SaleBillDetails

class HiddenModelAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}

admin.site.unregister(SaleBillDetails)
admin.site.register(SaleBillDetails, HiddenModelAdmin)

from django.contrib import admin
from transactions.models import PurchaseBill

class HiddenModelAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}

admin.site.unregister(PurchaseBill)
admin.site.register(PurchaseBill, HiddenModelAdmin)

from django.contrib import admin
from transactions.models import SaleBill

class HiddenModelAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}

admin.site.unregister(SaleBill)
admin.site.register(SaleBill, HiddenModelAdmin)