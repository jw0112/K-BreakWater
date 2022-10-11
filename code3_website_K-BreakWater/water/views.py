from django.shortcuts import render
from django.http import HttpResponse
from plotly.offline import plot
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# html 연결

# Create your views here.
# water views를 urls에서 해줬으니 index html로 연결
def water(request):
    return render(request, 'water/index.html')

# city_detail views를 urls에서 해줬으니 str:city에서 city로 받아오는 값마다 함수를 이용해 연결
def city_detail(request, city):
    path_template = 'water/'
    if city == 'daedeokgu':
        path_template += 'daedeokgu.html'
    elif city == 'donggu':
        path_template += 'donggu.html'
    elif city == 'junggu':
        path_template += 'junggu.html'
    elif city == 'seogu':
        path_template += 'seogu.html'
    elif city == 'yuseonggu':
        path_template += 'yuseonggu.html'
    else:
        path_template += 'index.html'
    
    #plotly
    # 그래프 데이터 값
    time = ['10:00', '10:10', '10:20', '10:30', '10:40', '10:50']
    time_pre = ['1100']
    wl_y = [1.7, 1.7, 1.8, 2.0, 2.1, 2.2]
    wl_pre = [2.4]
    a = [2.8, 2.8, 2.8, 2.8, 2.8, 2.8]
    b = [3.2, 3.2, 3.2, 3.2, 3.2, 3.2]
    c = [3.6, 3.6, 3.6, 3.6, 3.6, 3.6]
    d = [4.0, 4.0, 4.0, 4.0, 4.0, 4.0]
    rf_y = [1, 2, 2, 4, 2, 2]
    graphs = []
    range_x=[1000,1130,10]
    graphs.append(
        go.Scatter(x=time, y=rf_y, mode='lines', name='강수량(mm)')
    )
    graphs.append(
        go.Scatter(x=time, y=wl_y, mode='lines', name='수위(m)')
    )
    graphs.append(
        go.Scatter(x=time_pre, y=wl_pre, mode='markers', name='예측 수위')
    )
#   graphs.append(
#       go.Scatter(x = time, y = a, mode='lines', name='관심')
#   )
#   graphs.append(
#       go.Scatter(x = time, y = b, mode='lines', name='주의')
#   )
#   graphs.append(
#       go.Scatter(x = time, y = c, mode='lines', name='경계')
#   )
#   graphs.append(
#       go.Scatter(x = time, y = d, mode='lines', name='심각')
#   )

    legend = dict(
        orientation="h",
        yanchor="bottom", y=1.05, # y축 방향 위치 설정
        xanchor="right", x=1,# x축 방향 위치 설정
        font=dict(
            size=10,
            color="black"
        )
	)
    # 그래프 시각화
    layout = {
        'xaxis_title': '시간',
        'yaxis_title': '강수량 / 수위',
        'margin': {'l': 40, 'r': 0, 't': 50, 'b': 30},
        'height': 200,
        'width': 320,
        'legend' : legend,
    }

    plot_div = plot({'data': graphs, 'layout': layout}, 
                    output_type='div')
    return render(request, path_template, context={'plot_div': plot_div})

