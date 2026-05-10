from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import IrisPrediction

class IrisPredictionAPITests(APITestCase):

    def test_create_prediction_success(self):
        """
        Skenario 1: Memastikan API berhasil menerima data yang valid, 
        menyimpan ke database, dan mengembalikan status 201 CREATED.
        """
        url = reverse('prediction-list')
        data = {
            "sepal_length": 5.1,
            "sepal_width": 3.5,
            "petal_length": 1.4,
            "petal_width": 0.2
        }
        
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(IrisPrediction.objects.count(), 1)
        self.assertIn('predicted_class', response.data) # Pastikan hasil prediksi ada di response

    def test_create_prediction_missing_field(self):
        """
        Skenario 2: Memastikan lapisan validasi Serializer bekerja dengan baik 
        saat user lupa mengirimkan salah satu parameter wajib.
        """
        url = reverse('prediction-list')
        data = {
            "sepal_length": 5.1,
            # sepal_width sengaja dihilangkan
            "petal_length": 1.4,
            "petal_width": 0.2
        }
        
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('sepal_width', response.data) # Pastikan error spesifik pada field yang hilang

    def test_get_prediction_list(self):
        """
        Skenario 3: Memastikan endpoint GET merespons dengan struktur JSON 
        yang benar dan membungkus data dengan key 'predictions'.
        """
        url = reverse('prediction-list')
        response = self.client.get(url, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('predictions', response.data)