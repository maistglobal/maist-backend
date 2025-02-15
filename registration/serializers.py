from rest_framework import serializers
from .models import TechProvider, TechSeeker
import re

class TechProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechProvider
        fields = '__all__'

    def validate_primary_email(self, value):
        domain_pattern = r'^[a-zA-Z0-9._%+-]+@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})$'
        personal_domains = ['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com','yopmail.com']

        match = re.match(domain_pattern, value)
        if not match:
            raise serializers.ValidationError("Invalid email format.")

        domain = match.group(1)
        if domain in personal_domains:
            raise serializers.ValidationError("Only company domain emails are allowed.")

        if TechProvider.objects.filter(primary_email=value).exists():
            raise serializers.ValidationError("This email is already registered.")

        return value

    def validate_linkedin_link(self, value):
        linkedin_pattern = r'^https:\/\/(www\.)?linkedin\.com\/.*$'
        if not re.match(linkedin_pattern, value):
            raise serializers.ValidationError("Invalid LinkedIn profile URL.")
        return value

class TechSeekerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechSeeker
        fields = '__all__'

    def validate_email(self, value):
        domain_pattern = r'^[a-zA-Z0-9._%+-]+@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})$'
        personal_domains = ['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com']

        match = re.match(domain_pattern, value)
        if not match:
            raise serializers.ValidationError("Invalid email format.")

        domain = match.group(1)
        if domain in personal_domains:
            raise serializers.ValidationError("Only official company emails are allowed.")

        if TechSeeker.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already registered.")

        return value

    def validate_linkedin_link(self, value):
        linkedin_pattern = r'^https:\/\/(www\.)?linkedin\.com\/.*$'
        if not re.match(linkedin_pattern, value):
            raise serializers.ValidationError("Invalid LinkedIn profile URL.")
        return value

    # def validate_company_name(self, value):
    #     if not TechProvider.objects.filter(company_name=value).exists():
    #         raise serializers.ValidationError("Company does not exist. Please register as a Tech Provider first.")
    #     return value