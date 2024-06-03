import dash
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output, State
import pandas as pd
import plotly.express as px
import io
import base64

# Инициализация Dash приложения
app = dash.Dash(__name__)

# Загрузка и обработка данных
df = pd.read_csv(r'C:\Users\Ксения\PycharmProjects\pythonProject3\sunset.csv', sep=';')

# Проверка наличия данных
if df.empty:
    raise ValueError("DataFrame пуст")

# Проверка форматирования дат
try:
    df['date'] = pd.to_datetime(df['date'], format='%d.%m.%Y')
except Exception as e:
    print(f"Ошибка при форматировании даты: {e}")

# Layout дашборда
app.layout = html.Div([
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Перетащите CSV файл сюда или ',
            html.A('нажмите здесь', style={'color': 'blue'})
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        multiple=False
    ),
    html.Div(id='output-data-upload'),
    dcc.Dropdown(
        id='time-period-dropdown',
        options=[
            {'label': 'Январь', 'value': 'january'},
            {'label': 'Февраль', 'value': 'february'},
            {'label': 'Март', 'value': 'march'},
            {'label': 'Апрель', 'value': 'april'},
            {'label': 'Все', 'value': 'all'}
        ],
        value='all'
    ),
    dash_table.DataTable(id='table'),
    dcc.Graph(id='line-chart'),
    html.Div(id='statistic-output'),
    html.Div(id='indicator-container')
])

# Callback для загрузки данных
@app.callback(Output('output-data-upload', 'children'),
              Input('upload-data', 'contents'),
              State('upload-data', 'filename'))
def update_output(contents, filename):
    if contents is not None:
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        try:
            if 'csv' in content_type:
                df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
            else:
                return html.Div(['Неподдерживаемый тип файла'])
        except Exception as e:
            print(e)
            return html.Div(['Ошибка при чтении файла: ' + str(e)])
    return html.Div([])

# Callback для обновления линейного графика и таблицы
@app.callback([Output('line-chart', 'figure'),
               Output('table', 'data')],
              Input('time-period-dropdown', 'value'))
def update_charts_and_table(time_period):
    if time_period == 'all':
        filtered_df = df
    elif time_period == 'january':
        filtered_df = df[df['date'].dt.month == 1]
    elif time_period == 'february':
        filtered_df = df[df['date'].dt.month == 2]
    elif time_period == 'march':
        filtered_df = df[df['date'].dt.month == 3]
    elif time_period == 'april':
        filtered_df = df[df['date'].dt.month == 4]
    else:
        filtered_df = df

    # Линейный график
    fig_line = px.line(filtered_df, x='date', y=['sunset', 'sunrise'], title='Динамика восхода и заката солнца')

    # Таблица
    table_data = filtered_df.to_dict('records')

    return fig_line, table_data



if __name__ == '__main__':
    app.run_server(debug=True)