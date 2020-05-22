from rest_framework import serializers
from api.models import Match, Sport, Ground

class MatchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Match
        fields = ('game_name', 'start_time', 'sport_name', 'ground_name')

class SportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sport
        fields = ['sport_name']

class GrondSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ground
        fields = ('ground_name', 'sport')