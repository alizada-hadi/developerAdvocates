from rest_framework import serializers
from .models import Company, SocialAccount, Advocate


class CompanyShortInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class SocialAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialAccount
        fields = ['name', 'account_url', 'member_since']


class AdvocateSerializer(serializers.ModelSerializer):
    social_links = serializers.SerializerMethodField(read_only=True)
    company = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Advocate
        fields = ['id', 'name', 'short_bio', 'long_bio', 'years_of_exp', 'profile_pic','company', 'social_links']

    def get_social_links(self, obj):
        links = obj.socialaccount_set.all()
        serializer = SocialAccountSerializer(links, many=True)
        return serializer.data

    def get_company(self,obj):
        company = obj.company
        serializer = CompanyShortInfoSerializer(company, many=False)
        return serializer.data


class CompanySerializer(serializers.ModelSerializer):
    advocates = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Company
        fields = ['id', 'name', 'about', 'address', 'logo', 'advocates']

    def get_advocates(self, obj):
        advocates = obj.advocate_set.all()
        serializer = AdvocateSerializer(advocates, many=True)
        return serializer.data


