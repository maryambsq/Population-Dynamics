import pandas as pd
from numpy import size
from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt

def load_data(file_path):
    return pd.read_csv(file_path)

def clean_data(data):
    # Dropping rows with NaN values
    data_cleaned = data.dropna(how='all')

    # Renaming columns
    data_cleaned.columns = ['Series_Name', 'Series_Code', 'Country_Name', 'Country_Code','1990', '2000', '2014', 
                            '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']

    # Dropping rows where country code is NaN
    data_cleaned = data_cleaned.dropna(subset=['Country_Code'])

    # Selecting only the necessary columns
    data_cleaned = data_cleaned[['Country_Name', 'Country_Code', '1990', '2000', '2014', '2015', '2016', '2017',
                                 '2018', '2019', '2020', '2021', '2022']] 

    # Converting year columns into numerics
    year_columns = ['1990', '2000', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
    data_cleaned[year_columns] = data_cleaned[year_columns].apply(pd.to_numeric, errors='coerce')

    return data_cleaned

def format_millions_billions(x, pos):
    if x >= 1e9:
        return f'{x*1e-9:0.1f}B'
    elif x >= 1e6:
        return f'{x*1e-6:0.1f}M'
    else:
        return f'{x:0.1f}'

def plot_trend(data, title, xlabel='Year', ylabel='Population'):
    # Reshaping data for plotting
    population_trend = data.melt(id_vars=['Country_Name', 'Country_Code'],
                                 var_name='Year', 
                                 value_name='Total_Population')


    # Plotting the population
    plt.figure(figsize=(10,6))
    plt.plot(population_trend['Year'], population_trend['Total_Population'], marker='o')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)

    formatter = FuncFormatter(format_millions_billions)
    plt.gca().yaxis.set_major_formatter(formatter)

    plt.show()

def bar_graph(data, title):
    # Bar plot of population by year
    population_bar = data.melt(id_vars=['Country_Name', 'Country_Code'],
                                 var_name='Year', 
                                 value_name='Total_Population')
    plt.figure(figsize=(10, 6))
    plt.bar(population_bar['Year'], population_bar['Total_Population'], color='skyblue')
    plt.title(title)
    plt.xlabel('Year')
    plt.ylabel('Total Population')

    formatter = FuncFormatter(format_millions_billions)
    plt.gca().yaxis.set_major_formatter(formatter)

    plt.show()

def pie_chart_gender(male_population, female_population, year, title):
    # Pie chart of population distribution by gender
    male_p = male_population[year].sum()
    female_p = female_population[year].sum()
    labels = ['Male', 'Female']
    sizes = [male_p, female_p]
    colors = ['lightblue', 'pink']

    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.title(title)
    plt.axis('equal')
    plt.show()    

def pie_chart_age(ages_0_14, ages_15_64, ages_above_65, year, title):
    # Pie chart of age-wise population distribution
    ages_0_14 = ages_0_14[year].sum()
    ages_15_64 = ages_15_64[year].sum()
    ages_above_65 = ages_above_65[year].sum()  
    labels = ['0-14', '15-64', '65 AND ABOVE']  
    sizes = [ages_0_14, ages_15_64, ages_above_65]
    colors = ['lightslategray', 'lightcoral', 'palegoldenrod']

    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.title(title)
    plt.axis('equal')
    plt.show()