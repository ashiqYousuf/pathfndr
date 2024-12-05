import datetime

from rest_framework import serializers


class FlightSearchAPISerializer(serializers.Serializer):
    org_code = serializers.CharField(max_length=10)
    dest_code = serializers.CharField(max_length=10)
    depart_date = serializers.CharField(max_length=12)
    num_adults = serializers.IntegerField(min_value=1)
    no_cache = serializers.IntegerField(default=0)

    def validate(self, attrs):
        """
        perform all the necessary validation checks at the serialization level
        """
        try:
            _ = datetime.datetime.strptime(attrs['depart_date'], '%Y-%m-%d')
        except ValueError:
            raise serializers.ValidationError(
                "depart_date must be of the format 'YYYY-MM-DD'")
        return super().validate(attrs)
