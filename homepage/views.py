from django.shortcuts import render
import pandas as pd
import plotly.express as px
from plotly.offline import plot
import plotly.io as pio
import numpy as np
import plotly.graph_objects as go
import json

CSV_PATH = './homepage/static/csv/bird.csv'
born_df = pd.read_csv(CSV_PATH)
fill_mean_func = lambda g: g.fillna(g.mean())
df_fill = born_df.groupby('type').apply(fill_mean_func)
df_fill.rename(columns={'huml':'상완골길이', 'humw':'상완골지름', 'ulnal':'척골길이', 'ulnaw':'척골지름',
                        'feml':'대퇴골길이', 'femw':'대퇴골지름', 'tibl':'경골길이', 'tibw':'경골지름',
                        'tarl':'족저근길이', 'tarw':'족저근지름', 'type':'종류'}, inplace=True)
df_fill['종류'][df_fill['종류'] == "SW"] = "수영가능"
df_fill['종류'][df_fill['종류'] == "W"] = "습지서식"
df_fill['종류'][df_fill['종류'] == "T"] = "육상조류"
df_fill['종류'][df_fill['종류'] == "R"] = "육식조류"
df_fill['종류'][df_fill['종류'] == "P"] = "나무등반"
df_fill['종류'][df_fill['종류'] == "SO"] = "노래가능"
# Create your views here.

def main(request):
    return render(request, 'main.html', {})

def preprocess(request):
    df_head = born_df.head(5)
    json_records_df = df_head.to_json(orient = 'records')

    df_describe = born_df.describe()
    df_describe.insert(0, 'describe', ['count','mean','std','min','25%','50%','75%','max'])
    json_records_describe = df_describe.to_json(orient='records')

    df_fill_describe = df_fill.describe()
    df_fill_describe.insert(0, 'describe', ['count','mean','std','min','25%','50%','75%','max'])
    json_records_fill = df_fill_describe.to_json(orient='records')

    df_json = json.loads(json_records_df)
    describe_json = json.loads(json_records_describe)
    drop_fill = json.loads(json_records_fill)

    grouped = df_fill['종류'].value_counts().rename_axis('type').to_frame('counts')

    fig = px.pie(grouped, values='counts', names=["노래가능", "수영가능", "습지서식", "육식조류", "나무등반", "육상조류"])
    plt_div_1 = plot(fig, output_type='div')

    return render(request, 'preprocess.html', {"df_json":df_json, "describe_json":describe_json, "fill_json":drop_fill, "plot_div_1":plt_div_1})

def hypotheses(request):
    df_corr = df_fill.drop(['id'], axis=1).corr()
    fig = go.Figure()
    fig.update_layout(
        title="Correlation Heatmap",
        title_x=0.5
    )
    fig.add_trace(
        go.Heatmap(
            x = df_corr.columns,
            y = df_corr.index,
            z = np.array(df_corr)
        )
    )
    plt_div_1 = plot(fig, output_type='div')
    return render(request, 'hypotheses.html', {"plot_div_1":plt_div_1})

def validation(request):
    fig = px.scatter(df_fill, x = '상완골길이', y = '상완골지름', color='종류', symbol='종류',  title="종류별 상완골길이와 지름")
    fig.update_layout(
        title_x=0.5
    )
    plt_div_1 = plot(fig, output_type='div')

    fig = px.box(df_fill, x="종류", y="척골길이", color='종류', title="종류에 따른 척골길이")
    fig.update_layout(
        title_x=0.5
    )
    plt_div_2 = plot(fig, output_type='div')

    fig = px.box(df_fill, x="종류", y="대퇴골길이", color='종류', title="종류에 따른 대퇴골길이")
    fig.update_layout(
        title_x=0.5
    )
    plt_div_3 = plot(fig, output_type='div')

    fig = px.box(df_fill, x="종류", y="경골길이", color='종류', title="종류에 따른 경골길이")
    fig.update_layout(
        title_x=0.5
    )
    plt_div_4 = plot(fig, output_type='div')


    fig = px.violin(df_fill, y="족저근길이", x= "종류", color='종류', box=True, hover_data=df_fill.columns)
    fig.update_layout(
        title_x=0.5
    )

    plt_div_5 = plot(fig, output_type='div')
    return render(request, 'validation.html', {"plot_div_1":plt_div_1, "plot_div_2":plt_div_2, "plot_div_3":plt_div_3, "plot_div_4":plt_div_4, "plot_div_5":plt_div_5})