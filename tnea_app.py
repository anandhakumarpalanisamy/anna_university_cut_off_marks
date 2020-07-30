#!/usr/bin/env python
# coding: utf-8

# # Python Libraries

# In[ ]:


import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import dash_table
import pandas as pd

import dash_bootstrap_components as dbc
import json

from dash.dependencies import Input, Output, State


# # Csv Data files

# In[ ]:


# Joined data of allotted list of all 4 rounds of anna university counselling, branch info and college info
tnea_csv_file = "assets/csv/joined_table.csv"


# # Read csv to a pandas dataframe and format it

# In[ ]:


alloted_list_df = pd.read_csv(tnea_csv_file)
alloted_list_df.drop('S.NO', axis=1, inplace=True)
alloted_list_df["COLLEGE CODE"] = pd.to_numeric(alloted_list_df["COLLEGE CODE"])


# # Generates plotly Data table which shows the cut off details

# In[ ]:


def generate_plotly_data_table(df,radio_button_value):
    '''
    table = dbc.Table.from_dataframe(df, 
                                     striped=True, 
                                     bordered=True, 
                                     hover=True,
                                     dark=True,
                                     responsive=True)
    return table
    
    
    '''
    #heading_string = 'Max Mark = ' + str(df['AGGR MARK'].iloc[0]) + ' | ' + "Min Mark = " + str(df['AGGR MARK'].iloc[-1])
    
    
    if radio_button_value == "Cut Off Marks":
        heading_string = "TNEA 2019 CUT OFF MARKS"
    else:
        heading_string = 'Total Students = '+ str(df.shape[0])
    return html.Div(children=[
                        #html.H4(children='Student Count = '+str(df.shape[0]),style={
                                                    #'text-align': 'center',
                                                    #'color' : 'green',
                                                    #'padding':'4px'
                                                  #}), 
                        html.H4(children=heading_string,style={
                                                    'text-align': 'center',
                                                    'color' : 'green',
                                                    'padding':'4px'
                                                  }),
                        dash_table.DataTable(
                                            id='datatable-interactivity',
                                            style_data={'whiteSpace': 'normal'},
                                            css=[{
                                                'selector': '.dash-cell div.dash-cell-value',
                                                'rule': 'display: inline; white-space: inherit; overflow: inherit; text-overflow: inherit;'
                                            }],
                                            columns=[
                                                {"name": i, "id": i, "deletable": True} for i in df.columns
                                            ],
                                            
                                            style_header={
                                                'backgroundColor': '#3DC2ED',
                                                'fontWeight': 'bold',
                                                'white-space': 'pre-wrap'
                                            },

                                            data=df.to_dict('records'),
                                            #editable=True,
                                            filter_action="native",
                                            sort_action="native",
                                            sort_mode="multi",
                                            #row_selectable="multi",
                                            #row_deletable=True,
                                            #selected_rows=[],
                                            page_action="native",
                                            page_current= 0,
                                            page_size= 18,
                                            style_data_conditional=[{
                                                'if': {'column_id': 'CUT OFF MARK'},
                                                'backgroundColor': '#3D9970',
                                                'color': 'white',
                                            }]
                                        ),
                        html.Div(id='datatable-interactivity-container')
                        ])

    


# # Adding meta tags to app to be discovered by google crawler

# In[ ]:


