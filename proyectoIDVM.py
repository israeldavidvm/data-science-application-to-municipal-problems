# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc, Input, Output, dash_table
import plotly.express as px
import pandas as pd

def createListWithoutDuplicates(listWithDublicate):
    return list(set(listWithDublicate))

def generateTable(df,page_current=0,max_rows=10):
    return dash_table.DataTable(
        data=df.to_dict('records'),
        columns=None,
        page_action="native",
        page_current= page_current,
        page_size=  max_rows,
    )

def generateAnalysis1(data):
    analysis = ""
    
    maxUnresolvedProjects=0
    maxUnresolvedProjectsIndex=[]

    for m in range(0,len(data['province'])):

        if(data['unresolvedProjects'][m]>0 and data['unresolvedProjects'][m]==maxUnresolvedProjects):
            maxUnresolvedProjectsIndex.append(m)

        elif(data['unresolvedProjects'][m]>maxUnresolvedProjects):
            maxUnresolvedProjectsIndex=[m]
            maxUnresolvedProjects=data['unresolvedProjects'][m]
            # print(f"indice {m} detectado como maximo")
            # print(f"se detecto un valor igual a {data['unresolvedProjects'][m]} para {data['province'][m]} en el indice {m}")


        if(m==len(data['province'])-1 or data['province'][m]!=data['province'][m+1]):
            if len(maxUnresolvedProjectsIndex)==0:
                analysis += data['province'][m]+" no tienen proyectos no resueltos"
            else:
                for i in maxUnresolvedProjectsIndex:
                    analysis += data['province'][i] + " en la categoría de " + data['category'][i] + " subcategoría de " + data['subCategory'][i] + " que posee un total de " + str(data['unresolvedProjects'][i]) + " proyectos no resueltos,"
                    # print(f"se detecto un valor igual a {data['unresolvedProjects'][i]} para {data['province'][i]} en el indice {i}")

            maxUnresolvedProjects=0
            maxUnresolvedProjectsIndex=[]
            
    return analysis

def generateAnalysis2(data, province):

    analysis=f""

    if(len(province)!=0):
        analysis += f"Para la provincia {province} existen:"
    else:
        analysis += f"Entre todas las provincias existen:"
    
    for m in range(0,len(data['subCategory'])):

        if(len(province)!=0):
            analysis += f"{data['numProjects'][m]} en estatus de {data['status'][m]} en la subcategoria de {data['subCategory'][m]},"
        else:
            analysis += f"{data['numProjects'][m]} en estatus de {data['status'][m]} en la subcategoria de {data['subCategory'][m]},"


    return analysis


df = pd.read_excel('./reports_TEST.xlsx')
provinces=sorted(createListWithoutDuplicates(df['Provincia']))
categories=sorted(createListWithoutDuplicates(df['Categoria']))
subCategories=sorted(createListWithoutDuplicates(df['Subcategoria']))
status=sorted(createListWithoutDuplicates(df['Estatus']))

unresolvedProjectsByCategoryByProvince={
    "province":[],
    "unresolvedProjects":[],
    "category":[],
    "subCategory":[]
}
for province in provinces:
    for category in categories:
        for subCategory in subCategories:
            unresolvedProjectsByCategoryByProvince["province"].append(province)
            unresolvedProjectsByCategoryByProvince["category"].append(category)
            unresolvedProjectsByCategoryByProvince["subCategory"].append(subCategory)
            unresolvedProjectsByCategoryByProvince["unresolvedProjects"].append(
                len(df[
                    (df['Provincia'] == province) & 
                    (df['Categoria'] == category) & 
                    (df['Subcategoria'] == subCategory) & 
                    (df['Estatus'] != "Resuelto")
                    ])
            )

dfUnresolvedProjectsByCategoryByProvince=pd.DataFrame(unresolvedProjectsByCategoryByProvince)

fig = px.bar(
    dfUnresolvedProjectsByCategoryByProvince, 
    x="province", 
    y="unresolvedProjects", 
    color="subCategory", 
    pattern_shape="category",
    barmode="group",
    labels={
        'province':'Provincia',
        'category':'Categoria',
        'subCategory':'Subcategoria',
        'unresolvedProjects':'Cantidad Proyectos No Resueltos',
    },
    
)

analisysUnresolvedProjectsByCategoryByProvince=generateAnalysis1(unresolvedProjectsByCategoryByProvince)

resolvedProjectsBySubCategory={
    "resolvedProjects":[],
    "subCategory":[],
    "averageLifeTime":[]
}

for subCategory in subCategories:
    df2=df[(df['Subcategoria'] == subCategory) & (df['Estatus'] == "Resuelto")] 
    resolvedProjectsBySubCategory["subCategory"].append(subCategory)
    resolvedProjectsBySubCategory["resolvedProjects"].append(len(df2))
    resolvedProjectsBySubCategory["averageLifeTime"].append(
        (pd.to_datetime(df2["updatedAt"])-pd.to_datetime(df2["createdAt"])).mean().total_seconds()/86400
    )

