"""
Reports application serializers
"""

from rest_framework import serializers

from reports.models import HappinessReportModel


class HappinessReportModelSerializer(serializers.ModelSerializer):
    """Happiness report model serializer"""

    class Meta:
        model = HappinessReportModel
        fields = "level", "reporter"


class AnnotatedHappinessReportSerializer(serializers.Serializer):
    """Annotated happiness reports serializer"""

    date = serializers.DateField()
    team_id = serializers.IntegerField()
    team = serializers.CharField()
    avg = serializers.FloatField(source="level")
    avg_prev = serializers.FloatField(source="prev")

    def create(self, validated_data):
        raise NotImplementedError("Operation is restricted")

    def update(self, instance, validated_data):
        raise NotImplementedError("Operation is restricted")
