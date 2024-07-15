from common_functions import load_data, clean_data, plot_trend, bar_graph

file_path = 'datasets\\total_population_1990,2000,2015-2022.csv'
# Loading dataset via common functions
total_population = load_data(file_path)

# Inspecting first three lines
print(total_population.head(3))

# Cleaning data via common functions
total_population_cleaned = clean_data(total_population)
print(total_population_cleaned)

# Population trends over time // Plotting annual total population growth
plot_trend(total_population_cleaned, title='Total Population Growth Over Time')

# Bar plot of population by year
bar_graph(total_population_cleaned, title='Population by Year')