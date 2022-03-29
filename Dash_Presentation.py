
import dash
from dash import html 
from dash import dcc 
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output 
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np



app = dash.Dash(external_stylesheets=[dbc.themes.YETI])

server = app.server


colors = {
    'background': 'rgb(37, 59, 128)',  
    'text': 'rgba(255, 255, 255, 1)',
    'template': 'plotly_white',
    'paper': 'rgb(37, 59, 128)',
    'plot': 'rgb(41, 151, 216)'
}


df = pd.read_csv('DestinationCountByCountry.csv')
df1 = pd.read_excel('travel_insurance.xlsx')


def NetSalesVScomission():
    fig = px.scatter(df1, x = 'Net Sales', y = 'Commision (in value)', 
        color = 'Agency', template = colors['template'], 
        title = 'Net Sales and Comission (in value) Relation by Agency',
        width = 1000,
        height = 650).update_layout(
        paper_bgcolor = colors['paper'], 
        plot_bgcolor = colors['plot'])   
    fig.update_layout(
        title_x = 0.5,
        font=dict(
            size=25,
            color=colors['text']
        )
    )
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="white",
            font_size=32,
            font_family="Rockwell"
        )
    )
    fig.update_traces(marker=dict(size=12,
        line=dict(width=2,
            color='DarkSlateGrey')),
        selector=dict(mode='markers'))
    return fig


def NetSalesVScomission2():
    fig = px.scatter(df1, x = 'Net Sales', y = 'Commision (in value)', 
        color = 'Agency Type', template = colors['template'], 
        title = 'Net Sales and Comission (in value) Relation by Agency Type',
        width = 1000,
        height = 650).update_layout(
        paper_bgcolor = colors['paper'], 
        plot_bgcolor = colors['plot'])   
    fig.update_layout(
        title_x = 0.5,
        font=dict(
            size=25,
            color=colors['text']
        )
    )
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="white",
            font_size=32,
            font_family="Rockwell"
        )
    )
    fig.update_traces(marker=dict(size=12,
        line=dict(width=2,
            color='DarkSlateGrey')),
        selector=dict(mode='markers'))
    return fig


def AgencyTypeCount(key=None):
    if key == 'Claims':
        df = df1[df1['Claim']=='Yes']
        title = 'Insurance Claims by Agency Type'
    else: 
        df = df1
        title = 'Insurance Sales by Agency Type'
    fig = px.histogram(
        df, 
        x="Agency Type", 
        color = 'Agency Type', 
        text_auto = True, 
        title = title,
        height=650, 
        width = 1000, 
        template = colors['template']).update_layout(
        paper_bgcolor = colors['paper'],
        plot_bgcolor = colors['plot'])
    fig.update_layout(
        title_x = 0.5,
        font=dict(
            size=25,
            color=colors['text']
        )
    )
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="white",
            font_size=32,
            font_family="Rockwell"
        )
    )
    fig.update_traces(
        marker_line_color='rgb(0,0,0,1)',
        marker_line_width=2.5, opacity=1)
    return fig


def DistributionChannelCount(key=None):
    if key == 'Claims':
        df = df1[df1['Claim']=='Yes']
        title = 'Insurance Claims by Distribution Channel'
    else: 
        df = df1
        title = 'Insurance Sales by Distribution Channel'
    fig = px.histogram(
        df, 
        x="Distribution Channel", 
        color = 'Distribution Channel', 
        text_auto = True, 
        title = title,
        height=650, 
        width = 1000, 
        template = colors['template']).update_layout(
        paper_bgcolor = colors['paper'], 
        plot_bgcolor = colors['plot'])
    fig.update_layout(
        title_x = 0.5,
        font=dict(
            size=25,
            color=colors['text']
        )
    )
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="white",
            font_size=32,
            font_family="Rockwell"
        )
    )    
    fig.update_traces(
        marker_line_color='rgb(0,0,0,1)',
        marker_line_width=2.5, opacity=1)
    return fig


