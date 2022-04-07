import pandas as pd
from pathlib import Path, PurePath

directory = Path(__file__).parent.absolute()
data_csv_file = PurePath(directory, "salaries_by_college_major.csv")

df = pd.read_csv(data_csv_file)
pd.set_option("max_columns", 10)
pd.options.display.float_format = '{:,.2f}'.format 


print("Head:")
print(df.head())
pd.reset_option("max_columns")

print("Shape:")
print(df.shape)

print("Columns:")
print(df.columns)

print("Cells not a number:")
print(df.isna())

# drop rows with cells containing not a number values
df = df.dropna()


max_starting_median_salary = df['Starting Median Salary'].max()
print(max_starting_median_salary)

id_max_starting_median_salary = df['Starting Median Salary'].idxmax()
print(id_max_starting_median_salary)

max_starting_median_salary_major = df['Undergraduate Major'].loc[id_max_starting_median_salary]
print(max_starting_median_salary_major)


# What college major has the highest mid-career salary? How much do graduates with this major earn? (Mid-career is defined as having 10+ years of experience).
print("\nWhat college major has the highest mid-career salary? How much do graduates with this major earn? (Mid-career is defined as having 10+ years of experience).")
max_mid_career_median_salary = df['Mid-Career Median Salary'].max()
id_max_mid_career_median_salary = df['Mid-Career Median Salary'].idxmax()
max_mid_career_median_salary_major = df['Undergraduate Major'][id_max_mid_career_median_salary]
print(max_mid_career_median_salary)
print(max_mid_career_median_salary_major)

# Which college major has the lowest starting salary and how much do graduates earn after university?
print("\nWhich college major has the lowest starting salary and how much do graduates earn after university?")
min_starting_median_salary = df['Starting Median Salary'].min()
id_min_starting_median_salary = df['Starting Median Salary'].idxmin()
min_starting_median_salary_major = df['Undergraduate Major'][id_min_starting_median_salary]
print(min_starting_median_salary)
print(min_starting_median_salary_major)

# Which college major has the lowest mid-career salary and how much can people expect to earn with this degree? 
print("\nWhich college major has the lowest mid-career salary and how much can people expect to earn with this degree?")
min_mid_career_median_salary = df['Mid-Career Median Salary'].min()
id_min_mid_career_median_salary = df['Mid-Career Median Salary'].idxmin()
min_mid_career_median_salary_major = df['Undergraduate Major'][id_min_mid_career_median_salary]
print(min_mid_career_median_salary)
print(min_mid_career_median_salary_major)

# Insert spread between 90th and 10th percentile salaries - to help find spread of the salary ranges
df.insert(1, "Spread", df['Mid-Career 90th Percentile Salary'].subtract(df['Mid-Career 10th Percentile Salary']))
print("\n")
print(df.head())

df = df.sort_values('Spread')

print("\nLow risk:")
print(df.head())


print("\nHighest potential (top 5 degrees with the highest values in the 90th percentile):")
df = df.sort_values('Mid-Career 90th Percentile Salary', ascending=False)
print(df.head())


print("\nHighest risk (largest spread):")
df = df.sort_values('Spread', ascending=False)
print(df.head())


print("\nHighest mid career median salary:")
df = df.sort_values('Mid-Career Median Salary', ascending=False)
print(df.head())


df_grouped = df.groupby('Group')
print(f"\nDegree group count: {df_grouped.count()}")
print(f"\nMean: {df_grouped.mean()}")