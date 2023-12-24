from django.shortcuts import render

# Create your views here.
# mldeployment/views.py
from django.shortcuts import render
from .forms import CarForm
# from .your_ml_module import predict_price  # Import your machine learning module
import joblib
import pandas as pd

def predict_car_price(request):
    form = CarForm(request.POST or None)

    if form.is_valid():
        # Extract data from the form and pass it to your machine learning model
        input_data = form.cleaned_data
        df = pd.DataFrame([input_data])

        loaded_model = joblib.load('static/mldeployment/your_linear_regression_model_1.joblib')
        input_data_encoded = pd.get_dummies(df,
                                    columns=['Registration', 'Body_Type', 'Color', 'Transmission', 'Drive', 'Steering',
                                             'Condition', 'Customs', 'Availability', 'Region_City_of_Sale',
                                             'Engine_fuel_type', 'Car_make'])


        predicted_price = loaded_model.predict(input_data_encoded)
        # Add the predicted price to the form or display it in the template

    return render(request, 'mldeployment/index.html', {'form': form})