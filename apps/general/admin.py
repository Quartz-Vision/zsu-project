from django.contrib import admin
from apps.general.models import(
    MilitarySpecialization,
    MilitaryRank,
    Position,
    TariffCategory,
    TariffGrid,
    PremiumGrid,
    WacationType,
    PaymentType
)

admin.site.register(MilitarySpecialization)
admin.site.register(MilitaryRank)
admin.site.register(Position)
admin.site.register(TariffCategory)
admin.site.register(TariffGrid)
admin.site.register(PremiumGrid)
admin.site.register(WacationType)
admin.site.register(PaymentType)
