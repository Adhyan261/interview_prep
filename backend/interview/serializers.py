from rest_framework import serializers
from .models import InterviewExperience
from questions.serializers import QuestionSerializer
from questions.models import QuestionModel
from django.utils.translation import gettext_lazy as _
from company.models import Company

class InterviewReadSerilizer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField()
    company = serializers.SerializerMethodField()
    interview_questions = QuestionSerializer(many = True,read_only=True)
    total_questions = serializers.SerializerMethodField()

    class Meta:
        model = InterviewExperience
        fields = ('id','user','company','position','interview_date','interview_round','rating','total_questions','interview_questions','created_at')


    def get_company(self,instance):
        return instance.company.name  

    def get_total_questions(self,instance):
        return int(instance.interview_questions.count())

    def get_user(self,instance):
        return instance.user.username


class InterviewWriteSerilizer(serializers.ModelSerializer):

    company = serializers.CharField()
    user = serializers.SerializerMethodField()
    total_questions = serializers.SerializerMethodField()
    interview_questions = QuestionSerializer(many = True)
    class Meta:
        model = InterviewExperience
        fields = ('id','user','company','position','interview_date','interview_round','rating','total_questions','interview_questions','created_at')
        read_only_fields = ('user',)

    def get_user(self, instance):
        return instance.user.id


    def create(self,validated_data):
        company_data = validated_data.pop('company')
        if not (Company.objects.filter(name = company_data).exists()) :
            Company.objects.create(name = company_data)
        company_id = Company.objects.get(name=company_data)
        
        questions_data = validated_data.pop('interview_questions')
        interview = InterviewExperience.objects.create(company = company_id,**validated_data)
        for question_data in questions_data:
            QuestionModel.objects.create(interview=interview,user=interview.user,company = company_id,**question_data)
        return interview

    def update(self, instance, validated_data):

        questions_data = validated_data.pop('interview_questions')
        instance.position = validated_data.get('position',instance.position)
        instance.interview_date = validated_data.get('interview_date',instance.interview_date)
        instance.interview_round = validated_data.get('interview_round',instance.interview_round)
        instance.rating = validated_data.get('rating',instance.rating)
            
        for question_data in questions_data:
            question, _ = QuestionModel.objects.get_or_create(interview=instance,user=instance.user,company = instance.company ,**question_data)
            question.save()
        
        instance.save()
        return instance

    def get_total_questions(self,instance):
        return int(instance.interview_questions.count())
        
