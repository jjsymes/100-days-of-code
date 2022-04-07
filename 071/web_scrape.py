from urllib.error import HTTPError
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


BASE_URL = "https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors"

df = pd.DataFrame(columns = ['Major' , 'Early Career Pay', 'Mid-Career Pay', '% High Meaning'])
page = 1
more_data = True

while more_data:
    url = f"{BASE_URL}/page/{page}"
    try:
        header = {
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
        }
        response = requests.get(url, headers=header)
        response.raise_for_status()
    except HTTPError:
        print("Failed to load page.")
    else:
        print(f"Scraping page {page}...")
        page += 1
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        data_rows = soup.find_all(class_="data-table__row", name="tr")

        if len(data_rows) == 0:
            more_data = False

        for row in data_rows:
            major = row.find(class_="data-table__cell csr-col--school-name").find(class_="data-table__value", name="span").get_text()
            rank = row.find(class_="data-table__cell csr-col--rank").find(class_="data-table__value", name="span").get_text()
            degree_type = row.find(class_="csr-col--school-type").find(class_="data-table__value", name="span").get_text()
            extra_columns = row.find_all(class_="data-table__cell csr-col--right")
            for extra_column in extra_columns:
                column_title = extra_column.find(class_="data-table__title").get_text()
                if "Early Career Pay" in column_title:
                    early_career_pay = extra_column.find(class_="data-table__value").get_text()
                elif "Mid-Career Pay" in column_title:
                    mid_career_pay = extra_column.find(class_="data-table__value").get_text()
                elif "% High Meaning" in column_title:
                    percentage_high_meaning = extra_column.find(class_="data-table__value").get_text()

            df=df.append({'Major': major , 'Early Career Pay': early_career_pay, 'Mid-Career Pay': mid_career_pay, '% High Meaning': percentage_high_meaning} , ignore_index=True)


df["Early Career Pay"] = df["Early Career Pay"].replace('[\$,]', '', regex=True).astype(float)
df["Mid-Career Pay"] = df["Mid-Career Pay"].replace('[\$,]', '', regex=True).astype(float)
df["% High Meaning"] = df["% High Meaning"].replace('[\%]', '', regex=True)
df["% High Meaning"] = df["% High Meaning"].replace('[\-]', np.nan, regex=True)
df = df.dropna()
print(df)

max_starting_median_salary = df['Early Career Pay'].max()
print("Max starting salary:")
print(max_starting_median_salary)
id_max_starting_median_salary = df['Early Career Pay'].idxmax()
print(id_max_starting_median_salary)
max_starting_median_salary_major = df['Major'].loc[id_max_starting_median_salary]
print(max_starting_median_salary_major)


# # What college major has the highest mid-career salary? How much do graduates with this major earn? (Mid-career is defined as having 10+ years of experience).
print("\nWhat college major has the highest mid-career salary? How much do graduates with this major earn? (Mid-career is defined as having 10+ years of experience).")
max_mid_career_median_salary = df['Mid-Career Pay'].max()
id_max_mid_career_median_salary = df['Mid-Career Pay'].idxmax()
max_mid_career_median_salary_major = df['Major'][id_max_mid_career_median_salary]
print(max_mid_career_median_salary)
print(max_mid_career_median_salary_major)

# # Which college major has the lowest starting salary and how much do graduates earn after university?
print("\nWhich college major has the lowest starting salary and how much do graduates earn after university?")
min_starting_median_salary = df['Early Career Pay'].min()
id_min_starting_median_salary = df['Early Career Pay'].idxmin()
min_starting_median_salary_major = df['Major'][id_min_starting_median_salary]
print(min_starting_median_salary)
print(min_starting_median_salary_major)

# # Which college major has the lowest mid-career salary and how much can people expect to earn with this degree? 
print("\nWhich college major has the lowest mid-career salary and how much can people expect to earn with this degree?")
min_mid_career_median_salary = df['Mid-Career Pay'].min()
id_min_mid_career_median_salary = df['Mid-Career Pay'].idxmin()
min_mid_career_median_salary_major = df['Major'][id_min_mid_career_median_salary]
print(min_mid_career_median_salary)
print(min_mid_career_median_salary_major)

# print("\nHighest mid career median salary:")
df = df.sort_values('Mid-Career Pay', ascending=False)
print(df.head())
