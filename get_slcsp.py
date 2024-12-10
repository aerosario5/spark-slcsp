import csv
import pandas as pd
import shutil

def match_zip_code_to_rate_area(zip_codes, zip_code):
    zip_code_data = zip_codes.loc[zip_codes['zipcode'] == zip_code]
    rate_areas = zip_code_data.loc[:, 'rate_area'].tolist()
    if all(rate_area == rate_areas[0] for rate_area in rate_areas):
        return rate_areas[0]
    return None

def match_rate_area_to_plan_rates(rate_area, plans):
    if not rate_area:
        return []
    area_plans = plans.loc[plans['rate_area'] == rate_area]
    sorted_area_plans = area_plans.sort_values(by='rate', ascending=True)
    return [float(rate) for rate in sorted_area_plans.loc[:, 'rate'].tolist()]

def find_second_lowest_rate(rates):
    if not rates or len(rates) < 2:
        return ''
    lowest_rate = rates[0]
    for i in range(1,len(rates)):
        if rates[i] > lowest_rate:
            return rates[i]
    return ''


if __name__ == '__main__':
    zip_codes = pd.read_csv('zips.csv')
    plans = pd.read_csv('plans.csv')
    silver_plans = plans.loc[plans['metal_level'] == 'Silver']
    tempfile_name = 'tempfile.csv'
    with open('slcsp.csv', newline='') as slcsp:
        reader = csv.DictReader(slcsp)
        with open(tempfile_name, 'w', newline='') as tempfile:
            writer = csv.writer(tempfile, quoting=csv.QUOTE_MINIMAL, quotechar='\n')
            writer.writerow(['zipcode','rate'])
            for row in reader:
                z = row['zipcode']
                rate_area = match_zip_code_to_rate_area(zip_codes, int(z))
                silver_plan_rates = match_rate_area_to_plan_rates(rate_area, silver_plans)
                second_lowest_rate = find_second_lowest_rate(silver_plan_rates)
                print(z + ','+str(second_lowest_rate))
                writer.writerow([z, second_lowest_rate])

    # Rename original file to have a backup
    shutil.move('slcsp.csv', 'slcsp_backup.csv')
    # Return new file with rates added
    shutil.move(tempfile_name, 'slcsp.csv')
