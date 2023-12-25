from django.shortcuts import render
import os
# Create your views here.
# mldeployment/views.py
from django.shortcuts import render
from .forms import CarForm
# from .your_ml_module import predict_price  # Import your machine learning module
import joblib
import pandas as pd
from django.http import HttpResponse
from sklearn.preprocessing import OneHotEncoder

def predict_car_price(request):
    context = {
                }

    # разбор по пунктам что мне надо сделать
    # 1 мне надо сделать так чтобы инпут у юзера был такой же как и данные для тренировки модели
    form = CarForm(request.POST or None)

    if form.is_valid():
        # Extract data from the form and pass it to your machine learning model

        input_data = form.cleaned_data

        user_df = pd.DataFrame([input_data])
        user_df = user_df.drop(['name_of_car'], axis=1)

        desired_order = [
            'Mileage', 'Body_Type', 'Color', 'Transmission', 'Drive', 'Steering',
            'Condition', 'Customs', 'Availability', 'Region_City_of_Sale',
            'Registration', 'Engine_volume', 'Engine_fuel_type', 'Car_make', 'Door_num'
        ]

        # Reorder the DataFrame columns
        user_df = user_df[desired_order]
        print(f' user df: {user_df}')

        with open('user_colunms.txt', 'w') as user_file:
            for col in user_df.columns:
                user_file.write(col + '\n')

        categorical_columns = [
            'Body_Type',
            'Color',
            'Transmission',
            'Drive',
            'Steering',
            'Condition',
            'Customs',
            'Availability',
            'Region_City_of_Sale',
            'Registration',
            'Engine_fuel_type',
            'Car_make'
        ]

        # encoder = OneHotEncoder(sparse=False, handle_unknown='ignore')
        # encoder.fit(user_df[categorical_columns])  # Assuming you have the same encoder fitted with your training data
        #
        # # encoded_cols = encoder.transform(user_df[categorical_columns])
        # # encoded_cols_df = pd.DataFrame(encoded_cols, columns=encoder.get_feature_names_out(categorical_columns))
        #
        # # Concatenate with original data
        # # user_df_encoded = pd.concat([user_df.drop(categorical_columns, axis=1), encoded_cols_df], axis=1)
        #
        # # Ensure user data has the same columns as training data, fill missing columns with zeros
        # # Assuming 'fitted_model_columns' is a list of columns from your model training data
        # fitted_model_columns = []
        # file_path = 'auto_mvp/mldeployment/columns.txt'
        #
        # # Check if the file exists
        # if os.path.exists(file_path):
        #     with open('auto_mvp/mldeployment/columns_f.txt', 'r') as file:
        #         fitted_model_columns = [line.strip() for line in file]
        #
        #
        # for col in fitted_model_columns:
        #     if col not in user_df_encoded.columns:
        #         user_df_encoded[col] = 0
        #
        # # Reorder columns to match training data
        # user_df_encoded = user_df_encoded[fitted_model_columns]
