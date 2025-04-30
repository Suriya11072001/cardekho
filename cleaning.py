import pandas as pd
import numpy as np



# Load the structured data
data = pd.read_csv('combined_structured_cars.csv')

# 1. Replace missing Engine_CC with median
data['Engine_CC'] = pd.to_numeric(data['Engine_CC'], errors='coerce')
engine_median = data['Engine_CC'].median()
data['Engine_CC'].fillna(engine_median, inplace=True)

# 2. Replace missing Mileage_kmpl with mean
data['Mileage_kmpl'] = pd.to_numeric(data['Mileage_kmpl'], errors='coerce')
mileage_mean = data['Mileage_kmpl'].mean()
data['Mileage_kmpl'].fillna(mileage_mean, inplace=True)

# 3. Convert Car_Price to numeric (if still string with ₹ or Lakh)
def convert_price(value):
    if pd.isnull(value):
        return np.nan
    value = str(value).replace('₹', '').strip()
    if 'Lakh' in value:
        return float(value.replace('Lakh', '').strip()) * 100000
    elif 'Crore' in value:
        return float(value.replace('Crore', '').strip()) * 10000000
    else:
        return float(''.join(c for c in value if c.isdigit() or c == '.'))

data['Car_Price'] = data['Car_Price'].apply(convert_price)

# Convert fields to integers after cleaning
data['Car_Price'] = data['Car_Price'].fillna(0).astype(int)
data['Registration_Year'] = pd.to_numeric(data['Registration_Year'], errors='coerce').fillna(0).astype(int)
data['Engine_CC'] = data['Engine_CC'].astype(int)
# Clean Kilometers_Driven properly
data['Kilometers_Driven'] = (
    data['Kilometers_Driven']
    .astype(str)
    .str.replace(',', '')
    .str.replace(' kms', '', case=False)
    .str.replace('km', '', case=False)
    .str.strip()
    .replace('nan', np.nan)
)

data['Kilometers_Driven'] = pd.to_numeric(data['Kilometers_Driven'], errors='coerce')
data['Kilometers_Driven'] = data['Kilometers_Driven'].astype(int)

# Save cleaned version
data.to_csv('preprocessed_car_data.csv', index=False)
print("✅ Cleaned and preprocessed data saved as 'preprocessed_car_data.csv'")
