from rest_framework import serializers
from accounts.models import Account
from datetime import datetime
from django.utils import timezone
import json

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id',
                  'owner',
                  'balance',
                  'creation_date')

    @staticmethod
    def validate_balance(value):
        if value < 0:
            raise serializers.ValidationError("It is not allowed negative balance")
        return value

    @staticmethod
    def validate_json_creation_date(data):
        if "creation_date" in data:
            raise serializers.ValidationError("The account creation date should not be provided")
        return True

    @staticmethod
    def validate_patch(old_account_balance, account_patched):
        if not("balance" in str(account_patched)) or len(account_patched) != 1:
            raise serializers.ValidationError("Only balance should be patched")
        
        account_patched_balance = account_patched['balance']
        
        final_account_balance = old_account_balance + account_patched_balance
        if account_patched_balance > 0:
            return final_account_balance
        elif account_patched_balance < 0:
            if final_account_balance < 0:
                raise serializers.ValidationError("The patched balance should not leave the final balance negative")
            return final_account_balance
        else:
            raise serializers.ValidationError("The patched balance must not be zero")
