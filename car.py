import pandas as pd
import numpy as np
import ast
import os

def structure_unstructured_city(filepath, city_name):
    df = pd.read_excel('chennai_cars.xlsx')

    fuel_type = []
    body_type = []
    kilometers_driven = []
    transmission_type = []
    no_of_owners = []
    oem = []
    model = []
    model_year = []
    price = []
    registration_year = []
    seats = []
    engine_cc = []
    mileage = []

    for i in range(df.shape[0]):
        try:
            new_car_detail = ast.literal_eval(df['new_car_detail'][i])
            new_car_overview = ast.literal_eval(df['new_car_overview'][i])
            new_car_specs = ast.literal_eval(df['new_car_specs'][i])

            fuel_type.append(new_car_detail.get('ft'))
            # BODY TYPE FIX — Try detail, then fallback to overview
            body = new_car_detail.get('bt')
            if not body:
                body = next((item['value'] for item in new_car_overview.get('top', []) if item['key'] == 'Body Type'), None)
            body_type.append(body)
            kilometers_driven.append(new_car_detail.get('km'))
            transmission_type.append(new_car_detail.get('transmission'))
            no_of_owners.append(new_car_detail.get('ownerNo'))
            oem.append(new_car_detail.get('oem'))
            model.append(new_car_detail.get('model'))
            model_year.append(int(new_car_detail.get('modelYear', 0)))
            price.append(new_car_detail.get('price'))

            # Robustly get registration year and seating
            try:
                registration_year.append(new_car_overview['top'][0]['value'][-4:])
            except:
                registration_year.append(None)

            try:
                seats.append(new_car_overview['top'][3]['value'][0])
            except:
                seats.append(None)

            try:
                if (new_car_specs['data'][0]['list'][2]['value']).isnumeric():
                    engine_cc.append(new_car_specs['data'][0]['list'][2]['value'])
                else:
                    engine_cc.append(new_car_specs['data'][0]['list'][1]['value'])
            except:
                engine_cc.append(np.nan)

            try:
                mileage.append(new_car_specs['top'][0]['value'][:-5])
            except:
                mileage.append(None)

        except Exception as e:
            print(f"Error processing row {i} in {city_name}: {e}")
            fuel_type.append(None)
            body_type.append(None)
            kilometers_driven.append(None)
            transmission_type.append(None)
            no_of_owners.append(None)
            oem.append(None)
            model.append(None)
            model_year.append(None)
            price.append(None)
            registration_year.append(None)
            seats.append(None)
            engine_cc.append(None)
            mileage.append(None)

    df_structured = pd.DataFrame({
        'Fuel_Type': fuel_type,
        'Body_Type': body_type,
        'Kilometers_Driven': kilometers_driven,
        'Transmission_Type': transmission_type,
        'No_of_Owners': no_of_owners,
        'Manufactured_By': oem,
        'Car_Model': model,
        'Car_Produced_Year': model_year,
        'Car_Price': price,
        'Registration_Year': registration_year,
        'No_of_Seats': seats,
        'Engine_CC': engine_cc,
        'Mileage_kmpl': mileage,
        'City': city_name,
        'Car_Link': df['car_links']
    })

    return df_structured


if __name__ == "__main__":
    folder_path = 'C:\\Users\\HP\\Desktop\\capstone.3\\'
    city_files = {
        'Chennai': 'chennai_cars.xlsx',
        'Bangalore': 'bangalore_cars.xlsx',
        'Kolkata': 'kolkata_cars.xlsx',
        'Jaipur': 'jaipur_cars.xlsx',
        'Delhi': 'delhi_cars.xlsx',
        'Hyderabad':'hyderabad_cars.xlsx'
    }

    all_dfs = []

    for city, filename in city_files.items():
        path = os.path.join(folder_path, filename)
        print(f"📄 Processing {city} data...")
        city_df = structure_unstructured_city(path, city)
        all_dfs.append(city_df)

    # Combine all cities into one dataset
    combined_df = pd.concat(all_dfs, ignore_index=True)

    # Save to CSV
    combined_df.to_csv('combined_structured_cars.csv', index=False)

    print("✅ All 5 city datasets combined and saved as 'combined_structured_cars.csv'")
