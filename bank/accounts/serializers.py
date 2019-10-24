from rest_framework import serializers
from accounts.models import Account
from datetime import datetime
from django.utils import timezone

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('owner',
                  'balance',
                  'creation_date')
    