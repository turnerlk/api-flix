from rest_framework import serializers
from movies.models import Movie


class MovieModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

    def validate_release_date(self, value):
        if value.year < 1950:
            raise serializers.ValidationError('A data de lançamento não pode ser anterior a 1950')
        return value
    
    def validate_resume(self, value):
        if len (value)  > 200:
            raise serializers.ValidationError('Resumo não deve ser maior que 200 caracteres')
        return value