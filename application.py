from azure.storage.blob import ContainerClient
from io import StringIO
import pandas as pd
from dash import Dash, dash, html, dcc, dash_table
import dash_bootstrap_components as dbc
import plotly.graph_objects as go 


dash_app = dash.Dash() 
app = dash_app.server 

#app = dash.Dash(__name__)
#server = app.server

#Connecting to data in Blob Storage for overall data

conn_str = "Enter connection string from the Azure Portal -- Storage Account :: This is on the portal"
container = "Enter container name"
blob_name = "Enter blob name"

container_client = ContainerClient.from_connection_string(conn_str=conn_str, container_name=container)
downloaded_blob = container_client.download_blob(blob_name)

df = pd.read_csv(StringIO(downloaded_blob.content_as_text()))


conn_str = "Enter connection string from the Azure Portal -- Storage Account"
container = "Enter container name"
blob_name = "Enter blob name"

container_client = ContainerClient.from_connection_string(conn_str=conn_str, container_name=container)
downloaded_blob = container_client.download_blob(blob_name)

kpidf = pd.read_csv(StringIO(downloaded_blob.content_as_text()))

#dash_app = Dash(__name__)


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



#Plotly Viz
fig = go.Figure(go.Indicator(
    mode = "number+gauge+delta",
    gauge = {'shape': "bullet"},
    delta = {'reference': float(pd.unique(kpidf['FundRaisingGoal']))},
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