app_meta_tags =[
                    # A description of the app, used by e.g.
                    # search engines when displaying search results.
                    {
                        'name': 'description',
                        'content': 'tnea 2019 cut off , anna university 2019 cut off , tamil nadu engineering admissions 2019 cut offs, tnea 2019 cut off marks, anna university counselling cut off marks, tnea 2020 cut off marks, tnea previous year cut off marks, anna university previous year cut off'
                    },
                    {
                        'name': 'keywords',
                        'content': 'tnea 2019 cut off,anna university 2019 cut off, anna university cut off , 2019 cut off for anna university, anna university 2019 cut off, tnea 2019 cut off, tnea 2019 cut off marks,tnea 2019 cut off , anna university 2019 cut off , tamil nadu engineering admissions 2019 cut offs, tnea 2019 cut off marks, anna university counselling cut off marks, tnea 2020 cut off marks, tnea previous year cut off marks, anna university previous year cut off'
                    },
                    {
                        'name': 'google-site-verification',
                        'content': 'X7KxETg-LS3TyR1O4AWzv30G0M-xVQKEgmuOjhXfOB0'
                    },
                    # A tag that tells Internet Explorer (IE)
                    # to use the latest renderer version available
                    # to that browser (e.g. Edge)
                    {
                        'http-equiv': 'X-UA-Compatible',
                        'content': 'IE=edge'
                    },
                    # A tag that tells the browser not to scale
                    # desktop widths to fit mobile screens.
                    # Sets the width of the viewport (browser)
                    # to the width of the device, and the zoom level
                    # (initial scale) to 1.
                    #
                    # Necessary for "true" mobile support.
                    {
                      'name': 'viewport',
                      'content': 'width=device-width, initial-scale=1.0'
                    }
                ]


# # External css for the app

# In[ ]:


# external CSS stylesheets
external_stylesheets = [
    "https://unpkg.com/tachyons@4.10.0/css/tachyons.min.css",
]


# # Initialise dash app

# In[ ]:


app = dash.Dash(__name__,meta_tags=app_meta_tags,external_stylesheets=external_stylesheets)
app.title='Tnea 2019 cut off marks - Anna University 2019 cut off marks'
server = app.server


# # App Layout Design Details

# In[ ]:


