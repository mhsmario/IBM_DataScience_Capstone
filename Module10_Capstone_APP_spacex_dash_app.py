#coursera IBM Module 10 - Capstone
#Author: Mario Saraiva


# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("/Users/mariosaraiva/Documents/DataScience/Coursera/IBM DataScience Track/spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),

                                # Dropdown
                                dcc.Dropdown(id='site_dropdown',
                                          options=[
                                              {'label': 'All Sites', 'value': 'ALL'},
                                              {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
                                              {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'},
                                              {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
                                              {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'},],
                                           value= 'ALL',
                                           placeholder='Select a Launch Site here',
                                           searchable = True),    
                                
                                html.Br(),

                                # Pie Chart
                                html.Div(dcc.Graph(id='success_pie_chart')),
                                
                                html.Br(),

                                html.P("Payload range (Kg):"),

                                #Slider
                                dcc.RangeSlider(id='payload_slider',
                                    min=0, max=10000, step=1000, 
                                    marks={0: '0',
                                    100: '100'},
                                    value=[min_payload, max_payload]),

                                html.Div(dcc.Graph(id='success_payload_scatter_chart')),
                                ])


@app.callback([
    Output(component_id='success_pie_chart', component_property='figure'),
    Output(component_id='success_payload_scatter_chart', component_property='figure'),
    Input(component_id='site_dropdown', component_property='value'),
    Input(component_id='payload_slider', component_property='value')]
    
              )

def get_pie_chart(entered_site, slider_input):
    filtered_df = spacex_df
    
    #Pie chart
    filtered_df['dummy'] = 1

    if entered_site == 'ALL':
        fig = px.pie(filtered_df, values='dummy', names='class', title='Launch Success Rate')
        success_pie_chart = fig
        
    else:
        filtered_df = filtered_df[ filtered_df['Launch Site'] == entered_site ]
        fig = px.pie(filtered_df, values='dummy', names='class', title='Launch Success Rate')
        success_pie_chart = fig

    
    #Scatter chart    
    f_df = filtered_df[filtered_df['Payload Mass (kg)'] >= float(slider_input[0])]
    f_df = f_df[f_df['Payload Mass (kg)'] <= float(slider_input[1])]

    scatter_fig = px.scatter(f_df, x='Payload Mass (kg)', y='class', 
    color='Booster Version', title='Success rate and Payload Mass (kg)')
                                
    success_payload_scatter_chart = scatter_fig

    return[success_pie_chart, success_payload_scatter_chart]
    

# Run the app
if __name__ == '__main__':
    app.run_server()
    
