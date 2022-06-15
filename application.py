# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, dash, html, dcc, dash_table
import pandas as pd
import pyodbc
import dash_bootstrap_components as dbc 
import plotly.graph_objects as go
#pd.options.plotting.backend = "plotly"

dash_app = dash.Dash() 
app = dash_app.server 

#Azure SQL Credentials
server = 'farmlinkinsights.database.windows.net' 
database = 'farmlinkdonorinsights' 
username = 'farmlinkadmin' 
password = 'Farmlink2021'  
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
query = "select [Fundraiser Full Name] as Name, sum(cast([Converted Payout Amount (USD)] as float)) as AmountRaised from fundraiseup.DonationsDataMain where [Campaign Name] = '2022 SUMMER FL P2P' group by [Fundraiser Full Name] order by 2 desc;"
df = pd.read_sql(query, cnxn)

kpiquery = "select sum(cast([Converted Payout Amount (USD)] as float)) as AmountRaised from fundraiseup.DonationsDataMain where [Campaign Name] = '2022 SUMMER FL P2P';"
kpidf = pd.read_sql(kpiquery, cnxn)

#df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')


def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


dash_app = Dash(__name__)
dash_app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

#Plotly Viz
fig = go.Figure(go.Indicator(
    mode = "number+gauge+delta",
    gauge = {'shape': "bullet"},
    #delta = {'reference': 300},
    #value = 220
    value = float(pd.unique(kpidf['AmountRaised']))
    ))

fig.update_layout(
    font_family="Tahoma",
    font_color="blue",
    title_font_family="Tahoma",
    title_font_color="red",
    legend_title_font_color="green"
), 

dash_app.layout =  html.Div([
    html.H4(children='2022 P2P Fundraising Results', style={'textAlign': 'left','fontFamily':'Tahoma'}), 
    dcc.Graph(
        id = 'Total Amount Raised',
        figure=fig 
    ),
    dash_table.DataTable(
        id='2022 Peer to Peer Fundraising Results',
        columns=[{"name": i, "id": i} for i in df.columns], 
        data = df.to_dict("records"), 
        export_format = "csv", 
        style_table={'maxHeight': '700px',
                     'overflowY': 'scroll'},
        style_cell = {"fontFamily": "Tahoma", "size": 11, 'textAlign': 'left'}
        )   
    
    ])


#KPI Dashboard



if __name__ == '__main__':
    dash_app.run_server(debug=True)


#Deploying to Azure
#https://www.phillipsj.net/posts/deploying-dash-to-azure-without-using-docker/