################################    new prepreprocessing    ############################################
        # Load the model columns from the text file
        # model_columns = pd.read_csv('columns_f.txt', header=None).iloc[:, 0].tolist()
          # Declare the variable outside the function

        # def load_model_columns():
        #     global model_columns
        #     model_columns = []
        #     # Declare that we're using the global variable
        #     file_path = '/home/daniil/Desktop/auto_shop/auto_mvp/mldeployment/columns_f.txt'
        #     if os.path.exists(file_path):
        #         with open(file_path, 'r') as file:
        #             line_strip = [line.strip() for line in file]
        #             model_columns.append(line_strip)
        #     else:
        #         return HttpResponse('model does"nt know cost of your car')
        # return model_columns
        # # Call the function to load the model columns
        #
        # load_model_columns()

        model_columns = ['Mileage', 'Engine_volume', 'Door_num', 'Body_Type_внедорожник 3 дв.', 'Body_Type_внедорожник 5 дв.',
         'Body_Type_компактвэн', 'Body_Type_купе', 'Body_Type_лифтбек', 'Body_Type_минивэн',
         'Body_Type_пикап двойная кабина', 'Body_Type_седан', 'Body_Type_универсал', 'Body_Type_фургон',
         'Body_Type_хэтчбек 3 дв.', 'Body_Type_хэтчбек 5 дв.', 'Color_баклажан', 'Color_бежевый', 'Color_белый',
         'Color_бирюзовый', 'Color_бордовый', 'Color_бронза', 'Color_вишня', 'Color_голубой', 'Color_жёлтый',
         'Color_зеленый', 'Color_золотистый', 'Color_коричневый', 'Color_красный', 'Color_оранжевый',
         'Color_серебристый', 'Color_серый', 'Color_синий', 'Color_фиолетовый', 'Color_хамелеон', 'Color_черный',
         'Transmission_автомат', 'Transmission_вариатор', 'Transmission_механика', 'Transmission_робот', 'Drive_задний',
         'Drive_передний', 'Drive_полный', 'Steering_слева', 'Steering_справа', 'Condition_идеальное',
         'Condition_новое', 'Condition_хорошее', 'Customs_не растаможен', 'Customs_растаможен',
         'Engine_fuel_type_бензин', 'Engine_fuel_type_газ', 'Engine_fuel_type_гибрид', 'Engine_fuel_type_дизель',
         'Availability_в наличии', 'Availability_в пути', 'Availability_на заказ',
         'Region_City_of_Sale_Айдаркен, Баткенская область', 'Region_City_of_Sale_Ала-Бука, Джалал-Абадская область',
         'Region_City_of_Sale_Базар-Коргон, Джалал-Абадская область', 'Region_City_of_Sale_Баткен, Баткенская область',
         'Region_City_of_Sale_Беловодское', 'Region_City_of_Sale_Бишкек', 'Region_City_of_Sale_Гульча, Ошская область',
         'Region_City_of_Sale_Джалал-Абад, Джалал-Абадская область', 'Region_City_of_Sale_Кадамжай, Баткенская область',
         'Region_City_of_Sale_Кант', 'Region_City_of_Sale_Каныш-Кыя, Джалал-Абадская область',
         'Region_City_of_Sale_Кара-Балта', 'Region_City_of_Sale_Кара-Куль, Джалал-Абадская область',
         'Region_City_of_Sale_Кара-Суу, Ошская область', 'Region_City_of_Sale_Каракол, Иссык-Кульская область',
         'Region_City_of_Sale_Кербен, Джалал-Абадская область', 'Region_City_of_Sale_Китай',
         'Region_City_of_Sale_Кочкор-Ата, Джалал-Абадская область', 'Region_City_of_Sale_Кызыл-Адыр, Таласская область',
         'Region_City_of_Sale_Кызыл-Кия, Баткенская область', 'Region_City_of_Sale_Маасы, Джалал-Абадская область',
         'Region_City_of_Sale_Майлуу-Суу, Джалал-Абадская область', 'Region_City_of_Sale_Нарын, Нарынская область',
         'Region_City_of_Sale_Ноокат, Ошская область', 'Region_City_of_Sale_Ош, Ошская область',
         'Region_City_of_Sale_США', 'Region_City_of_Sale_Сокулук', 'Region_City_of_Sale_Сузак, Джалал-Абадская область',
         'Region_City_of_Sale_Талас, Таласская область', 'Region_City_of_Sale_Таш-Кумыр, Джалал-Абадская область',
         'Region_City_of_Sale_Токмок', 'Region_City_of_Sale_Токтогул, Джалал-Абадская область',
         'Region_City_of_Sale_Узген, Ошская область', 'Region_City_of_Sale_в наличии', 'Registration_Абхазия',
         'Registration_Армения', 'Registration_Бишкек', 'Registration_Джалал-Абад, Джалал-Абадская область',
         'Registration_Кыргызстан', 'Registration_Кыргызстан', 'Registration_Не стоит на учёте',
         'Registration_Ош, Ошская область', 'Registration_Россия', 'Car_make_Acura', 'Car_make_Audi', 'Car_make_BMW',
         'Car_make_BYD', 'Car_make_Changan', 'Car_make_Chery', 'Car_make_Chevrolet', 'Car_make_Daewoo',
         'Car_make_EXEED', 'Car_make_Ford', 'Car_make_GAC', 'Car_make_Geely', 'Car_make_Genesis', 'Car_make_Haval',
         'Car_make_Honda', 'Car_make_Hyundai', 'Car_make_Infiniti', 'Car_make_Jaguar', 'Car_make_Jeep',
         'Car_make_Jetour', 'Car_make_Kia', 'Car_make_Land', 'Car_make_Lexus', 'Car_make_LiXiang', 'Car_make_Mazda',
         'Car_make_Mercedes-Benz', 'Car_make_Mitsubishi', 'Car_make_Nissan', 'Car_make_OMODA', 'Car_make_Opel',
         'Car_make_Ravon', 'Car_make_SsangYong', 'Car_make_Subaru', 'Car_make_Suzuki', 'Car_make_Tank',
         'Car_make_Toyota', 'Car_make_Volkswagen', 'Car_make_Volvo', 'Car_make_Voyah', 'Car_make_Zeekr', 'Car_make_ВАЗ']


        # print(f'model columns :{model_columns}')
        # print("Current Working Directory:", os.getcwd())

        # Assuming 'user_input_data' is a dictionary with user input
        # user_input_data = {
        #     # your user input data
        # }
        #
        # # Convert user input data to DataFrame
        # user_df = pd.DataFrame([user_input_data])

        # Apply one-hot encoding using pd.get_dummies (for categorical columns)
        # Add a prefix to avoid column name collisions
        categorical_columns = ['Body_Type', 'Color', 'Transmission', 'Drive', 'Steering',
                               'Condition', 'Customs', 'Availability', 'Region_City_of_Sale',
                               'Registration', 'Engine_fuel_type', 'Car_make']
        user_df = pd.get_dummies(user_df, columns=categorical_columns, prefix_sep='_')

        # print(user_df)

        # Align user_df columns with model_columns
        # Add missing columns and reorder
        # print(model_columns)
        for col in model_columns:
            if col not in user_df.columns:
                user_df[col] = 0  # adding missing columns with default value
        # print(user_df)
        user_df = user_df[model_columns]  # reordering columns

        print( f'last {user_df}')


        # Now user_df is ready for prediction
        # loaded_model = joblib.load('path/to/your_model.joblib')
        # predictions = loaded_model.predict(user_df)
######################################################################


        loaded_model = joblib.load('static/mldeployment/final_linear_regression_model.joblib')
        # input_data_encoded = pd.get_dummies(df,
        #                             columns=['Registration', 'Body_Type', 'Color', 'Transmission', 'Drive', 'Steering',
        #                                      'Condition', 'Customs', 'Availability', 'Region_City_of_Sale',
        #                                      'Engine_fuel_type', 'Car_make'])


        predicted_price = loaded_model.predict(user_df)
        print(predicted_price)




        if request.method == 'POST':

            predicted_price = loaded_model.predict(user_df)
            # Assuming predicted_price is a numpy array, get the first element
            predicted_price = predicted_price[0] if predicted_price.size > 0 else None

            context['predicted_price'] = predicted_price
    else:
    # If not a POST request, initialize an empty form
        form = CarForm()

    context['form'] = form

    return render(request, 'mldeployment/index.html', context)