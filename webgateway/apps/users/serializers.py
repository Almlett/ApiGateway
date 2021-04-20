"""
Autogenerate serializers file
"""
from rest_framework import serializers
from permissions.models import ProfilePermission
from django.contrib.auth.hashers import make_password
from .models import ApiUser, UserProfile, UserPermission, PasswordToken, Department, Turn, UserDepartment	# pylint: disable=relative-beyond-top-level

class UserDataSerializer(serializers.Serializer):
    """
    Serializer for
    """
    token = serializers.CharField(max_length=300, required=True)

class UserLogoutSerializer(serializers.Serializer):
    """
    Serializer for
    """
    token = serializers.CharField(max_length=300, required=True)


class UserLoginSerializer(serializers.Serializer):
    """
    Serializer for
    """
    email = serializers.CharField(max_length=300, required=True)
    password = serializers.CharField(required=True, write_only=True)


class ChangePasswordSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint.
    """
    token = serializers.CharField(required=True)
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class ResetPasswordSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint.
    """
    token = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class PasswordTokenSerializer(serializers.ModelSerializer):
    """
    Serializer for
    """
    class Meta: #pylint: disable=too-few-public-methods
        """
        Serializer for
        """
        model = PasswordToken
        fields = '__all__'
        read_only_fields = ['key','created_at']


class ApiUserSerializer(serializers.ModelSerializer):
    """
    ApiUser Serialzier
    """
    permissions = serializers.SerializerMethodField()

    class Meta: 	# pylint: disable=too-few-public-methods
        """
        Select all fields from model ApiUser
        """

        model = ApiUser
        fields = '__all__'
        read_only_fields = ['last_login', 'groups','user_permissions']
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(ApiUserSerializer, self).create(validated_data)

    @staticmethod
    def get_permissions(obj, type = "all"):
        """
        type = all, frontend, backend
        categorized = true, false
        """
        user_permissions = UserPermission.objects.filter(user=obj)
        user_profiles = UserProfile.objects.filter(user=obj)
        result = []
        for perm in user_permissions:
            if type == "query":
                result.append(perm.permission)
            else:
                temp = {}
                temp['id'] = perm.permission.id
                temp['name'] = perm.permission.name
                temp['key'] = perm.permission.key
                #temp['api'] = perm.permission.api
                temp['description'] = perm.permission.description
                temp['type'] = perm.permission.type
                temp['enabled'] = False if not perm.enabled else perm.permission.enabled
                temp['profile'] = "extra permission"
                result.append(temp)

        for u_profile in user_profiles:
            enabled_perm = u_profile.enabled
            objects = ProfilePermission.objects.filter(profile=u_profile.profile)
            for perm in objects:
                if enabled_perm:
                    enabled_perm = u_profile.profile.enabled
                temp = {}
                if type == "query":
                    result.append(perm.permission)
                else:
                    temp['id'] = perm.permission.id
                    temp['name'] = perm.permission.name
                    temp['key'] = perm.permission.key
                    #temp['api'] = perm.permission.api
                    temp['description'] = perm.permission.description
                    temp['type'] = perm.permission.type
                    temp['enabled'] = False if not enabled_perm else perm.permission.enabled
                    temp['profile'] = u_profile.profile.name
                    result.append(temp)
        return result


class UserProfileSerializer(serializers.ModelSerializer):
    """
    UserProfile Serialzier
    """

    class Meta: 	# pylint: disable=too-few-public-methods
        """
        Select all fields from model UserProfile
        """

        model = UserProfile
        fields = '__all__'


class UserPermissionSerializer(serializers.ModelSerializer):
    """
    UserPermission Serialzier
    """

    class Meta: 	# pylint: disable=too-few-public-methods
        """
        Select all fields from model UserPermission
        """

        model = UserPermission
        fields = '__all__'


class UserDepartmentSerializer(serializers.ModelSerializer):
    """
    UserDepartment Serialzier
    """

    class Meta: 	# pylint: disable=too-few-public-methods
        """
        Select all fields from model UserDepartment
        """

        model = UserDepartment
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    """
    Department Serialzier
    """

    class Meta: 	# pylint: disable=too-few-public-methods
        """
        Select all fields from model Department
        """

        model = Department
        fields = '__all__'


class TurnSerializer(serializers.ModelSerializer):
    """
    Turn Serialzier
    """

    class Meta: 	# pylint: disable=too-few-public-methods
        """
        Select all fields from model Turn
        """

        model = Turn
        fields = '__all__'
