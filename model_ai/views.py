# from keras.models import load_model
# # from django.http import JsonResponse
# from keras.applications.imagenet_utils import preprocess_input
# from keras.preprocessing import image
# import numpy as np
# # import os
# # from rest_framework.decorators import api_view
# # from rest_framework.response import Response
# from .serializers import CategorySerializer
# from database.models import Food, Category




# from django.shortcuts import get_object_or_404
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework.views import APIView


# class PredictView(APIView):
#     # permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         queryset = Category.objects.all()
#         return queryset

#     def post(self, request):
#         model = load_model('model_ai/model.h5')
#         img_path = request.FILES['image']
#         img = image.load_img(img_path, target_size=(224, 224))
#         x = image.img_to_array(img)
#         c = np.expand_dims(x, axis=0)
#         x = preprocess_input(x)
#         prediction = model.predict(x)
#         food = Food.objects.filter(englishName=prediction)[0]
#         category = get_object_or_404(self.get_queryset(), food=food)
#         serializer = CategorySerializer(category)
#         return Response(serializer.data)

 









# from django.http import JsonResponse
# from django.shortcuts import get_object_or_404
# from django.views.decorators.csrf import csrf_exempt
# from keras.applications.imagenet_utils import preprocess_input
# from keras.preprocessing import image
# from rest_framework.decorators import api_view
# from database.models import Category, Food, Allergy
# import numpy as np
# import os
# from keras.models import load_model

# # Load the Keras model
# model = load_model('model_ai/model.h5')

# @csrf_exempt
# @api_view(['POST'])
# def predict_food(request):
# # Load the image
#     img_file = request.FILES.get('image', None)
#     if img_file is None:
#         return JsonResponse({'error': 'Image file is missing.'}, status=400)
#     img = image.load_img(img_file, target_size=(224, 224))
#     x = image.img_to_array(img)
#     x = preprocess_input(x)
#     x = np.expand_dims(x, axis=0)

# # Make the prediction
#     preds = model.predict(x)
#     food_type = np.argmax(preds)

# # Get the food name and associated allergies
#     food_name = Food.objects.get(id=food_type)
#     category = get_object_or_404(Category, food=food_name)
#     allergies = category.allergy.all()

# # Return the list of allergies
#     allergy_list = [{'arabicName': allergy.arabicName, 'englishName': allergy.englishName} for allergy in allergies]
#     return JsonResponse({'food_type': food_name.englishName, 'allergies': allergy_list})
