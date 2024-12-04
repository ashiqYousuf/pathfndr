from rest_framework import serializers


class FlightSearchAPISerializer(serializers.Serializer):
    org_code = serializers.CharField(max_length=10)
    dest_code = serializers.CharField(max_length=10)
    depart_date = serializers.CharField(max_length=12)
    num_adults = serializers.IntegerField(min_value=1)
