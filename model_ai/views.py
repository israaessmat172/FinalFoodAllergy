from django.shortcuts import render

from django.shortcuts import render
from .utils import load_model
from .models import ImageClassification
from database.models import Category
import numpy as np
from keras.preprocessing import image

def predict(request):
    if request.method == 'POST':
        model = load_model('model_name.h5')
        img_file = request.FILES['image']
        img = image.load_img(img_file, target_size=(224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        prediction = model.predict(x)

        # Save the image classification result to the database
        category_id = np.argmax(prediction)
        category = Category.objects.get(pk=category_id)
        result = ImageClassification.objects.create(image=img_file, category=category, result='')

        # Retrieve the allergy information associated with the category
        allergies = category.allergy.all()
        allergy_names = [allergy.arabicName for allergy in allergies]
        result.result = ', '.join(allergy_names)
        result.save()

        # Return the prediction and allergy information to the user
        return render(request, 'prediction.html', {'prediction': prediction, 'allergies': allergy_names})
    else:
        return render(request, 'temp.html')
