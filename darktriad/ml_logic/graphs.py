"""
This file holds functions that draw different plots
"""

### IMPORTING LIBRARIES/PACKAGES
from darktriad.ml_logic.preprocess import preprocess
from darktriad.ml_logic.Feat_engine import feature_engineering
import pandas as pd
import plotly.express as px
import country_converter as coco
import matplotlib.pyplot as plt


### DRAWS MAP OF THE WORLD WITH AVERAGE SCORES SHOWN
# This expects the raw dataframe (i.e. X = pd.read(URL))
def draw_map(X: pd.DataFrame):
    X = preprocess(X)
    X = feature_engineering(X)
    X['Overall_Avg'] = X[['Narcissism_Avg', 'Psychopathy_Avg', 'Machiavellianism_Avg']].mean(axis = 1).round(3)
    X = X[['country', 'Narcissism_Avg', 'Psychopathy_Avg', 'Machiavellianism_Avg', 'Overall_Avg']]
    tmp = X.groupby('country').mean()
    tmp.reset_index(inplace=True)
    tmp = tmp.iloc[2:]
    countries = tmp.country
    countries_to_drop = ['AP', 'AN', 'EU']
    tmp.country = countries[~countries.isin(countries_to_drop)].dropna()
    tmp.dropna(inplace=True)
    cc = coco.CountryConverter()
    iso3_codes = cc.pandas_convert(series = tmp.country, to = 'ISO3')
    countries_full_name = cc.pandas_convert(series = tmp.country, to = 'name_short')
    tmp['country_code'] = iso3_codes
    tmp['country_name'] = countries_full_name
    fig = px.choropleth(tmp,
                        locations = 'country_code',
                        color = 'Overall_Avg',
                        hover_data = ['Narcissism_Avg',
                                       'Psychopathy_Avg',
                                       'Machiavellianism_Avg'],
                        labels = 'country_name',
                        color_continuous_scale = px.colors.sequential.thermal_r,
                        title = '<b>Average SD3 Scores by Country</b>',
                        width = 750)
    fig.update_layout(title=dict(text="Average Dark Triad Trait Scores by Country",
                                 font=dict(size=30),
                                 automargin=True,
                                 yref='paper'),
                      title_x = 0.5,
                      title_font_color = 'white',
                      title_font_family = 'balto',
                      plot_bgcolor='black',
                      paper_bgcolor = 'rgba(0,0,0,0)')  # controls the transparency of the background
    return fig

### DRAWS THE BARPLOTS SHOWING DISTRIBUTION OF SCORES PER QUESTION
# NOT CURRENTLY WORKING!!! NEEDS TO BE ADAPTED FOR USE WITH STREAMLIT
def draw_question_dist_barplots(X: pd.DataFrame):
    X = preprocess(X)
    X = feature_engineering(X)

    questions = ["It's not wise to tell your secrets.",
                 "I like to use clever manipulation to get my way.",
                 "Whatever it takes, you must get the important people on your side. ",
                 "Avoid direct conflict with others because they may be useful in the future.",
                 "It's wise to keep track of information that you can use against people later.",
                 "You should wait for the right time to get back at people. ",
                 "There are things you should hide from other people because they don't need to know.",
                 "Make sure your plans benefit you, not others.",
                 "Most people can be manipulated.",
                 "People see me as a natural leader. ",
                 "I hate being the center of attention.",
                 "Many group activities tend to be dull without me.",
                 "I know that I am special because everyone keeps telling me so. ",
                 "I like to get acquainted with important people. ",
                 "I feel embarrassed if someone compliments me.",
                 "I have been compared to famous people. ",
                 "I am an average person.",
                 "I insist on getting the respect I deserve.",
                 "I like to get revenge on authorities.",
                 "I avoid dangerous situations.",
                 "Payback needs to be quick and nasty. ",
                 "People often say I'm out of control. ",
                 "It's true that I can be mean to others. ",
                 "People who mess with me always regret it.",
                 "I have never gotten into trouble with the law.",
                 "I enjoy having sex with people I hardly know.",
                 "I'll say anything to get what I want.",
                 "Are you a US citizen?"]

    column_names = ['M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8', 'M9', 'N1',
                    'N2', 'N3', 'N4', 'N5', 'N6', 'N7', 'N8', 'N9', 'P1', 'P2',
                    'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9']

    def plot_bar_chart(column_name):
        column_values = X[column_name]
        value_counts = column_values.value_counts()
        position = column_names.index(column_name)
        question = questions[position]
        plt.bar(value_counts.index, value_counts.values)
        plt.xlabel(f'Scores for question {column_name}')
        plt.ylabel('Count')
        plt.title(f'{column_name}: {question}')
        plt.show()

    return plot_bar_chart(X)
