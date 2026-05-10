import uuid
from django.db import models

class IrisPrediction(models.Model):
    # Menggunakan UUID sebagai primary key
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sepal_length = models.FloatField()
    sepal_width = models.FloatField()
    petal_length = models.FloatField()
    petal_width = models.FloatField()
    
    # Kolom hasil prediksi
    predicted_class = models.CharField(max_length=50, blank=True, null=True)
    
    # Fitur Soft Delete
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return f"Prediction: {self.predicted_class}"