app.layout = dcc.Loading(
    children=[html.Div(children=[
                                html.H1(children='TNEA 2019 Cut Off Marks',style={
                                                    'text-align': 'center',
                                                    'background-color': '#5274a0',
                                                    'color' : 'white',
                                                    'padding':'18px'
                                                  }),
                                
                
                                #html.H4(children='TNEA 2019 Cut Offs'),
    
                                html.P(children='Filter by College Code :',style={'padding':'4px',
                                                                                 'font-weight': 'bold',
                                                                                'color': '#2c1fcc'
                                                  }),
    
                                html.P(id='college_label',style={
                                                    'text-align': 'center',
                                                    'color' : 'green',
                                                    'padding':'4px'
                                                  }),
    
    
                                dcc.Dropdown(id='dropdown',
                                             options=[
                                                        {'label': i, 'value': i} for i in sorted(alloted_list_df['COLLEGE CODE'].unique())
                                                    ], 
                                             multi=False, 
                                             placeholder='Filter by College Code...'),
    
                                
    
                                html.P(children='Filter by College Name :',style={'padding':'4px',
                                                                                 'font-weight': 'bold',
                                                                                'color': '#2c1fcc'
                                                  }),
    
                                dcc.Dropdown(id='dropdown5',
                                             options=[
                                                        {'label': i, 'value': i} for i in sorted(alloted_list_df['COLL_NAME'].unique())
                                                    ], 
                                             value='UNIVERSITY DEPARTMENTS OF ANNA UNIVERSITY, CHENNAI - CEG CAMPUS', 
                                             multi=False, 
                                             placeholder='Filter by College Name...'),
    
                                html.P(children='Filter by Branch Code :',style={'padding':'4px',
                                                                                 'font-weight': 'bold',
                                                                                'color': '#2c1fcc'
                                                  }),
    
                                 html.P(id='branch_label',style={
                                                    'text-align': 'center',
                                                    'color' : 'green',
                                                    'padding':'4px'
                                                  }),
    
    
                                dcc.Dropdown(id='dropdown3',
                                             options=[
                                                        {'label': i, 'value': i} for i in sorted(alloted_list_df['BRANCH CODE'].unique())
                                                    ], 
                                             multi=True, 
                                             placeholder='Filter by Branch Code...'),
    
                               
    
                                html.P(children='Filter by Branch Name :',style={'padding':'4px',
                                                                                 'font-weight': 'bold',
                                                                                'color': '#2c1fcc'
                                                  }),
                                dcc.Dropdown(id='dropdown4',
                                             options=[
                                                        {'label': i, 'value': i} for i in sorted(alloted_list_df['BRANCH_NAME'].unique())
                                                    ], 
                                             multi=True, 
                                             placeholder='Filter by Branch Name...'),
    
                                html.P(children='Filter by Community Code :',style={'padding':'4px',
                                                                                 'font-weight': 'bold',
                                                                                'color': '#2c1fcc'
                                                  }),
    
                                html.P(id='community_label',style={
                                                    'text-align': 'center',
                                                    'color' : 'green',
                                                    'padding':'4px'
                                                  }),
    
    
                                dcc.Dropdown(id='dropdown2',
                                             options=[
                                                        {'label': i, 'value': i} for i in sorted(alloted_list_df['ALLOTTED CATEGORY'].unique())
                                                    ], 
                                             multi=False, 
                                             value='OC',
                                             placeholder='Filter by Community Code...'),
        
        
                                html.P(children='Filter by Cut Off Mark :',style={'padding':'4px',
                                                                                 'font-weight': 'bold',
                                                                                'color': '#2c1fcc'
                                                  }),
        
                             html.P(id='mark_label',style={
                                                    'text-align': 'center',
                                                    'color' : 'green',
                                                    'padding':'4px'
                                                  }),
                               dcc.Dropdown(id='mark_filter',
                                            
                                             options=[
                                                        {'label': i, 'value': i} for i in sorted([x * 0.25 for x in range(1, 801)], reverse=True)

                                                    ], 
                                             multi=False, 
                                             value=200,
                                             placeholder='Filter by Cut Off Mark...'),
                                
    
        
    
                                dcc.RadioItems(id='radio_button',
                                                style={
                                                    'text-align': 'center',
                                                    'color' : 'green',
                                                    'padding':'4px',
                                                    'font-weight': 'bold',
                                                    'margin-top':'20px',
                                                  },
                                                inputStyle={
                                                    "margin-right": "5px", 
                                                    "margin-left": "15px",
                                                },
                                                options=[
                                                        {'label': 'Cut Off Marks', 'value': 'Cut Off Marks'},
                                                        {'label': 'Full Student List', 'value': 'Full Student List'},
                                                ],
                                                value='Cut Off Marks',
                                                labelStyle={'display': 'inline-block'}
                                                ),  
                              
    
                                html.Div(id='table-container'),
                                #html.Div(id='bootstrap-table-container'),
                                html.H4(children='Downloads'),
                                html.A(
                                            'Sports Alloted List',
                                            id='Sports Alloted List',
                                            download="sports_allotted_list.pdf",
                                            href=app.get_asset_url('./pdf/sports_allotted_list.pdf'),
                                            target="_blank"
                                        ),
                                html.A(
                                            'Ex-Servicemen Allotted List',
                                            id='Ex-Servicemen Allotted List',
                                            download="ex-servicemen_Allotted_List.pdf",
                                            href=app.get_asset_url('./pdf/ex-servicemen_Allotted_List.pdf'),
                                            target="_blank"
                                        ),
                                html.A(
                                            'Differently Abled Allotted List',
                                            id='Differently Abled Allotted List',
                                            download="differently_abled_allotted_list.pdf",
                                            href=app.get_asset_url('./pdf/differently_abled_allotted_list.pdf'),
                                            target="_blank"
                                        ),
                                html.A(
                                            'Allotted List Round 1',
                                            id='Allotted List Round 1',
                                            download="allotted_list_round_1.pdf",
                                            href=app.get_asset_url('./pdf/allotted_list_round_1.pdf'),
                                            target="_blank"
                                        ),
                                html.A(
                                            'Allotted List Round 2',
                                            id='Allotted List Round 2',
                                            download="allotted_list_round_2.pdf",
                                            href=app.get_asset_url('./pdf/allotted_list_round_2.pdf'),
                                            target="_blank"
                                        ),
    
                                html.A(
                                            'Allotted List Round 3',
                                            id='Allotted List Round 3',
                                            download="allotted_list_round_3.pdf",
                                            href=app.get_asset_url('./pdf/allotted_list_round_3.pdf'),
                                            target="_blank"
                                      ),
                                html.A(
                                            'Allotted List Round 4',
                                            id='Allotted List Round 4',
                                            download="allotted_list_round_4.pdf",
                                            href=app.get_asset_url('./pdf/allotted_list_round_4.pdf'),
                                            target="_blank"
                                        ),
                            ])], type='cube', fullscreen=True)


