
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import StudentRecord


class StudentRecordSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all()
    )

    class Meta:
        model = StudentRecord
        fields = '__all__'

    def get_fields(self):
        fields = super().get_fields()

        # Prevent changing the owner after record creation.
        if self.instance is not None:
            fields['owner'].read_only = True

        return fields