def AgencyCount(key=None):
    if key == 'Claims':
        df = df1[df1['Claim']=='Yes']
        title = 'Insurance Claims by Agency'
    else: 
        df = df1
        title = 'Insurance Sales by Agency'
    aux_df = df.groupby(['Agency', 'Agency Type']).size().reset_index(name='Count').sort_values('Count', ascending=False)
    fig = px.bar(
        aux_df,
        x="Agency", 
        y = 'Count',
        color = 'Agency',
        text_auto = True, 
        hover_name = 'Agency Type',
        title = title,
        height=650, 
        width = 1000, 
        template = colors['template']).update_layout(
        paper_bgcolor = colors['paper'],  
        plot_bgcolor = colors['plot'])
    fig.update_layout(
        title_x = 0.5,
        font=dict(
            size=25,
            color=colors['text']
        )
    )
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="white",
            font_size=32,
            font_family="Rockwell"
        )
    )
    fig.update_traces(
        marker_line_color='rgb(0,0,0,1)',
        marker_line_width=2.5, opacity=1)
    return fig


def GenderCount(): 
    df = df1.fillna('Not Informed')
    fig = px.histogram(
        df, 
        x='Gender', 
        color = 'Gender', 
        text_auto = True, 
        facet_col = 'Claim',
        title = 'Insurance Sales and Claim by Gender(and Funny Fact!)',
        height=650, 
        width = 1000,
        template = colors['template']).update_layout(
        paper_bgcolor = colors['paper'],  
        plot_bgcolor = colors['plot'])
    fig.update_layout(
        title_x = 0.5,
        font=dict(
            size=25,
            color=colors['text']
        )
    )
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="white",
            font_size=32,
            font_family="Rockwell"
        )
    )
    fig.update_traces(
        marker_line_color='rgb(0,0,0,1)',
        marker_line_width=2.5, opacity=1)
    return fig


def DestinationCount(key=None):
    if key == 'Claims':
        df = df1[df1['Claim']=='Yes']
        title = 'Insurance Claims by Destination'
    else: 
        df = df1
        title = 'Insurance Sales by Destination'
    aux_df = df.groupby('Destination').size().reset_index(name='Count').sort_values('Count', ascending=False).head(10) 
    fig = px.bar(
        aux_df, 
        x="Destination", 
        y = 'Count', 
        color = 'Destination',
        text_auto = True, 
        title = title,
        height=650, 
        width = 1000,
        template = colors['template']).update_layout(
        paper_bgcolor = colors['paper'],  
        plot_bgcolor = colors['plot'])
    fig.update_layout(
        title_x = 0.5,
        font=dict(
            size=20,
            color=colors['text']
        )
    )
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="white",
            font_size=32,
            font_family="Rockwell"
        )
    )
    fig.update_traces(
        marker_line_color='rgb(0,0,0,1)',
        marker_line_width=2.5, opacity=1)
    return fig  


def C2BClaims():
    df = df1.loc[df1['Claim']=='Yes']
    df = df.groupby(by=["Agency"]).size().reset_index(name="counts").head(10)
    fig = px.pie(
        df, 
        values='counts', 
        names='Agency', 
        title='Most Claimed Agencies',
        height=650, 
        width = 650,
        template = colors['template']).update_layout(
        paper_bgcolor = colors['paper'],  
        plot_bgcolor = colors['plot'])
    fig.update_layout(
        title_x = 0.5,
        font=dict(
            size=20,
            color=colors['text']
        )
    )
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="white",
            font_size=32,
            font_family="Rockwell"
        )
    )
    fig.update_traces(
        marker_line_color='rgb(0,0,0,1)',
        marker_line_width=2.5, opacity=1)
    return fig


def table1():
    return df1.head()


def table2():
    aux_df = df1.groupby(['Agency'])['Claim'].value_counts().reset_index(name='Count')
    aux_df = aux_df.pivot(index = ['Agency'], columns = 'Claim', values = 'Count')
    aux_df['ClaimProp'] = (aux_df['Yes']/(aux_df['Yes'] + aux_df['No'])).round(4)
    return aux_df[aux_df['ClaimProp'] > 0].sort_values('ClaimProp', ascending=False).head(5).reset_index()

def table3():
    return df1[df1['Agency'] == 'C2B'].head(5)


header = html.Div(
    id="app-header",
    children=[
        html.H1(
            children = "Flight Ensurance Claim Study",
            style = {
                'textAlign': 'center',
                'color':  colors['text'],
                'font-size': '48pt'
            }
        )
    ],   
)

