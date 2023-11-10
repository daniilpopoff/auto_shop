import pandas as pd

car_info_dict = {
    "Year of Manufacture": None,
    "Mileage": None,
    "Body Type": None,
    "Color": None,
    "Engine": None,
    "Transmission": None,
    "Drive": None,
    "Steering": None,
    "Condition": None,
    "Customs": None,
    "Availability": None,
    "Region, City of Sale": None,
    "Registration": None
}

# Convert the dictionary to a Pandas DataFrame
df = pd.DataFrame.from_dict(car_info_dict, orient='index', columns=['Value'])

# Reset the index to set the labels as a column
df.reset_index(inplace=True)
df.columns = ['Label', 'Value']

# Display the DataFrame
print(type(df))