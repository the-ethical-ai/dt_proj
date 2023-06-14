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
import seaborn as sns
import numpy as np

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
    plot_bar_chart(X)

### Draws the Average Question Scores scatterplot (bubble plots)
def draw_bubble_plot():
    df = pd.read_csv("https://raw.githubusercontent.com/Habeus-Crimpus/Dark_Triad/main/data.csv",delimiter = '\t')
    df.drop_duplicates(inplace = True)
    df.dropna(inplace=True)
    df.drop("source", axis=1, inplace = True)
    flip_cols = ['N2', 'N6', 'N8', 'P2', 'P4', 'P7']
    for col in flip_cols:
        for i in df[col]:
            if df[col][i] == 1:
                df[col][i] = 5
            elif df[col][i] == 5:
                df[col][i] = 1
            elif df[col][i] == 4:
                df[col][i] = 2
            elif df[col][i] == 2:
                df[col][i] = 4
    df.replace(0,3, inplace=True)
    df.drop(columns = 'country', inplace = True)
    narcis_df = df[['N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7', 'N8', 'N9']]
    mach_df = df[['M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8', 'M9']]
    psych_df = df[['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9']]
    question_avg_scores = df.mean(axis = 0).reset_index()
    trait_type = ['Machiavellianism', 'Machiavellianism', 'Machiavellianism', 'Machiavellianism',
              'Machiavellianism', 'Machiavellianism', 'Machiavellianism', 'Machiavellianism',
              'Machiavellianism', 'Narcissism','Narcissism', 'Narcissism', 'Narcissism',
              'Narcissism', 'Narcissism', 'Narcissism', 'Narcissism', 'Narcissism',
              'Psychopathy', 'Psychopathy', 'Psychopathy', 'Psychopathy', 'Psychopathy',
              'Psychopathy', 'Psychopathy', 'Psychopathy', 'Psychopathy']
    question_avg_scores['Trait_Type'] = trait_type
    question_avg_scores.rename(columns = {0: 'Average_Score'}, inplace=True)
    question_avg_scores.Average_Score = question_avg_scores.Average_Score.round(3)
    color_map = {'Machiavellianism': 'rgb(7, 28, 105)',
             'Narcissism': 'rgb(2, 168, 10)',
             'Psychopathy': 'rgb(133, 9, 32)'}

    bubble_fig = px.scatter(question_avg_scores,
                            x = 'index',
                            y = 'Average_Score',
                            size = 'Average_Score',
                            color = 'Trait_Type',
                            symbol = 'Trait_Type',
                            opacity = [1],
                            hover_name = 'index',
                            color_discrete_map = color_map)


    bubble_fig.update_layout(title = dict(text="Average Scores by Question",
                                 font = dict(size=30),
                                 automargin = True,
                                 yref = 'paper'),
                      title_x = 0.5,
                      title_font_color = 'white',
                      title_font_family = 'balto',
                      plot_bgcolor = 'rgb(36,36,36)',
                      xaxis = dict(title = 'Questions', range=[-1, 27], dtick=0.5,
                                   showticklabels = False,
                                   tickcolor = 'white',
                                   title_font=dict(size=18, family='balto',
                                                   color = 'white')),
                      yaxis = dict(title = 'Scores', range=[1, 5], dtick=1,
                                   showticklabels = True,
                                   tickcolor = 'white',
                                   title_font=dict(size=18, family='balto',
                                                   color = 'white')),
                      legend = dict(font=dict(color='white')),
                      paper_bgcolor = 'rgba(0,0,0,0)')

    bubble_fig.show()

def plot_results(PSY, NAR, MAC):
    C = ['PSYCHOPATHY', 'NARCISSISM', 'MACHIAVELLIANISM']

    sns.set_style("white")

    fig, ax = plt.subplots(figsize=(8, 6))

    sns.set_palette(["lightblue", "#99FF99", "#FF9999"])

    positions = np.arange(3)

    total_height = 5

    ratios = [(0.14,0.70,0.16), (0.12,0.67,0.21), ( 0.13, 0.70,0.17)]

    bars = []
    for i in range(len(positions)):
        bar_bottom = 0
        for j, ratio in enumerate(ratios[i]):
            bar_height = ratio * total_height

            if i == 0 and PSY == 1 and j == 2:
                color = '#FF9999'
            elif i == 0 and PSY == 0 and j == 1:
                color = '#99FF99'
            elif i == 0 and PSY == -1 and j == 0:
                color = 'lightblue'
            elif i == 1 and NAR == 1 and j == 2:
                color = '#FF9999'
            elif i == 1 and NAR == 0 and j == 1:
                color = '#99FF99'
            elif i == 1 and NAR == -1 and j == 0:
                color = 'lightblue'
            elif i == 2 and MAC == 1 and j == 2:
                color = '#FF9999'
            elif i == 2 and MAC == 0 and j == 1:
                color = '#99FF99'
            elif i == 2 and MAC == -1 and j == 0:
                color = 'lightblue'
            else:
                color = 'gray'

            bar = ax.bar(positions[i], bar_height, width=0.35, bottom=bar_bottom, color=color, edgecolor='black', linewidth=0.3, alpha=0.9, capstyle='round')
            bars.append(bar)
            bar_bottom += bar_height

    ax.set_title('Result')
    ax.set_xticks(positions)
    ax.set_xticklabels(C)
    ax.set_yticks(range(int(total_height)+1))
    ax.set_ylim(0, total_height+1)
    ax.yaxis.grid(False)

    for bar_group in bars:
        for bar in bar_group:
            height = bar.get_height()
            x = bar.get_x() + bar.get_width() / 2
            y = bar.get_y() + height / 2
            ax.annotate(f'{int(height / total_height * 100 + 0.5)}%', xy=(x, y), xytext=(0, 0), textcoords='offset points', ha='center', va='center')

    above_avg_patch = plt.Rectangle((0, 0), 1, 1, fc='#FF9999')
    avg_patch = plt.Rectangle((0, 0), 1, 1, fc='#99FF99')
    below_avg_patch = plt.Rectangle((0, 0), 1, 1, fc='lightblue')

    ax.legend([above_avg_patch, avg_patch, below_avg_patch], ['Above average', 'Average', 'Below average'])


    plt.show()

