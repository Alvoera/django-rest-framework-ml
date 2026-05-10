from rest_framework.reverse import reverse
from rest_framework import serializers
from .models import IrisPrediction

class IrisPredictionSerializer(serializers.HyperlinkedModelSerializer):
    _links = serializers.SerializerMethodField()
    
    class Meta:
        model = IrisPrediction
        fields = [
            'id', 'sepal_length', 'sepal_width', 
            'petal_length', 'petal_width', 'predicted_class', 
            'is_delete', '_links'
        ]
        # Mencegah user mengisi class secara manual
        read_only_fields = ['predicted_class']

    def get__links(self, obj):
        request = self.context.get('request')
        
        # Mencegah error jika object belum memiliki PK saat proses inisialisasi
        if not obj.pk:
            return []
            
        return [
            {
                "rel": "self",
                "href": reverse('prediction-list', request=request),
                "action": "POST",
                "types": ["application/json"]
            },
            {
                "rel": "self",
                "href": reverse('prediction-detail', kwargs={'pk': obj.pk}, request=request),
                "action": "GET",
                "types": ["application/json"]
            },
            {
                "rel": "self",
                "href": reverse('prediction-detail', kwargs={'pk': obj.pk}, request=request),
                "action": "PUT",
                "types": ["application/json"]
            },
            {
                "rel": "self",
                "href": reverse('prediction-detail', kwargs={'pk': obj.pk}, request=request),
                "action": "DELETE",
                "types": ["application/json"]
            }
        ]