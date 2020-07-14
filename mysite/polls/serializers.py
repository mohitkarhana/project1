from rest_framework import serializers

from polls.models  import *

class StudentSerializer(serializers.Serializer):
	class Meta:
		models = Student
		fields = '__all__'


class DoubtSerializer(serializers.Serializer):
	class Meta:
		model = Doubt
		fields = '__all__'
