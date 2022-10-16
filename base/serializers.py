from rest_framework import serializers
from .models import Branch, Company, SocialAccount, Advocate, Project, Skill, Tech

# ? Serializing the models

# First we serialize our skill models

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'title', 'description', 'level_of_mastery']

# 2. techs/tools serializer
class TechSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tech
        fields = ['id','tech']

# 3. project serializer
class ProjectSerializer(serializers.ModelSerializer):
    techs = serializers.SerializerMethodField(read_only=True)
    number_of_likes = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'sample_photo', 'likes', 'created_at', 'techs', 'number_of_likes']

    def get_techs(self, obj):
        techs = obj.tech_set.all()
        return TechSerializer(techs, many=True).data

    def get_number_of_likes(self, obj):
        return obj.likes.all().count()

        


# 4. company branches serializer
class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['id', 'branch_name', 'address', 'created_at']

# 5. company short info serializer
class CompanyShortInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


# 6. social accounts serializer
class SocialAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialAccount
        fields = ['name', 'account_url', 'member_since']

# 7. advocate serializer
class AdvocateSerializer(serializers.ModelSerializer):
    social_links = serializers.SerializerMethodField(read_only=True)
    company = serializers.SerializerMethodField(read_only=True)
    projects = serializers.SerializerMethodField(read_only=True)
    skills = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Advocate
        fields = ['id', 'name', 'short_bio', 'long_bio', 'years_of_exp', 'profile_pic','company', 'social_links', 'projects', 'skills']

    def get_social_links(self, obj):
        links = obj.socialaccount_set.all()
        serializer = SocialAccountSerializer(links, many=True)
        return serializer.data

    def get_company(self,obj):
        company = obj.company
        serializer = CompanyShortInfoSerializer(company, many=False)
        return serializer.data

    def get_projects(self, obj):
        projects = obj.project_set.all()
        return ProjectSerializer(projects, many=True).data

    def get_skills(self, obj):
        skills = obj.skill_set.all()
        return  SkillSerializer(skills, many=True).data

# 8. company seriliazer
class CompanySerializer(serializers.ModelSerializer):
    advocates = serializers.SerializerMethodField(read_only=True)
    branches = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Company
        fields = ['id', 'name', 'about', 'address', 'logo', 'branches', 'advocates']

    def get_advocates(self, obj):
        advocates = obj.advocate_set.all()
        serializer = AdvocateSerializer(advocates, many=True)
        return serializer.data

    def get_branches(self, obj):
        branches = obj.branch_set.all()
        return BranchSerializer(branches, many=True).data


