#from django.db import models
from django.contrib.gis.db import models
from django.utils.html import mark_safe

# psql> VACUUM FULL;

countries = "FIJI TONGA VANUATU COOK_ISLANDS SAMOA"

# Create your models here.


class Building(models.Model):
    #
    validated = models.BooleanField(default=False)
    published = models.BooleanField(default=False, editable=True)
    country_type = models.TextChoices("country_type", countries)
    country = models.CharField(
        blank=True, choices=country_type.choices, max_length=255)
    location_point = models.PointField(blank=True, null=True)
    surveyor = models.CharField(
        max_length=255, blank=True, null=True)
    #location_line = models.MultiLineStringField(blank=True, null=True)
    location_polygon = models.PolygonField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    
    photo_1 = models.ImageField(
        upload_to='photos', blank=True, null=True, max_length=6544444)
    photo_2 = models.ImageField(
        upload_to='photos', blank=True, null=True, max_length=6544444)
    photo_3 = models.ImageField(
        upload_to='photos', blank=True, null=True, max_length=6544444)
    photo_4 = models.ImageField(
        upload_to='photos', blank=True, null=True, max_length=6544444)
    #
    usage_occupancy_class_type = models.TextChoices(
        'usage_occupancy_class_type', 'RESIDENTIAL COMMERCIAL INDUSTRIAL PUBLIC EDUCATIONAL INSTITUTIONAL EVACUATION_CENTER OUT_BUILDING INFRASTRUCTURE OTHER')
    usage_occupancy_class = models.CharField(
        blank=True, choices=usage_occupancy_class_type.choices, max_length=255, null=True)
    subuse_type = models.TextChoices(
        'subuse_type', 'RESIDENTIAL COMMERCIAL INDUSTRIAL PUBLIC EDUCATIONAL INSTITUTIONAL STORAGE EVACUATION_CENTER NONE OTHER')
    subuse = models.CharField(
        blank=True, choices=subuse_type.choices, max_length=255, null=True)
    foundation_type_type = models.TextChoices(
        'foundation_type_type', 'CONCRETE_SLAB WOODEN_CONCRETE_PILE STEEL_PIPE WOODEN_STEEL_POLE CONCRETE_COLUMNS LOAD_BEARING_WALL STEEL_COLUMN UNKNOWN')
    foundation_type = models.CharField(
        blank=True, choices=foundation_type_type.choices, max_length=255, null=True)
    foundation_bracing_type = models.TextChoices(
        'foundation_bracing_type', 'TIMBER_WALLS CONCRETE_WALL MASONRY PARTIAL_BRACING OTHER_(STEEL_SHEET__TIMBER_STRUTS) NONE UNKNOWN')
    foundation_bracing = models.CharField(
        blank=True, choices=foundation_bracing_type.choices, max_length=255, null=True)
    foundation_condition_type = models.TextChoices(
        'foundation_condition_type', '5_EXCELLENT_CONDITION 4_GOOD_CONDITION 3_FAIR_CONDITION 2_POOR_CONDITION 1_VERY_POOR_CONDITION')
    foundation_condition = models.CharField(
        blank=True, choices=foundation_condition_type.choices, max_length=255, null=True)
    min_floor_height_above_ground_type = models.TextChoices(
        'min_floor_height_above_ground_type', '<1.0M_(25CM_INCREMENT) >1.0M_(50CM_INCREMENT)')
    min_floor_height_above_ground = models.CharField(
        blank=True, choices=min_floor_height_above_ground_type.choices, max_length=255, null=True)
    max_floor_height_above_ground_type = models.TextChoices(
        'max_floor_height_above_ground_type', '<1.0M_(25CM_INCREMENT) >1.0M_(50CM_INCREMENT)')
    max_floor_height_above_ground = models.CharField(
        blank=True, choices=max_floor_height_above_ground_type.choices, max_length=255, null=True)
    building_structure_type = models.TextChoices(
        'building_structure_type', 'TIMBER_FRAME WOODEN_POLE CONCRETE_COLUMNS STEEL_COLUMN LOAD_BEARING_WALL TILT_UP_SLAB UNKNOWN_OTHER')
    building_structure = models.CharField(
        blank=True, choices=building_structure_type.choices, max_length=255, null=True)
    wall_material_type = models.TextChoices(
        'wall_material_type', 'CONCRETE MASONRY METAL_SHEET FIBRE_CEMENT_SHEETS UNKNOWN_SHEET FIBRE_CEMENT_BOARD TIMBER_BOARD UNKNOWN_BOARD TRADITIONAL_MATERIAL OTHER NONE_(NO_WALLS)')
    wall_material = models.CharField(
        blank=True, choices=wall_material_type.choices, max_length=255, null=True)
    wall_condition_type = models.TextChoices(
        'wall_condition_type', '5_EXCELLENT_CONDITION 4_GOOD_CONDITION 3_FAIR_CONDITION 2_POOR_CONDITION 1_VERY_POOR_CONDITION')
    wall_condition = models.CharField(
        blank=True, choices=wall_condition_type.choices, max_length=255, null=True)
    window_type_type = models.TextChoices(
        'window_type_type', 'AWNING_WINDOWS LOUVRES BAY_RECTANGLE_WINDOWS BOW_(OUTWARD_PROJECTED)_WINDOWS OTHERS')
    window_type = models.CharField(
        blank=True, choices=window_type_type.choices, max_length=255, null=True)
    window_protection_type = models.TextChoices(
        'window_protection_type', 'YES NO')
    window_protection = models.CharField(
        blank=True, choices=window_protection_type.choices, max_length=255, null=True)
    roof_shape_type = models.TextChoices(
        'roof_shape_type', 'MONO_PITCH ARCH GABLE HIP OTHER')
    roof_shape = models.CharField(
        blank=True, choices=roof_shape_type.choices, max_length=255, null=True)
    roof_material_type = models.TextChoices(
        'roof_material_type', 'CONCRETE METAL_SHEET FIBRE_CEMENT_SHEETS UNKNOWN_SHEET METAL_TILES HEAVY_TILES WOODEN_SHAKES TRADITIONAL_MATERIALS OTHER')
    roof_material = models.CharField(
        blank=True, choices=roof_material_type.choices, max_length=255, null=True)
    roof_pitch_type = models.TextChoices(
        'roof_pitch_type', 'FLAT LOW MODERATE STEEP')
    roof_pitch = models.CharField(
        blank=True, choices=roof_pitch_type.choices, max_length=255, null=True)
    roof_condition_type = models.TextChoices(
        'roof_condition_type', '5_EXCELLENT_CONDITION 4_GOOD_CONDITION 3_FAIR_CONDITION 2_POOR_CONDITION 1_VERY_POOR_CONDITION')
    roof_condition = models.CharField(
        blank=True, choices=roof_condition_type.choices, max_length=255, null=True)
    building_year_type = models.TextChoices(
        'building_year_type', 'NEW_(0_5_YRS) MEDIUM_(5_20YRS) OLD_(>20YRS) UNKNOWN')
    building_year = models.CharField(
        blank=True, choices=building_year_type.choices, max_length=255, null=True)
    under_storey_level_type = models.TextChoices(
        'under_storey_level_type', 'YES NO')
    under_storey_level = models.CharField(
        blank=True, choices=under_storey_level_type.choices, max_length=255, null=True)
    utilities_type = models.TextChoices(
        'utilities_type', 'WATER ELECTRICITY TELECOMMUNICATION ELECTRICITY_SOLAR WATER_TANK')
    utilities = models.CharField(
        blank=True, choices=utilities_type.choices, max_length=255, null=True)
    number_of_storeys = models.CharField(max_length=255, blank=True, null=True)
    population_vehicle_type = models.TextChoices(
        'population_vehicle_type', 'YES NO')
    population_vehicle = models.CharField(
        blank=True, choices=population_vehicle_type.choices, max_length=255, null=True)
    population_telecommunication_access_type = models.TextChoices(
        'population_telecommunication_access_type', 'CELLPHONE MOBILE VHF_RADIO INTERNET_CONNECTIVITY RADIO_(AM_FM)')
    population_telecommunication_access = models.CharField(
        blank=True, choices=population_telecommunication_access_type.choices, max_length=255, null=True)
    population_disability_type = models.TextChoices(
        'population_disability_type', 'MENTAL_DISABILITY SIGHT_DISABILITY HEARING_DISABILITY WALKING_DISABILITY')
    population_disability = models.CharField(
        blank=True, choices=population_disability_type.choices, max_length=255, null=True)
    population_employment_status = models.CharField(
        max_length=255, blank=True, null=True)
    population_number_of_people_in_the_household = models.CharField(
        max_length=255, blank=True, null=True)
    population_number_of_males = models.CharField(
        max_length=255, blank=True, null=True)
    population_number_of_female = models.CharField(
        max_length=255, blank=True, null=True)
    population_place_of_residence = models.CharField(
        max_length=255, blank=True, null=True)
    population_language = models.CharField(
        max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'Building'
        verbose_name_plural = 'Buildings'

    def __str__(self):
        return '{} Building {}'.format(self.country.capitalize(), self.id)


class UtilityWater(models.Model):
    #
    validated = models.BooleanField(default=False)
    published = models.BooleanField(default=False, editable=True)
    country_type = models.TextChoices("country_type", countries)
    country = models.CharField(
        blank=True, choices=country_type.choices, max_length=255)
    location_point = models.PointField(blank=True, null=True)
    location_line = models.MultiLineStringField(blank=True, null=True)
    location_polygon = models.PolygonField(blank=True, null=True)
    photo_1 = models.ImageField(
        upload_to='photos', blank=True, null=True, max_length=6544444)
    photo_2 = models.ImageField(
        upload_to='photos', blank=True, null=True, max_length=6544444)
    photo_3 = models.ImageField(
        upload_to='photos', blank=True, null=True, max_length=6544444)
    photo_4 = models.ImageField(
        upload_to='photos', blank=True, null=True, max_length=6544444)
    #
    asset_type_type = models.TextChoices(
        'asset_type_type', 'WATER_TANK RESEVOIR DESALINATION_PLANT PUMPING_STATION TREATMENT_PLANT DAMS WELL')
    asset_type = models.CharField(
        blank=True, choices=asset_type_type.choices, max_length=255)
    source_type_type = models.TextChoices(
        'source_type_type', 'SURFACE_WATER GROUND_WATER SEA_WATER WASTE_WATER RAIN_WATER')
    source_type = models.CharField(
        blank=True, choices=source_type_type.choices, max_length=255)
    condition_type = models.TextChoices(
        'condition_type', '5_EXCELLENT_CONDITION 4_GOOD_CONDITION 3_FAIR_CONDITION 2_POOR_CONDITION 1_VERY_POOR_CONDITION')
    condition = models.CharField(
        blank=True, choices=condition_type.choices, max_length=255)
    water_network_type = models.TextChoices('water_network_type', 'YES NO')
    water_network = models.CharField(
        blank=True, choices=water_network_type.choices, max_length=255)
    asset_ownership_type = models.TextChoices(
        'asset_ownership_type', 'PRIVATE GOVERNMENT STATE_OWNED_ENTERPRISE COMMUNITY_OWNED')
    asset_ownership = models.CharField(
        blank=True, choices=asset_ownership_type.choices, max_length=255)
    asset_material_type = models.TextChoices(
        'asset_material_type', 'PVC CONCRETE STEEL FIBRE_CEMENT EARTH_NATURAL OTHER')
    asset_material = models.CharField(
        blank=True, choices=asset_material_type.choices, max_length=255)
    covered_type = models.TextChoices('covered_type', 'YES NO')
    covered = models.CharField(
        blank=True, choices=covered_type.choices, max_length=255)
    treated_type = models.TextChoices('treated_type', 'YES NO')
    treated = models.CharField(
        blank=True, choices=treated_type.choices, max_length=255)

    class Meta:
        verbose_name = 'Utility Water'
        verbose_name_plural = 'Utility Water'

    def __str__(self):
        return '{} Utility Water {}'.format(self.country.capitalize(), self.id)


class UtilityElectricity(models.Model):
    #
    validated = models.BooleanField(default=False)
    published = models.BooleanField(default=False, editable=True)
    country_type = models.TextChoices("country_type", countries)
    country = models.CharField(
        blank=True, choices=country_type.choices, max_length=255)
    location_point = models.PointField(blank=True, null=True)
    location_line = models.MultiLineStringField(blank=True, null=True)
    location_polygon = models.PolygonField(blank=True, null=True)
    photo_1 = models.ImageField(
        upload_to='photos', blank=True, null=True, max_length=6544444)
    photo_2 = models.ImageField(
        upload_to='photos', blank=True, null=True, max_length=6544444)
    photo_3 = models.ImageField(
        upload_to='photos', blank=True, null=True, max_length=6544444)
    photo_4 = models.ImageField(
        upload_to='photos', blank=True, null=True, max_length=6544444)
    #
    asset_type_type = models.TextChoices(
        'asset_type_type', 'POWER_PLANT TRANSFORMER TOWER SUB_STATION SOLAR_FARM')
    asset_type = models.CharField(
        blank=True, choices=asset_type_type.choices, max_length=255)
    source_type_type = models.TextChoices(
        'source_type_type', 'RENEWABLE_HYDRO_SOLAR_WIND_BIOMASS_GEOTHERMAL_OTEC NON_RENEWABLE_GAS_FUEL_COAL_WOOD')
    source_type = models.CharField(
        blank=True, choices=source_type_type.choices, max_length=255)
    asset_material_type = models.TextChoices(
        'asset_material_type', 'STEEL CONCRETE STEEL_AND_CONCRETE OTHER')
    asset_material = models.CharField(
        blank=True, choices=asset_material_type.choices, max_length=255)
    transformer_type_type = models.TextChoices(
        'transformer_type_type', 'PAD___MOUNTED POLE___MOUNTED')
    transformer_type = models.CharField(
        blank=True, choices=transformer_type_type.choices, max_length=255)
    ownership_type = models.TextChoices(
        'ownership_type', 'PRIVATE GOVERNMENT STATE_OWNED_ENTERPRISE IPP_GENERATION')
    ownership = models.CharField(
        blank=True, choices=ownership_type.choices, max_length=255)

    class Meta:
        verbose_name = 'Utility Electricity'
        verbose_name_plural = 'Utility Electricity'

    def __str__(self):
        return '{} Utility Electricity {}'.format(self.country.capitalize(), self.id)


class InfrastructureFuel(models.Model):
    #
    validated = models.BooleanField(default=False)
    published = models.BooleanField(default=False, editable=True)
    country_type = models.TextChoices("country_type", countries)
    country = models.CharField(
        blank=True, choices=country_type.choices, max_length=255)
    location_point = models.PointField(blank=True, null=True)
    location_line = models.MultiLineStringField(blank=True, null=True)
    location_polygon = models.PolygonField(blank=True, null=True)
    photo_1 = models.ImageField(
        upload_to='photos', blank=True, null=True, max_length=6544444)
    photo_2 = models.ImageField(
        upload_to='photos', blank=True, null=True, max_length=6544444)
    photo_3 = models.ImageField(
        upload_to='photos', blank=True, null=True, max_length=6544444)
    photo_4 = models.ImageField(
        upload_to='photos', blank=True, null=True, max_length=6544444)
    #
    fuel_type_type = models.TextChoices(
        'fuel_type_type', 'WOOD COAL DIESEL KEROSENE GASOLINE PETROL ETHANOL PROPANE METHANE LPG')
    fuel_type = models.CharField(
        blank=True, choices=fuel_type_type.choices, max_length=255)
    fuel_asset_type_type = models.TextChoices(
        'fuel_asset_type_type', 'SERVICE_STATION STORAGE_FACILITY')
    fuel_asset_type = models.CharField(
        blank=True, choices=fuel_asset_type_type.choices, max_length=255)
    tank_material_type = models.TextChoices(
        'tank_material_type', 'STEEL WOODEN METAL_IORN CEMENT')
    tank_material = models.CharField(
        blank=True, choices=tank_material_type.choices, max_length=255)
    storage_type_type = models.TextChoices(
        'storage_type_type', 'FACILITY BUILDING_YARD UNDERGROUND_TANKS SILOS')
    storage_type = models.CharField(
        blank=True, choices=storage_type_type.choices, max_length=255)
    tenure_type = models.TextChoices(
        'tenure_type', 'PRIVATE PUBLIC STATE_OWNED_ENTERPRISE')
    tenure = models.CharField(
        blank=True, choices=tenure_type.choices, max_length=255)
    condition_type = models.TextChoices(
        'condition_type', '5_EXCELLENT_CONDITION 4_GOOD_CONDITION 3_FAIR_CONDITION 2_POOR_CONDITION 1_VERY_POOR_CONDITION')
    condition = models.CharField(
        blank=True, choices=condition_type.choices, max_length=255)
    storage_capacity = models.CharField(max_length=255)
    fuel_service_provider = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Infrastructure Fuel'
        verbose_name_plural = 'Infrastructure Fuel'

    def __str__(self):
        return '{} Infrastructure Fuel {}'.format(self.country.capitalize(), self.id)


class InfrastructureTelecommunication(models.Model):
    #
    validated = models.BooleanField(default=False)
    published = models.BooleanField(default=False, editable=True)
    country_type = models.TextChoices("country_type", countries)
    country = models.CharField(
        blank=True, choices=country_type.choices, max_length=255)
    location_point = models.PointField(blank=True, null=True)
    location_line = models.MultiLineStringField(blank=True, null=True)
    location_polygon = models.PolygonField(blank=True, null=True)
    photo_1 = models.ImageField(
        upload_to='photos', blank=True, null=True, max_length=6544444)
    photo_2 = models.ImageField(
        upload_to='photos', blank=True, null=True, max_length=6544444)
    photo_3 = models.ImageField(
        upload_to='photos', blank=True, null=True, max_length=6544444)
    photo_4 = models.ImageField(
        upload_to='photos', blank=True, null=True, max_length=6544444)
    #
    asset_condition_type = models.TextChoices(
        'asset_condition_type', '5_EXCELLENT_CONDITION 4_GOOD_CONDITION 3_FAIR_CONDITION 2_POOR_CONDITION 1_VERY_POOR_CONDITION')
    asset_condition = models.CharField(
        blank=True, choices=asset_condition_type.choices, max_length=255)
    asset_type_type = models.TextChoices(
        'asset_type_type', 'TOWER POLES SATELLITE_DISH ANTENNA MAST')
    asset_type = models.CharField(
        blank=True, choices=asset_type_type.choices, max_length=255)
    tower_height_type = models.TextChoices(
        'tower_height_type', '5M_< 5M_>_X_<_20M 20M_>')
    tower_height = models.CharField(
        blank=True, choices=tower_height_type.choices, max_length=255)
    tower_construction_material_type = models.TextChoices(
        'tower_construction_material_type', 'STEEL TIMBER CONCRETE FIBER_GLASS')
    tower_construction_material = models.CharField(
        blank=True, choices=tower_construction_material_type.choices, max_length=255)
    tower_use_type = models.TextChoices(
        'tower_use_type', 'TELECOMMUNICATIONS MOBILE_NETWORKS VHF_RADIO')
    tower_use = models.CharField(
        blank=True, choices=tower_use_type.choices, max_length=255)
    subtype_type = models.TextChoices('subtype_type', 'LATTICE TABULAR')
    subtype = models.CharField(
        blank=True, choices=subtype_type.choices, max_length=255)
    satellite_dishes_attached_type = models.TextChoices(
        'satellite_dishes_attached_type', 'YES NO')
    satellite_dishes_attached = models.CharField(
        blank=True, choices=satellite_dishes_attached_type.choices, max_length=255)
    sirens_attached_type = models.TextChoices('sirens_attached_type', 'YES NO')
    sirens_attached = models.CharField(
        blank=True, choices=sirens_attached_type.choices, max_length=255)
    antenna_attached_type = models.TextChoices(
        'antenna_attached_type', 'YES NO')
    antenna_attached = models.CharField(
        blank=True, choices=antenna_attached_type.choices, max_length=255)
    subuse = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Infrastructure Telecommunications'
        verbose_name_plural = 'Infrastructure Telecommunications'

    def __str__(self):
        return '{} Telecommunications {}'.format(self.country.capitalize(), self.id)


class InfrastructureBridge(models.Model):
    #
    validated = models.BooleanField(default=False)
    published = models.BooleanField(default=False, editable=True)
    country_type = models.TextChoices("country_type", countries)
    country = models.CharField(
        blank=True, choices=country_type.choices, max_length=255)
    location_point = models.PointField(blank=True, null=True)
    location_line = models.MultiLineStringField(blank=True, null=True)
    location_polygon = models.PolygonField(blank=True, null=True)
    photo_1 = models.ImageField(
        upload_to='photos', blank=True, null=True, max_length=6544444)
    photo_2 = models.ImageField(
        upload_to='photos', blank=True, null=True, max_length=6544444)
    photo_3 = models.ImageField(
        upload_to='photos', blank=True, null=True, max_length=6544444)
    photo_4 = models.ImageField(
        upload_to='photos', blank=True, null=True, max_length=6544444)
    #
    bridge_tenure_type = models.TextChoices(
        'bridge_tenure_type', 'PRIVATE PUBLIC STATE_OWNED_ENTERPRISE')
    bridge_tenure = models.CharField(
        blank=True, choices=bridge_tenure_type.choices, max_length=255)
    bridge_type_type = models.TextChoices(
        'bridge_type_type', 'ARCH SLAB CABLE TRUSS CULVERT CAUSEWAY FORD')
    bridge_type = models.CharField(
        blank=True, choices=bridge_type_type.choices, max_length=255)
    piles_type = models.TextChoices('piles_type', 'YES NO')
    piles = models.CharField(
        blank=True, choices=piles_type.choices, max_length=255)
    wingwall_type = models.TextChoices('wingwall_type', 'YES NO')
    wingwall = models.CharField(
        blank=True, choices=wingwall_type.choices, max_length=255)
    abutment_material_type = models.TextChoices(
        'abutment_material_type', 'STEEL_TRUSS STEEL_CONCRETE CONCRETE NONE')
    abutment_material = models.CharField(
        blank=True, choices=abutment_material_type.choices, max_length=255)
    superstructure_condition_type = models.TextChoices(
        'super-structure_condition_type', '5_EXCELLENT_CONDITION 4_GOOD_CONDITION 3_FAIR_CONDITION 2_POOR_CONDITION 1_VERY_POOR_CONDITION')
    superstructure_condition = models.CharField(
        blank=True, choices=superstructure_condition_type.choices, max_length=255)
    superstructure_materials_type = models.TextChoices(
        'superstructure_materials_type', 'STEEL TIMBER CONCRETE NONE')
    superstructure_materials = models.CharField(
        blank=True, choices=superstructure_materials_type.choices, max_length=255)
    deck_material_type = models.TextChoices(
        'deck_material_type', 'STEEL TIMBER CONCRETE OTHER')
    deck_material = models.CharField(
        blank=True, choices=deck_material_type.choices, max_length=255)
    deck_condition_type = models.TextChoices(
        'deck_condition_type', '5_EXCELLENT_CONDITION 4_GOOD_CONDITION 3_FAIR_CONDITION 2_POOR_CONDITION 1_VERY_POOR_CONDITION')
    deck_condition = models.CharField(
        blank=True, choices=deck_condition_type.choices, max_length=255)
    length = models.CharField(max_length=255)
    width = models.CharField(max_length=255)
    min_height_of_deck_to_water = models.CharField(max_length=255)
    max_height_of_deck_to_water = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Infrastructure Bridges'
        verbose_name_plural = 'Infrastructure Bridges'

    def __str__(self):
        return '{} Bridge {}'.format(self.country.capitalize(), self.id)


class InfrastructurePort(models.Model):
    #
    validated = models.BooleanField(default=False)
    published = models.BooleanField(default=False, editable=True)
    country_type = models.TextChoices("country_type", countries)
    country = models.CharField(
        blank=True, choices=country_type.choices, max_length=255)
    location_point = models.PointField(blank=True, null=True)
    #location_line = models.MultiLineStringField(blank=True, null=True)
    location_polygon = models.PolygonField(blank=True, null=True)
    photo_1 = models.ImageField(
        upload_to='photos', blank=True, null=True, max_length=6544444)
    photo_2 = models.ImageField(
        upload_to='photos', blank=True, null=True, max_length=6544444)
    photo_3 = models.ImageField(
        upload_to='photos', blank=True, null=True, max_length=6544444)
    photo_4 = models.ImageField(
        upload_to='photos', blank=True, null=True, max_length=6544444)
    #
    asset_type_type = models.TextChoices(
        'asset_type_type', 'WHARF JETTIES PIERS MARINA MILITARY')
    asset_type = models.CharField(
        blank=True, choices=asset_type_type.choices, max_length=255)
    port_use_type = models.TextChoices(
        'port_use_type', 'INTERNATIONAL DOMESTIC PRIVATE')
    port_use = models.CharField(
        blank=True, choices=port_use_type.choices, max_length=255)
    types_of_vessel_type = models.TextChoices(
        'types_of_vessel_type', 'INTERNATIONAL_CARGO_CONTAINERS INTERNATIONAL_TANKERS INTERNATIONAL_FERRIES DOMESTIC_FERRIES_AND_PASSENGER DOMESTIC_OUTBOARDS PRIVATE_YACHTS OTHER')
    types_of_vessel = models.CharField(
        blank=True, choices=types_of_vessel_type.choices, max_length=255)
    condition_of_port_type = models.TextChoices(
        'condition_of_port_type', '5_EXCELLENT_CONDITION 4_GOOD_CONDITION 3_FAIR_CONDITION 2_POOR_CONDITION 1_VERY_POOR_CONDITION')
    condition_of_port = models.CharField(
        blank=True, choices=condition_of_port_type.choices, max_length=255)
    tenure_type = models.TextChoices(
        'tenure_type', 'GOVERNMENT_OWNED COMMERCIAL PRIVATE COMMUNITY STATE_OWNED_ENTERPRISE')
    tenure = models.CharField(
        blank=True, choices=tenure_type.choices, max_length=255)
    construction_material_type = models.TextChoices(
        'construction_material_type', 'STEEL_REINFORCEMENT CONCRETE STEEL TIMBER OTHER')
    construction_material = models.CharField(
        blank=True, choices=construction_material_type.choices, max_length=255)
    decking_type = models.TextChoices(
        'decking_type', 'CONCRETE STEEL TIMBER ASPHALT')
    decking = models.CharField(
        blank=True, choices=decking_type.choices, max_length=255)
    seawall_type_type = models.TextChoices(
        'seawall_type_type', 'BREAK_WATER GROYNE ETC')
    seawall_type = models.CharField(
        blank=True, choices=seawall_type_type.choices, max_length=255)
    number_of_tug_boats = models.CharField(max_length=255)
    length_of_birth = models.CharField(max_length=255)
    width_of_apron = models.CharField(max_length=255)
    port_vessel_capacity = models.CharField(max_length=255)
    port_storage_capacity = models.CharField(max_length=255)
    seawall_length = models.CharField(max_length=255)
    replacement_cost = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Infrastructure Ports'
        verbose_name_plural = 'Infrastructure Ports'

    def __str__(self):
        return '{} Port {}'.format(self.country.capitalize(), self.id)


class InfrastructureAirPort(models.Model):
    #
    validated = models.BooleanField(default=False)
    published = models.BooleanField(default=False, editable=True)
    country_type = models.TextChoices("country_type", countries)
    country = models.CharField(
        blank=True, choices=country_type.choices, max_length=255)
    location_point = models.PointField(blank=True, null=True)
    location_line = models.MultiLineStringField(blank=True, null=True)
    location_polygon = models.PolygonField(blank=True, null=True)
    photo_1 = models.ImageField(
        upload_to='photos', blank=True, null=True, max_length=6544444)
    photo_2 = models.ImageField(
        upload_to='photos', blank=True, null=True, max_length=6544444)
    photo_3 = models.ImageField(
        upload_to='photos', blank=True, null=True, max_length=6544444)
    photo_4 = models.ImageField(
        upload_to='photos', blank=True, null=True, max_length=6544444)
    #
    use_type = models.TextChoices('use_type', 'INTERNATIONAL DOMESTIC PRIVATE')
    use = models.CharField(
        blank=True, choices=use_type.choices, max_length=255)
    navigation_light_system_type = models.TextChoices(
        'navigation_light_system_type', 'YES NO')
    navigation_light_system = models.CharField(
        blank=True, choices=navigation_light_system_type.choices, max_length=255)
    security_fence_type = models.TextChoices(
        'security_fence_type', 'YES NO PARTIALLY_FENCED')
    security_fence = models.CharField(
        blank=True, choices=security_fence_type.choices, max_length=255)
    surface_type = models.TextChoices(
        'surface_type', 'CONCRETE ASPHALT GRASSED')
    surface = models.CharField(
        blank=True, choices=surface_type.choices, max_length=255)
    surface_type = models.TextChoices(
        'surface_type', 'CONCRETE ASPHALT GRASSED')
    surface = models.CharField(
        blank=True, choices=surface_type.choices, max_length=255)
    surface_type = models.TextChoices(
        'surface_type', 'CONCRETE ASPHALT GRASSED')
    surface = models.CharField(
        blank=True, choices=surface_type.choices, max_length=255)
    name_of_airport_airstrip = models.CharField(max_length=255)
    length_of_runaway = models.CharField(max_length=255)
    averaged_width_of_runway = models.CharField(max_length=255)
    length_of_taxiway = models.CharField(max_length=255)
    averaged_width_of_taxiway = models.CharField(max_length=255)
    apron_area = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Infrastructure Aerial'
        verbose_name_plural = 'Infrastructure Aerial'

    def __str__(self):
        return '{} Airport {}'.format(self.country.capitalize(), self.id)


class InfrastructureRoads(models.Model):
    #
    validated = models.BooleanField(default=False)
    published = models.BooleanField(default=False, editable=True)
    country_type = models.TextChoices("country_type", countries)
    country = models.CharField(
        blank=True, choices=country_type.choices, max_length=255)
    location_point = models.PointField(blank=True, null=True)
    location_line = models.MultiLineStringField(blank=True, null=True)
    location_polygon = models.PolygonField(blank=True, null=True)
    photo_1 = models.ImageField(
        upload_to='photos', blank=True, null=True, max_length=6544444)
    photo_2 = models.ImageField(
        upload_to='photos', blank=True, null=True, max_length=6544444)
    photo_3 = models.ImageField(
        upload_to='photos', blank=True, null=True, max_length=6544444)
    photo_4 = models.ImageField(
        upload_to='photos', blank=True, null=True, max_length=6544444)
    #
    road_class_type = models.TextChoices(
        'road_class_type', 'MAIN_ROAD SECONDARY_ROAD_STREET HIGHWAY')
    road_class = models.CharField(
        blank=True, choices=road_class_type.choices, max_length=255)
    surface_seal_type = models.TextChoices(
        'surface_seal_type', 'GRAVEL EARTH SEAL ASPHALT CHIPPED_SEAL CONCRETE')
    surface_seal = models.CharField(
        blank=True, choices=surface_seal_type.choices, max_length=255)
    condition_type = models.TextChoices(
        'condition_type', '5_EXCELLENT_CONDITION 4_GOOD_CONDITION 3_FAIR_CONDITION 2_POOR_CONDITION 1_VERY_POOR_CONDITION')
    condition = models.CharField(
        blank=True, choices=condition_type.choices, max_length=255)
    location_of_road_type = models.TextChoices(
        'location_of_road_type', 'URBAN RURAL')
    location_of_road = models.CharField(
        blank=True, choices=location_of_road_type.choices, max_length=255)
    evacuation_road_type = models.TextChoices('evacuation_road_type', 'YES NO')
    evacuation_road = models.CharField(
        blank=True, choices=evacuation_road_type.choices, max_length=255)
    footpath_presence_type = models.TextChoices(
        'footpath_presence_type', 'YES NO')
    footpath_presence = models.CharField(
        blank=True, choices=footpath_presence_type.choices, max_length=255)
    traffic_volume_type = models.TextChoices(
        'traffic_volume_type', 'LIGHT_(<100_VEHICLES_PER_DAY) MEDIUM_(100_1000_VEH_DAY) HIGH_(>1000_VEH_DAY)')
    traffic_volume = models.CharField(
        blank=True, choices=traffic_volume_type.choices, max_length=255)
    terrain_type = models.TextChoices(
        'terrain_type', 'FLAT ROLLING(SMALL_HILLS) STEEP MOUNTAINOUS')
    terrain = models.CharField(
        blank=True, choices=terrain_type.choices, max_length=255)
    number_of_lanes = models.CharField(max_length=255)
    year_constructed = models.CharField(max_length=255)
    length = models.CharField(max_length=255)
    width = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Infrastructure Roads'
        verbose_name_plural = 'Infrastructure Roads'

    def __str__(self):
        return '{} Roads {}'.format(self.country.capitalize(), self.id)


class CropsAgriculture(models.Model):
    #
    validated = models.BooleanField(default=False)
    published = models.BooleanField(default=False, editable=True)
    country_type = models.TextChoices("country_type", countries)
    country = models.CharField(
        blank=True, choices=country_type.choices, max_length=255)
    location_point = models.PointField(blank=True, null=True)
    #location_line = models.MultiLineStringField(blank=True, null=True)
    location_polygon = models.PolygonField(blank=True, null=True)
    photo_1 = models.ImageField(
        upload_to='photos', blank=True, null=True, max_length=6544444)
    photo_2 = models.ImageField(
        upload_to='photos', blank=True, null=True, max_length=6544444)
    photo_3 = models.ImageField(
        upload_to='photos', blank=True, null=True, max_length=6544444)
    photo_4 = models.ImageField(
        upload_to='photos', blank=True, null=True, max_length=6544444)
    #
    crop_type_type = models.TextChoices(
        'crop_type_type', 'ROOT_CROP FRUIT_TREE')
    crop_type = models.CharField(
        blank=True, choices=crop_type_type.choices, max_length=255)
    land_tenure_type = models.TextChoices(
        'land_tenure_type', 'PRIVATE PUBLIC STATE_OWNED_ENTERPRISED')
    land_tenure = models.CharField(
        blank=True, choices=land_tenure_type.choices, max_length=255)
    planting_method_type = models.TextChoices(
        'planting_method_type', 'MONO_CULTURE MIXED SHIFTING UNKNOWN')
    planting_method = models.CharField(
        blank=True, choices=planting_method_type.choices, max_length=255)
    farmers_classification_type = models.TextChoices(
        'farmers_classification_type', 'COMMERCIAL SEMI_COMMERCIAL SUBSISTENCE')
    farmers_classification = models.CharField(
        blank=True, choices=farmers_classification_type.choices, max_length=255)
    number_of_farm_holdings_type = models.TextChoices(
        'number_of_farm_holdings_type', 'PARTIAL_FARM_HOLDING FULL_FARM_HOLDING')
    number_of_farm_holdings = models.CharField(
        blank=True, choices=number_of_farm_holdings_type.choices, max_length=255)
    fertilizer_type = models.TextChoices(
        'fertilizer_type', 'ORGANIC INORGANIC UNKNOWN')
    fertilizer = models.CharField(
        blank=True, choices=fertilizer_type.choices, max_length=255)
    farming_tools_type = models.TextChoices(
        'farming_tools_type', 'MECHANISATION_TRACTORS GRAZING_MACHINES TOOLS_SPADES_FORKS')
    farming_tools = models.CharField(
        blank=True, choices=farming_tools_type.choices, max_length=255)
    crop_area = models.CharField(max_length=255)
    market_value = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Agriculture Crops'
        verbose_name_plural = 'Agriculture Crops'

    def __str__(self):
        return '{} Crops {}'.format(self.country.capitalize(), self.id)


class Livestock(models.Model):
    #
    validated = models.BooleanField(default=False)
    published = models.BooleanField(default=False, editable=True)
    country_type = models.TextChoices("country_type", countries)
    country = models.CharField(
        blank=True, choices=country_type.choices, max_length=255)
    location_point = models.PointField(blank=True, null=True)
    #location_line = models.MultiLineStringField(blank=True, null=True)
    location_polygon = models.PolygonField(blank=True, null=True)
    photo_1 = models.ImageField(
        upload_to='photos', blank=True, null=True, max_length=6544444)
    photo_2 = models.ImageField(
        upload_to='photos', blank=True, null=True, max_length=6544444)
    photo_3 = models.ImageField(
        upload_to='photos', blank=True, null=True, max_length=6544444)
    photo_4 = models.ImageField(
        upload_to='photos', blank=True, null=True, max_length=6544444)
    #
    land_tenure_type = models.TextChoices(
        'land_tenure_type', 'NON_TRADITIONAL PRIVATE COMMERCIAL STATEOWNED_ENTERPRISE')
    land_tenure = models.CharField(
        blank=True, choices=land_tenure_type.choices, max_length=255)
    method_of_farming_type = models.TextChoices(
        'method_of_farming_type', 'FREE_RANGE FENCED CONFINEMENT')
    method_of_farming = models.CharField(
        blank=True, choices=method_of_farming_type.choices, max_length=255)
    farmer_classification_type = models.TextChoices(
        'farmer_classification_type', 'COMMERCIAL SEMI_COMMERCIAL SUBSISTENCE')
    farmer_classification = models.CharField(
        blank=True, choices=farmer_classification_type.choices, max_length=255)
    fence_type_type = models.TextChoices(
        'fence_type_type', 'WOODEN STEEL__WIRES STEEL_FENCE CONCRETE WOODEN_AND_STEEL_WIRES')
    fence_type = models.CharField(
        blank=True, choices=fence_type_type.choices, max_length=255)
    sheds_type = models.TextChoices(
        'sheds_type', 'MILKING_SHED PIGGERY BROILER___CHICKEN_PENS OTHER_SHEDS')
    sheds = models.CharField(
        blank=True, choices=sheds_type.choices, max_length=255)
    tools_type = models.TextChoices(
        'tools_type', 'MECHANISATION MANUAL_MARCHINES_ETC.')
    tools = models.CharField(
        blank=True, choices=tools_type.choices, max_length=255)
    number_of_livestocks = models.CharField(max_length=255)
    livestock_growth_stage = models.CharField(max_length=255)
    livestock_feed = models.CharField(max_length=255)
    fence_length = models.CharField(max_length=255)
    farm_area_size = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Agriculture Livestock'
        verbose_name_plural = 'Agriculture LiveStock'

    def __str__(self):
        return '{} Livestock {}'.format(self.country.capitalize(), self.id)