app.layout = html.Div(
    style={'backgroundColor': colors['background']},
    children=[
        header,
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
    
        dbc.Row([
            dbc.Col(
                dcc.Dropdown(
                    id='dropdown1',
                    options = [
                        {'label': 'Normal', 'value' : 'Normal'},
                        {'label': 'Log(2)', 'value' : 'Log'}                
                    ],
                    placeholder='Select scale'        
                    ),
                width={'size': 6, 'offset': 6}
            ),
        ]),

        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    id="destination-count"
                    ),
                width={'size': 6, 'order': 2}
            ),
            dbc.Col(
                dcc.Markdown(children = """
                    # **The data consists in 63326 observations of Flight Insurance Claims Data, split into:** 


                    #### **Agency(the seller of the Insurance)**
                    #### **Agency Type(if the insurance was sold by an Airline or by a Travel Agency)**
                    #### **Distribution Channel(if the Insurance was bought online or personally)**
                    #### **Product Name(the name of the insurance product)**
                    #### **Claim(if the insurance was claimed or not)**
                    #### **Duration(Duration of the insured flight)**
                    #### **Destination(Destination of the insured flight)**
                    #### **Net Sales(revenue adquired by that Insurance sale)**
                    #### **Comission(Comission paid to the seller of the Insurance)**
                    #### **Gender(the gender of the insured)**
                    #### **Age(age of the insured)**                    
                """,
                style = {
                    'textAlign': 'center',
                    'color':  colors['text'],
                    'font-size': '48pt'
                    }
                ),
                width={'size': 5, 'order': 1, 'offset': 1}
            )
        ]),
        
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),

        dbc.Row(
            dbc.Col(
                dash.dash_table.DataTable(table1().to_dict('records'), [{'name': i, 'id': i} for i in table1().columns], 
                    style_data={'font-size': '20pt', 'border': '5px solid black'}, 
                    style_header={'font-size': '20pt', 'border': '5px solid black'},
                    style_data_conditional=[{
                        'backgroundColor': colors['background'],
                        'color': 'white'
                    }],
                    style_header_conditional=[{
                        'backgroundColor': colors['background'],
                        'color': 'white'
                    }],                
                ),
                width={'size': 10, 'offset': 1}              
            )
        ),        

        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),

        dbc.Row([
            dbc.Col(
                dcc.Markdown(children="""
                    # **DESCRIPTIVE STATISTICS**
                    """,
                    style = {
                        'textAlign': 'center',
                        'color':  colors['text'],
                        'font-size': '48pt'
                        }
                    ),
                    width={'size': '12'}
              ),
        ]),

        html.Br(),
        html.Br(),

        dbc.Row([
            dbc.Col(
                dcc.Markdown(children="""
                    ### Strange thing here, Airlines having almost twice Claims when it has nearly 1/3 sales
                """,
                    style = {
                        'textAlign': 'center',
                        'color':  colors['text'],
                        'font-size': '48pt'
                        }
                    ),
                    width={'size': '6', 'offset': 5}
            )
        ]),

        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    id="AgencyTypeCount-hist",
                    figure = AgencyTypeCount()
                    ),
                width={'size': 6, 'order': 1}                 
            ),

            dbc.Col(
                dcc.Graph(
                    id="AgencyTypeCountClaims-hist", 
                    figure = AgencyTypeCount('Claims')
                    ),
                width={'size': 6, 'order': 2}                 
            ),
        ]),

        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),

        dbc.Row([
            dbc.Col(
                dcc.Markdown(children="""
                    ### Nothing wrong here, except for the changed colors 
                """,
                    style = {
                        'textAlign': 'center',
                        'color':  colors['text'],
                        'font-size': '48pt'
                        }
                    ),
                    width={'size': '12'}
            )
        ]),

        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    id="DistributionChannelCount-hist",
                    figure = DistributionChannelCount()
                    ),
                width={'size': 6, 'order': 1}                 
            ),            
            dbc.Col(
                dcc.Graph(
                    id="DistributionChannelCountClaims-hist",
                    figure = DistributionChannelCount('Claims')
                    ),
                width={'size': 6, 'order': 2}

            ),
        ]),

        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),


        dbc.Row([
            dbc.Col(
                dcc.Markdown(children="""
                    ### C2B Agency has more than half of all claims(its's 927 in total)
                """,
                    style = {
                        'textAlign': 'center',
                        'color':  colors['text'],
                        'font-size': '48pt'
                        }
                    ),
                    width={'size': '6', 'offset': 5}
            )
        ]),

        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    id="AgencyCount-hist", 
                    figure = AgencyCount()
                    ),
                width={'size': 6, 'order': 1}  
            ),
            dbc.Col(
                dcc.Graph(
                    id="AgencyCountClaims-hist", 
                    figure = AgencyCount('Claims')
                    ),
                width={'size': 6, 'order': 2} 
            ),
        ]),

        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),

        dbc.Row([
            dbc.Col(
                dcc.Graph(id='C2BClaims-pie',
                figure = C2BClaims()
                ),
            width={'size': 4, 'order': 1, 'offset': 1}

            ),
            dbc.Col(
                dcc.Markdown(children="""
                    ### **If we subtract C2B claims from all claims on Singapore, there would be only 15 claims left for all other companies. This leaves C2B as the Airline with highest claim probability, with a 547/8267=6.6% claim prob.**
                """,
                    style = {
                        'textAlign': 'center',
                        'color':  colors['text'],
                        'font-size': '48pt'
                        }
                    ),
                    width={'size': '3', 'order': 2}
            ),
            dbc.Col(
                dash.dash_table.DataTable(table2().to_dict('records'), [{'name': i, 'id': i} for i in table2().columns], 
                    style_data={'font-size': '20pt', 'border': '5px solid black'}, 
                    style_header={'font-size': '20pt', 'border': '5px solid black'},
                    style_data_conditional=[{
                        'backgroundColor': colors['background'],
                        'color': 'white'
                    }],
                    style_header_conditional=[{
                        'backgroundColor': colors['background'],
                        'color': 'white'
                    }],                
                ),
                width={'size': 3, 'order': 3}              
            )
        ]),

        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),

        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    id = 'DestinationCount-hist',
                    figure=DestinationCount()
                    ),
                width={'size': 6, 'order': 1}
            ),

            dbc.Col(
                dcc.Graph(
                    id = 'DestinationCountClaims-hist',
                    figure=DestinationCount('Claims')
                    ),
                width={'size': 6, 'order': 2}
            )
        ]),

        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),

        dbc.Row([
            dbc.Col(
                dash.dash_table.DataTable(table3().to_dict('records'), [{'name': i, 'id': i} for i in table3().columns], 
                    style_data={'font-size': '20pt', 'border': '5px solid black'}, 
                    style_header={'font-size': '20pt', 'border': '5px solid black'},
                    style_data_conditional=[{
                        'backgroundColor': colors['background'],
                        'color': 'white'
                    }],
                    style_header_conditional=[{
                        'backgroundColor': colors['background'],
                        'color': 'white'
                    }],                
                ),
                width={'size': 8, 'order': 1, 'offset': 2}              
            )
        ]),
    
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),

        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    id = 'Gendergraph-hist',
                    figure=GenderCount()
                ),
            width={'size': 6, 'order': 1, 'offset': 1}
            ),
            dbc.Col(
                dcc.Markdown(children="""
                   ## **Apparently, sales with an informed gender have a bigger chance of being claimed**
                """,
                    style = {
                        'textAlign': 'center',
                        'color':  colors['text'],
                        'font-size': '48pt'
                        }
                    ),
                width={'size': 3, 'order': 2}
            )
        ]),

        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),

        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    id="netsalescomission-scatter",
                    figure = NetSalesVScomission(),             
                    ),
                width={'size': 6, 'order': 1}
            ),     
            dbc.Col(
                dcc.Graph(
                    id="netsalescomission-scatter2",
                    figure = NetSalesVScomission2()
                    ),
                width={'size': 6, 'order': 2}  
            ),
        ]),

    ],
)


@app.callback(
    Output(component_id='destination-count', component_property='figure'),
    Input(component_id='dropdown1', component_property='value')
)

def choroMap(selected_type):
    
    df = pd.read_csv('DestinationCountByCountry.csv')

    if selected_type == 'Normal':
        df = df
    elif selected_type == 'Log':
        df['Count'] = np.log2(df['Count'])

    fig = px.choropleth(df, 
                        locations = 'CountryCode', 
                        color = 'Count', 
                        hover_name = 'Country',
                        color_continuous_scale = px.colors.sequential.Plasma,
                        title = 'DESTINATIONS COUNT',
                        template = colors['template'],
                        width = 1300,
                        height = 700).update_layout(
                        paper_bgcolor = colors['paper'], 
                        plot_bgcolor = colors['plot'])
                                    
    # fig.update_layout({
    #     'geo': {
    #         'resolution': 50
    #     },
    # })
    fig.update_layout(
        title_x = 0.5,
        font=dict(
            size=25,
            color=colors['text']
        ),
        geo=dict(bgcolor= colors['plot'])
    )

    return fig


if __name__ == "__main__":
    app.run_server(debug=True)


