from rest_framework import serializers
from .models import Profile, Experience, Skill, Education, Project, TechStack

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"
        read_only_fields = ["user", "created_at", "updated_at"]

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = "__all__"
        read_only_fields = ["user"]

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"
        read_only_fields = ["user"]

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = "__all__"
        read_only_fields = ["user"]

class ProjectSerializer(serializers.ModelSerializer):
    tech_stack = serializers.ListField(
        child=serializers.CharField(),
        write_only=True
    )

    class Meta:
        model = Project
        fields = "__all__"
        read_only_fields = ["user"]

    def create(self, validated_data):
        tech_names = validated_data.pop("tech_stack")

        project = Project.objects.create(**validated_data)

        tech_objects = []

        for name in tech_names:
            tech, created = TechStack.objects.get_or_create(
                tech_name=name.strip()
            )

            tech_objects.append(tech)

        project.tech_stack.set(tech_objects)

        return project