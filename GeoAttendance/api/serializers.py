from rest_framework import serializers
from .models import UserData # Import your model

class serializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = '__all__'  # ✅ Include all fields OR specify fields like ['id', 'name', 'email']
        # exclude = ['']  ye exclude karegi feild

