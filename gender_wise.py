from common_functions import load_data, clean_data, plot_trend, bar_graph, pie_chart_gender

# -- DATASET 1 -- #

file_path = 'datasets\\male_population.csv'
# Loading datset via common functions
male_population = load_data(file_path)

# Inspecting first three lines
print(male_population.head(3))

# Cleaning data via common functions
male_population_cleaned = clean_data(male_population)

print(male_population_cleaned)

# Population trends over time // Plotting annual male population growth
plot_trend(male_population_cleaned, title='Male Population Growth Over Time')

# Bar plot of population by year
bar_graph(male_population_cleaned, title='Male Population by Year')


# -- DATASET 2 -- #

file_path1 = 'datasets\\female_population.csv'
# Loading dataset via common functions
female_population = load_data(file_path1)

# Inspecting first three lines
print(female_population.head(3))

# Cleaning data via common functions
female_population_cleaned = clean_data(female_population)

print(female_population_cleaned)

# Population trends over time // Plotting annual female population growth
plot_trend(female_population_cleaned, title='Female Population Growth Over Time')

# Bar plot of population by year
bar_graph(female_population_cleaned, title='Female Population by Year')


# -- COMBINED VISUALIZATION -- #

# Pie chart for the year 2022
pie_chart_gender(male_population_cleaned, female_population_cleaned, year='2022',
                  title='Population Distribution by Gender for 2022')