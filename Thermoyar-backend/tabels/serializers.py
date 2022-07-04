from rest_framework import serializers
from .models import superheat, sub_cold, saturate, material, state

class materialSerializer(serializers.ModelSerializer):
    class Meta:
        model = material
        fields = ('material_name')

class stateSerializer(serializers.ModelSerializer):
    class Meta:
        model = state
        fields = ('state_name')

class superheatserializer(serializers.ModelSerializer):
    class Meta:
        model = superheat
        fields = ('state_n_id', 'material_n_id', 'temp', 'pres', 'vol', 'eng', 'antal', 'ant')


class sub_coldserializer(serializers.ModelSerializer):
    class Meta:
        model = sub_cold
        fields = ('state_n_id', 'material_n_id', 'temp', 'pres', 'vol', 'eng', 'antal', 'ant')


class saturateserializer(serializers.ModelSerializer):
    class Meta:
        model = saturate
        fields = ('state_n_id', 'material_n_id', 'temp', 'pres', 'vol_f', 'vol_fg', 'vol_g', 'eng_f', 'eng_fg', 'eng_g',
                  'antal_fe', 'antal_fg', 'antal_g', 'ant_f', 'ant_fg', 'ant_g')