# # Handle filter option for mark

# In[ ]:


@app.callback(
            dash.dependencies.Output('mark_label', 'children'),
            [dash.dependencies.Input('mark_filter', 'value')])
def drop_down_value1(mark_filter_value):
    mark_label = None
    if mark_filter_value is not None:
        mark_label = mark_filter_value
    return mark_label


# # Handle filter option for college

# In[ ]:


@app.callback(
            dash.dependencies.Output('college_label', 'children'),
            [dash.dependencies.Input('dropdown', 'value')])
def drop_down_value1(dropdown_value):
    college_name = None
    if dropdown_value is not None:
        college_name_df = alloted_list_df.loc[alloted_list_df['COLLEGE CODE'] == dropdown_value]
        if college_name_df.shape[0] > 0:
            college_name = college_name_df['COLL_NAME'].iloc[0]
    return college_name


# # Handle filter option for branch

# In[ ]:


@app.callback(
            dash.dependencies.Output('branch_label', 'children'),
            [dash.dependencies.Input('dropdown3', 'value')])
def drop_down_value2(dropdown_value):
    branch_name = []
    if dropdown_value is not None:
        branch_name_df = alloted_list_df.loc[alloted_list_df['BRANCH CODE'].isin(dropdown_value)]
        if branch_name_df.shape[0] > 0:
            branch_name = branch_name_df['BRANCH_NAME'].unique().tolist()
    return ', '.join(branch_name)


# # Handle filter option for Community

# In[ ]:



@app.callback(
            dash.dependencies.Output('community_label', 'children'),
            [dash.dependencies.Input('dropdown2', 'value')])
def drop_down_value3(dropdown_value):
    return dropdown_value


# # Update college code when college name is changed

# In[ ]:


@app.callback(
            dash.dependencies.Output('dropdown', 'value'),
            [dash.dependencies.Input('dropdown5', 'value')])
def drop_down_value4(dropdown_value):
    if dropdown_value is not None:
        college_code = alloted_list_df.loc[alloted_list_df['COLL_NAME'] == dropdown_value]['COLLEGE CODE'].iloc[0]
        return college_code
    else:
        return None


# # Update Branch codes when branch names are changed

# In[ ]:


@app.callback(
            dash.dependencies.Output('dropdown3', 'value'),
            [dash.dependencies.Input('dropdown4', 'value'),
            dash.dependencies.Input('dropdown4', 'options')])
def drop_down_value5(dropdown_value,dropdown4_options):
    if dropdown_value is not None:
        dropdown4_list = []
        for x in dropdown4_options:
            dropdown4_list.append(x['value'])
        dropdown_value = list(set(dropdown_value) & set(dropdown4_list))
        if len(dropdown_value)>0:
            branch_code = alloted_list_df.loc[alloted_list_df['BRANCH_NAME'].isin(dropdown_value)]['BRANCH CODE'].unique().tolist()
            return branch_code
        else:
            return None
    else:
        return None


# # List branch codes that are available in the selected college

# In[ ]:


@app.callback(
            dash.dependencies.Output('dropdown3', 'options'),
            [dash.dependencies.Input('dropdown', 'value')])
def drop_down3_options(dropdown_value):
    
    if dropdown_value is not None:
        filtered_df = alloted_list_df.loc[alloted_list_df['COLLEGE CODE'] == dropdown_value]
        options=[
                {"label": i, "value": i} for i in sorted(filtered_df['BRANCH CODE'].unique())
            ]
        
        return options
    else:
        options=[
                    {"label": i, "value": i} for i in sorted(alloted_list_df['BRANCH CODE'].unique())
                ]
        return options


# # List branch names that are available in the selected college

# In[ ]:


@app.callback(
            dash.dependencies.Output('dropdown4', 'options'),
            [dash.dependencies.Input('dropdown', 'value')])
