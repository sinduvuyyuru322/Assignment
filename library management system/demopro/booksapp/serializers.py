from rest_framework import serializers
from .models import Books
class BookSerailizers(serializers.ModelSerializer):
    class Meta:
        model=Books
        fields=['id','Title','Author','Year','Genre']