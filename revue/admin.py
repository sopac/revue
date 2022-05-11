from django.contrib import admin
from django.contrib.gis.admin import GISModelAdmin

from .models import Building
from .models import UtilityWater
from .models import UtilityElectricity
from .models import InfrastructureTelecommunication
from .models import InfrastructurePort
from .models import InfrastructureFuel
from .models import InfrastructureBridge
from .models import InfrastructureRoads
from .models import InfrastructureAirPort
from .models import CropsAgriculture
from .models import Livestock

admin.site.site_header = 'PCRAFI Revue Tool - Field Data Validation'

#
admin.site.register(Building, GISModelAdmin)
admin.site.register(UtilityWater, GISModelAdmin)
admin.site.register(UtilityElectricity, GISModelAdmin)
admin.site.register(InfrastructureTelecommunication, GISModelAdmin)
admin.site.register(InfrastructurePort, GISModelAdmin)
admin.site.register(InfrastructureFuel, GISModelAdmin)
admin.site.register(InfrastructureBridge, GISModelAdmin)
admin.site.register(InfrastructureRoads, GISModelAdmin)
admin.site.register(InfrastructureAirPort, GISModelAdmin)
admin.site.register(CropsAgriculture, GISModelAdmin)
admin.site.register(Livestock, GISModelAdmin)
