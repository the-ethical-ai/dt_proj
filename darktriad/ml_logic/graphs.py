"""
This file holds functions that draw different plots
"""

### IMPORTING LIBRARIES/PACKAGES
from darktriad.ml_logic.preprocess import preprocess
from darktriad.ml_logic.Feat_engine import feature_engineering
import pandas as pd
import plotly.express as px
import country_converter as coco


### DRAWS MAP OF THE WORLD WITH AVERAGE SCORES SHOWN
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
