from rest_framework import serializers
from .models import QuestionModel

class QuestionSerializer(serializers.ModelSerializer):

    company = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    class Meta:
        model = QuestionModel
        fields = ('interview','id','user','question','answer','category','company')
        read_only_fields = ('interview','id','user','company')

    def get_user(self,instance):
        return instance.user.username

    def get_company(self,instance):
        return instance.company.name