def drop_down4_options(dropdown_value):
    if dropdown_value is not None:
        filtered_df = alloted_list_df.loc[alloted_list_df['COLLEGE CODE'] == dropdown_value]
        options=[
                {"label": i, "value": i} for i in sorted(filtered_df['BRANCH_NAME'].unique())
            ]
        
        return options
    else:
        options=[
                    {"label": i, "value": i} for i in sorted(alloted_list_df['BRANCH_NAME'].unique())
                ]
        return options


# # Update plotly data-table based on the filtered options

# In[ ]:


@app.callback(
            dash.dependencies.Output('table-container', 'children'),
            [dash.dependencies.Input('dropdown', 'value'),
             dash.dependencies.Input('dropdown2', 'value'),
             dash.dependencies.Input('dropdown3', 'value'),
             dash.dependencies.Input('radio_button', 'value'),
             dash.dependencies.Input('mark_filter', 'value'),
            ])
def display_table(dropdown_value,dropdown_value2,dropdown_value3,radio_button_value,mark_filter_value):
    filtered_df = alloted_list_df
    if mark_filter_value is not None:
        filtered_df = filtered_df.loc[filtered_df['AGGR MARK'] <= mark_filter_value]
    if dropdown_value is not None:
        filtered_df = filtered_df.loc[filtered_df['COLLEGE CODE'] == dropdown_value]
    if dropdown_value2 is not None:
        filtered_df = filtered_df.loc[filtered_df['ALLOTTED CATEGORY'] == dropdown_value2]
    if dropdown_value3 is not None:
        #filtered_df = filtered_df.loc[filtered_df['BRANCH CODE'] == dropdown_value3]
        if len(dropdown_value3) > 0:
            filtered_df = filtered_df[filtered_df['BRANCH CODE'].isin(dropdown_value3)]
        
    if radio_button_value == "Cut Off Marks":
        filtered_df["OVER ALL RANK"] = pd.to_numeric(filtered_df["OVER ALL RANK"], errors='coerce')
        #print(filtered_df.shape,filtered_df['OVER ALL RANK'].isna().sum())
        filtered_df = filtered_df.loc[filtered_df.groupby(["COLLEGE CODE","ALLOTTED CATEGORY","BRANCH CODE"])["OVER ALL RANK"].idxmax()]
        
        #filtered_df["OVER ALL RANK"] = filtered_df['OVER ALL RANK'].astype(int)
        #filtered_df["OVER ALL RANK"] = pd.to_numeric(filtered_df["OVER ALL RANK"], errors='coerce')
        filtered_df = filtered_df.sort_values(by=['OVER ALL RANK'],ascending=True)
        '''
        filtered_df = filtered_df.drop_duplicates(subset =["COLLEGE CODE","ALLOTTED CATEGORY","BRANCH CODE"], 
                                         keep = "last", 
                                         inplace = False)
        '''
        #print(filtered_df)
        if dropdown_value2 == 'OC':
            filtered_df = filtered_df[['COLLEGE CODE','COLL_NAME',
                                   #'COMMUNITY',
                                   'ALLOTTED CATEGORY',
                                   'BRANCH CODE', 'BRANCH_NAME',
                                   'OVER ALL RANK', 
                                   #'COMMUNITY RANK', 
                                   'AGGR MARK','COUNSELLING ROUND']]
        else:
            filtered_df = filtered_df[['COLLEGE CODE','COLL_NAME',
                                       #'COMMUNITY',
                                       'ALLOTTED CATEGORY',
                                       'BRANCH CODE', 'BRANCH_NAME',
                                       'OVER ALL RANK', 'COMMUNITY RANK', 
                                       'AGGR MARK','COUNSELLING ROUND']]
        filtered_df.rename({'ALLOTTED CATEGORY': 'COMMUNITY'}, axis=1, inplace=True)

    #print(dropdown_value,dropdown_value2,dropdown_value3,radio_button_value)
    #print(filtered_df.shape,alloted_list_df.shape)
    filtered_df.rename({'AGGR MARK': 'CUT OFF MARK'}, axis=1, inplace=True)
    return generate_plotly_data_table(filtered_df,radio_button_value)


# # Start the app

# In[ ]:


if __name__ == '__main__':
    app.run_server(debug=False,threaded=True,port=9007,host='0.0.0.0')


# In[ ]:




