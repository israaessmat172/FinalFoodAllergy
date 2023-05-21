import pathlib
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PredictSerializer
from database.models import Food, Category
import tensorflow as tf
import numpy as np
from .serializers import *
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras import Model
import tensorflow_hub as hub
from django.conf import settings
from rest_framework import status
from tensorflow.keras.preprocessing import image
from rest_framework.permissions import IsAuthenticated
import io
from django.shortcuts import get_object_or_404
from django.http import Http404

# from rest_framework import permissions

class PredictAPIView(APIView):
    # permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticated]
      
    serializer_class = PredictSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            img = serializer.validated_data['image']
            img = img.read()  
            print("Image read from InMemoryUploadedFile.")
            img = tf.image.decode_image(img, channels=3)  
            print("Image decoded.")
            img = tf.image.resize_with_pad(img, 224, 224) 
            print("Image resized with padding.")
            img = np.array(img) / 255.0  
            print("Image pixel values normalized.")

       
            print("Loading model...")
            model = tf.keras.models.load_model('model_ai/model.h5', custom_objects={'KerasLayer': hub.KerasLayer}, compile=False)
            model.build((None, 224, 224, 3))
            print("Model loaded.")
            prediction = model.predict(np.array([img]))
            print("Prediction :", prediction)
            prediction_class = np.argmax(prediction)
            print("prediction_classsssssss:", prediction_class)
            predicted_class_index = np.argmax(prediction)
         
            class_names = ['Burger', 'Dairy product', 'Donut', 'Egg', 'Meat', 'Noodles-Pasta', 'Pizza',
            'Sandwich', 'Seafood', 'cake', 'hotDog','sushi']   

            predicted_class_name = class_names[predicted_class_index]
            print("Prediction class:", prediction_class)
            print("Prediction NAAAAMAMMMMMMMEEEEEEEEEEE:", predicted_class_name)

           
        try:
            c = Category.objects.first()
            print(c.id)
            category = get_object_or_404(Category, pk=5)
            print(category)
            food = category.food.first()
            
            allergies = category.allergy.all()
            allergy_names = [allergy.englishName for allergy in allergies]
            food_name = food.englishName
            print("Food Found:", food)
               
            data = {
                    'category_name': category.englishName,
                    'food_name': food_name,
                    'allergies': allergy_names,
                }
                
               
            print("Returning the response...")
            return Response(data, status=status.HTTP_200_OK)
            
        except Http404:
            print("Category not found.")
            return Response({'error': 'Category not found.'}, status=status.HTTP_404_NOT_FOUND)




    # def post(self, request):
    #     serializer = self.serializer_class(data=request.data)
    #     if serializer.is_valid():
    #         img = serializer.validated_data['image']
    #         img = img.read()  # extract the binary data from the InMemoryUploadedFile
    #         print("Image read from InMemoryUploadedFile.")
    #         img = tf.image.decode_image(img, channels=3)  # decode the image
    #         print("Image decoded.")
    #         img = tf.image.resize_with_pad(img, 224, 224)  # resize the image to match the input shape of the model
    #         print("Image resized with padding.")
    #         img = np.array(img) / 255.0  # normalize the pixel values to be between 0 and 1
    #         print("Image pixel values normalized.")

    #         # load the model and get the prediction
    #         print("Loading model...")
    #         model = tf.keras.models.load_model('model_ai/model.h5', custom_objects={'KerasLayer': hub.KerasLayer}, compile=False)
    #         model.build((None, 224, 224, 3))
    #         print("Model loaded.")
    #         prediction = model.predict(np.array([img]))
    #         print("Prediction :", prediction)
    #         prediction_class = np.argmax(prediction)
    #         print("prediction_classsssssss:", prediction_class)

    #         predicted_class_index = np.argmax(prediction)
    #         #####  WWWWHHHHHHATTT TTTHHHEEEEE ***** (:---:)
    #         # data_dir = pathlib.Path('/content/drive/MyDrive/New folder/train')
    #         # class_names = np.array(sorted([item.name for item in data_dir.glob('*')]))
    #         class_names = ['Burger', 'Dairy product', 'Donut', 'Egg', 'Meat', 'Noodles-Pasta', 'Pizza',
    #         'Sandwich', 'Seafood', 'cake', 'hotDog','sushi']   

    #         predicted_class_name = class_names[predicted_class_index]
    #         print("Prediction class:", prediction_class)
    #         print("Prediction NAAAAMAMMMMMMMEEEEEEEEEEE:", predicted_class_name)

    #         # look up the category in the database and serialize the response
    #         # try:
    #         #     category = Category.objects.get(pk=prediction_class)
    #         #     print("Category found:", category)
    #         #     serializer = CategorySerializer(category)

    #         try:
    #             category = get_object_or_404(Category, pk=prediction_class)
    #             print("Category found:", category)
    #             serializer = CategorySerializer(category)


    #             # get the food and allergy for the category
    #             food = category.food_set.first()
    #             food_name = food.englishName
    #             print("Food found:", food)

    #             allergies = food.allergy_set.all()
    #             allergy_names = [allergy.englishName for allergy in allergies]
    #             print("Allergies found:", allergy_names)

    #             # add food name and allergy names to the response
    #             data = serializer.data
    #             data['allergies'] = allergy_names
    #             data['food_name'] = food_name

    #             # return the response   
    #             print("Returning the response...")
    #             return Response(data, status=status.HTTP_200_OK)
    #         except Category.DoesNotExist:
    #             print("Category not found.")
    #             return Response({'error': 'Category not found.'}, status=status.HTTP_404_NOT_FOUND)


# class PredictAPIView(APIView):
#     # permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
#     queryset = Category.objects.all()
#     permission_classes = [IsAuthenticated]
      
#     serializer_class = PredictSerializer



#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             img = serializer.validated_data['image']
#             img = img.read()  # extract the binary data from the InMemoryUploadedFile
#             print("Image read from InMemoryUploadedFile.")
#             img = tf.image.decode_image(img, channels=3)  # decode the image
#             print("Image decoded.")
#             img = tf.image.resize_with_pad(img, 224, 224)  # resize the image to match the input shape of the model
#             print("Image resized with padding.")
#             img = np.array(img) / 255.0  # normalize the pixel values to be between 0 and 1
#             print("Image pixel values normalized.")

#             # load the model and get the prediction
#             print("Loading model...")
#             model = tf.keras.models.load_model('model_ai/model.h5', custom_objects={'KerasLayer': hub.KerasLayer}, compile=False)
#             model.build((None, 224, 224, 3))
#             print("Model loaded.")
#             prediction = model.predict(np.array([img]))
#             print("Prediction :", prediction)
#             prediction_class = np.argmax(prediction)
#             print("prediction_classsssssss:", prediction_class)

#             predicted_class_index = np.argmax(prediction)
#             #####  WWWWHHHHHHATTT TTTHHHEEEEE ***** (:---:)
#             # data_dir = pathlib.Path('/content/drive/MyDrive/New folder/train')
#             # class_names = np.array(sorted([item.name for item in data_dir.glob('*')]))
#             class_names = ['Burger', 'Dairy product', 'Donut', 'Egg', 'Meat', 'Noodles-Pasta', 'Pizza',
#             'Sandwich', 'Seafood', 'cake', 'hotDog','sushi']   

#             predicted_class_name = class_names[predicted_class_index]
#             print("Prediction class:", prediction_class)
#             print("Prediction NAAAAMAMMMMMMMEEEEEEEEEEE:", predicted_class_name)

#             # look up the category in the database and serialize the response
#             print("Looking up category in database...")
#             category = Category.objects.get(pk=prediction_class)
#             print("Category found:", category)
#             serializer = CategorySerializer(category)

#             # get the food and allergy for the category
#             print("Getting food and allergy for the category...")
#             food = category.food_set.first()
#             allergies = food.allergy_set.all()
#             allergy_names = [allergy.englishName for allergy in allergies]
#             # add food name to the response
#             food_name = food.englishName

#             # return the response
#             print("Returning the response...")
#             data = serializer.data
#             data['allergies'] = allergy_names
#             data['food_name'] = food_name
#             return Response(data, status=status.HTTP_200_OK)
        
#         print("Invalid input data.")
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

