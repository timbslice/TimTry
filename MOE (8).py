#!/usr/bin/env python
# coding: utf-8

# In[59]:


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

st.set_page_config(page_title='MOE Dashboard', page_icon=':bar_chart')

# Load your data into a pandas DataFrame named data
data = pd.read_csv(r"C:\Users\Emily\Downloads\Lab's IOD\Education Indicators 2014.csv")

# Title and description
st.title('MOE Dashboard')
st.markdown('This is a basic dashboard displaying some insights into the MOE interview dataset.')

st.markdown("# DataFrame Head")
st.write(data.describe())


# Country and TDP Comparison Joint Plot
fig1, axs = plt.subplots(1, 2, figsize=(12, 6))

# Dropdown for country selection
countries = sorted(data['Country Name'].unique())
selected_country = st.sidebar.selectbox('Select a Country', countries)

# Filter the data for the selected country and for the world
country_data = data[data['Country Name'] == selected_country]
world_data = data[data['Country Name'] == 'World']

# Calculate the average unemployment and GDP for the selected country and the world
avg_unemp_country = country_data['UNEMP'].mean()
avg_gdp_country = country_data['GDP'].mean()

avg_unemp_world = world_data['UNEMP'].mean()
avg_gdp_world = world_data['GDP'].mean()

# Create a DataFrame for the plot
plot_data = pd.DataFrame({
    'Country': [selected_country, 'World'],
    'Average Unemployment': [avg_unemp_country, avg_unemp_world],
    'Average GDP': [avg_gdp_country, avg_gdp_world]
})


# Set a grayscale color palette
custom_palette = sns.color_palette('Set2')

# Create the bar chart with the grayscale color palette
sns.barplot(y= 'UNEMP', x='Country Name', data=data, ax=axs[0], palette=custom_palette)

axs[0].set_title('Comparing GDP and Unemployment')
axs[0].set_ylabel('Value')

# Country and TDP Comparison Scatter Plot
sns.scatterplot(y='TDP', x='Country Name', data=data, ax=axs[1])
axs[1].set_xlabel('Total Domestic Product (TDP)')
axs[1].set_ylabel('Country Name')
axs[1].set_title('Country vs TDP')

# Show the plots
st.pyplot(fig1)

# Description of the data set
st.subheader('Data Set Description')
st.markdown('This dataset contains education indicators from 2014.')

# Calculate mean and standard deviation of GDP
mean_gdp = data['GDP'].mean()
std_gdp = data['GDP'].std()

# Create a slider for GDP values in the sidebar
min_gdp = max(0, mean_gdp - 0.5 * std_gdp)
max_gdp = mean_gdp + 0.5 * std_gdp
selected_gdp = st.sidebar.slider('Select GDP Range', min_value=float(min_gdp), max_value=float(max_gdp),
                                 value=(float(min_gdp), float(max_gdp)))

# Filter the data for the selected GDP range
filtered_data = data[(data['GDP'] >= selected_gdp[0]) & (data['GDP'] <= selected_gdp[1])]

# Create two simple graphs, e.g., histograms
fig2, axs = plt.subplots(1, 2, figsize=(9, 6))

# Assuming the data frame has columns 'UNEMP' and 'PRPE'
filtered_data['UNEMP'].plot(kind='hist', ax=axs[0])
axs[0].set_title(f'Unemployment within selected GDP')

filtered_data['PRPE'].value_counts().plot(kind='bar', ax=axs[1])
axs[1].set_title(f'Percentage of repeaters in Primary Education')

# Show the graphs
st.pyplot(fig2)


# In[ ]:




