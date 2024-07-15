from common_functions import load_data, clean_data, plot_trend, pie_chart_age

# -- DATASET 1 -- #

file_path = 'datasets\\ages_0-14.csv'
# Loading datset via common functions
ages_0_14 = load_data(file_path)

# Inspecting first three lines
print(ages_0_14.head(3))

# Cleaning data via common functions
ages_0_14_cleaned = clean_data(ages_0_14)

print(ages_0_14_cleaned)

# Population trends over time // Plotting annual male population growth
plot_trend(ages_0_14_cleaned, title='Ages 0-14 Over Time')


# -- DATASET 2 -- #

file_path = 'datasets\\ages_15-64.csv'
# Loading datset via common functions
ages_15_64 = load_data(file_path)

# Inspecting first three lines
print(ages_15_64.head(3))

# Cleaning data via common functions
ages_15_64_cleaned = clean_data(ages_15_64)

print(ages_15_64_cleaned)

# Population trends over time // Plotting annual male population growth
plot_trend(ages_15_64_cleaned, title='Ages 15-64 Over Time')


# -- DATASET 3 -- #

file_path = 'datasets\\ages_65andabove.csv'
# Loading datset via common functions
ages_above_65 = load_data(file_path)

# Inspecting first three lines
print(ages_above_65.head(3))

# Cleaning data via common functions
ages_above_65_cleaned = clean_data(ages_above_65)

print(ages_above_65_cleaned)

# Population trends over time // Plotting annual male population growth
plot_trend(ages_above_65_cleaned, title='Ages 65 and Above Over Time')


# -- COMBIED VISUALIZATION -- #

# Pie chart for the year 2022
pie_chart_age(ages_0_14_cleaned, ages_15_64_cleaned, ages_above_65_cleaned, year='2022', 
              title='Age-wise Population Distribution for 2022')