from rest_framework import serializers
from .models import Path, Student

# First Way with Serializars
# class StudentSerializerWithSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length=30)
#     last_name = serializers.CharField(max_length=30)
#     number = serializers.IntegerField()

# Secand Way



class StudentSerializer(serializers.ModelSerializer):
    path = serializers.StringRelatedField()
    path_id = serializers.IntegerField(required=False)

    class Meta:
        model = Student
        # fields = "__all__"
        fields = ["first_name", "last_name", "number", "path", "id", "path_id"]
        # exclude = ["path"]

    def validate_last_name(self,value):
        if not value == value.upper():
            raise serializers.ValidationError("Last name should be all upper case")
        return value

class PathSerializer(serializers.ModelSerializer):
    # students = serializers.StringRelatedField(many=True)
    # students = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    students = StudentSerializer(many=True)

    class Meta:
        model = Path
        # fields = "__all__"
        fields = ["id","name","students"]
        # exclude = ["name"] 

    def create(self, validated_data):
        print(validated_data)
        students_data = validated_data.pop('students')
        path = Path.objects.create(**validated_data)
        for data in students_data:
            Student.objects.create(path_id=path.id, **data)
        return path