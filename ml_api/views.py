from django.shortcuts import render

# Create your views here.
import os
# pyrefly: ignore [missing-import]
import joblib
from django.conf import settings
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import IrisPredictionSerializer
from .models import IrisPrediction

# Fungsi helper untuk load model dan prediksi
def predict_machine_learning(sl, sw, pl, pw):
    CLASS_NAMES = ['Setosa', 'Versicolor', 'Virginica']
    try:
        model_path = os.path.join(settings.BASE_DIR, 'model_iris.pkl')
        model = joblib.load(model_path)
        features = [[sl, sw, pl, pw]]
        prediction_idx = model.predict(features)[0]
        return CLASS_NAMES[prediction_idx]
    except Exception:
        # Fallback jika file model.pkl belum dibuat/tidak ditemukan
        return "Unknown Error / Model Not Found"

class PredictionList(APIView):
    def post(self, request):
        note = IrisPredictionSerializer(data=request.data, context={'request': request})
        if note.is_valid(raise_exception=True):
            # Lakukan prediksi sebelum disimpan
            sl = note.validated_data['sepal_length']
            sw = note.validated_data['sepal_width']
            pl = note.validated_data['petal_length']
            pw = note.validated_data['petal_width']
            
            p_class = predict_machine_learning(sl, sw, pl, pw)
            
            # Save data beserta hasil prediksinya
            note.save(predicted_class=p_class)
            return Response(note.data, status=status.HTTP_201_CREATED)
            
        return Response(note.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        # Filter awal: Hanya prediksi yang belum di-soft delete
        predictions = IrisPrediction.objects.filter(is_delete=False)
        
        # Menggunakan serializer untuk menampilkan data
        serializer = IrisPredictionSerializer(predictions, many=True, context={'request': request})
        
        # Mengembalikan response dengan key (seperti pada OpenShop)
        return Response({
            "predictions": serializer.data
        }, status=status.HTTP_200_OK)      

class PredictionDetail(APIView):
    def get_object(self, pk):
        try:
            return IrisPrediction.objects.get(pk=pk)
        except IrisPrediction.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        prediction = self.get_object(pk)
        # Menambahkan context={'request': request} agar HATEOAS (_links) bisa merender URL dengan benar
        serializer = IrisPredictionSerializer(prediction, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        prediction = self.get_object(pk)
        serializer = IrisPredictionSerializer(prediction, data=request.data, context={'request': request})
        if serializer.is_valid():
            # Prediksi ulang jika ada perubahan parameter
            sl = serializer.validated_data.get('sepal_length', prediction.sepal_length)
            sw = serializer.validated_data.get('sepal_width', prediction.sepal_width)
            pl = serializer.validated_data.get('petal_length', prediction.petal_length)
            pw = serializer.validated_data.get('petal_width', prediction.petal_width)
            
            p_class = predict_machine_learning(sl, sw, pl, pw)
            
            serializer.save(predicted_class=p_class)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        prediction = self.get_object(pk)
        
        # Menerapkan logic Soft Delete
        prediction.is_delete = True
        prediction.save()
        
        return Response(status=status.HTTP_204_NO_CONTENT)