dfResolvedProjectsBySubCategory=pd.DataFrame(resolvedProjectsBySubCategory)

fig2 = px.bar(
    dfResolvedProjectsBySubCategory, 
    x="subCategory", 
    y="averageLifeTime", 
    barmode="group",
    labels={
        'subCategory':'Subcategoria',
        'averageLifeTime':'Cantidad de Tiempo Promedio en dias para resolver un proyecto',
    },
    
)
app = Dash(__name__,title='data-science-application-to-municipal-problems')

app.layout = html.Main([

    html.Header(children=[
        html.Div(children=[
            html.Span(
            children=[
                html.H1(children='data-science-application-to-municipal-problems',
                className="banner--modern__title"),
                html.P(
                    children='Desarrollador por: Israel David Villarroel Moreno',
                    className="banner--modern__description"
                    ),
            ],className='banner--modern__text'),

        ],className='banner--modern__content'),

        html.Img(src='/assets/investigacionOperaciones.jpg',className="banner--modern__background")

    ],className='banner--modern'),

    dcc.Tabs([
        dcc.Tab(label='Problemas Mas dificiles', children=[
            html.H2(children='Tipos de problemas que se nos han hecho más difícil de solucionar en cada estado'),
            dcc.Graph(
                id='graph-problemsMoreDifficult',
                figure=fig
            ),
            html.P(children="Como se puede observar en la gráfica los problemas mas dificiles (con una mayor cantidad de problemas no resueltos) para cada provincia son:"),
            html.P(children=analisysUnresolvedProjectsByCategoryByProvince),
        ]),
        dcc.Tab(label='Tiempos de Resolucion', children=[
            html.H2(children='Tiempo promedio de los problemas resueltos desde su momento de creación (reporte)'),
            dcc.Graph(
                id='graph-resolvedProyectTimes',
                figure=fig2
            )
        ]),
        
        dcc.Tab(label='Buscador de problemas por provincia', children=[
            html.Label('Buscador de problemas por provincias'),
            dcc.Dropdown(provinces,[],multi=False,id='select-province'),
            dcc.Graph(
                id='graph-projectsBySubCategory'    
            ),
            html.Div(id='container-table'),
            html.P(id='container-analisys'),
        ]),
    ])
],
className="publication--short"
)

@app.callback(
    Output(component_id='graph-projectsBySubCategory', component_property='figure'),
    Input(component_id='select-province', component_property='value'),
)
def update_graphProjectsBySubCategor(province):
    projectsBySubCategory={
        "numProjects":[],
        "subCategory":[],
        "status":[],
    }

    for subCategory in subCategories:

        for state in status:

            if(len(province)!=0):
        
                dfProjectBySubCategory=df[
                (df['Provincia'] == province) & 
                (df['Subcategoria'] == subCategory) &
                (df['Estatus']==state)
                ]

            else:

                dfProjectBySubCategory=df[
                (df['Subcategoria'] == subCategory) &
                (df['Estatus']==state)
                ]

            projectsBySubCategory["status"].append(state)
            projectsBySubCategory["subCategory"].append(subCategory)
            projectsBySubCategory["numProjects"].append(len(dfProjectBySubCategory))
    
    fig = px.bar(
        pd.DataFrame(projectsBySubCategory), 
        x="subCategory", 
        y="numProjects", 
        color="status", 
        barmode="group",
        labels={
            'status': "Estatus",
            'subCategory':'Subcategoria',
            'numProjects':'Cantidad Proyectos',
        },
    )

    return fig

@app.callback(
    Output(component_id='container-table', component_property='children'),
    Input(component_id='select-province', component_property='value'),
)
def update_TableByProvince(province):

    filteredDataFrame=df    
    
    if(len(province)!=0):
        
        filteredDataFrame=df[df['Provincia']==province]

    return generateTable(filteredDataFrame)

@app.callback(
    Output(component_id='container-analisys', component_property='children'),
    Input(component_id='select-province', component_property='value'),
)
def update_analysys2(province):
    projectsBySubCategory={
        "numProjects":[],
        "subCategory":[],
        "status":[],
    }

    for subCategory in subCategories:

        for state in status:

            if(len(province)!=0):
        
                dfProjectBySubCategory=df[
                (df['Provincia'] == province) & 
                (df['Subcategoria'] == subCategory) &
                (df['Estatus']==state)
                ]

            else:

                dfProjectBySubCategory=df[
                (df['Subcategoria'] == subCategory) &
                (df['Estatus']==state)
                ]

            projectsBySubCategory["status"].append(state)
            projectsBySubCategory["subCategory"].append(subCategory)
            projectsBySubCategory["numProjects"].append(len(dfProjectBySubCategory))

    return generateAnalysis2(projectsBySubCategory,province)


if __name__ == '__main__':
    app.run_server(debug=False)