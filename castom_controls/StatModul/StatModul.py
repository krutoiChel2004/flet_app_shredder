import flet as ft
from utils.database_utils import get_TrashStatTable
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from flet.plotly_chart import PlotlyChart

class StatModul(ft.UserControl):

    def build(self):
        data = get_TrashStatTable()

        grouping_by_class = data.groupby(["id_object"]).size()


        labels = grouping_by_class.index.tolist()
        count = grouping_by_class.values.tolist()
        data_count = {
                "id":labels,
                "count":count
            }
        d = pd.DataFrame(data_count)
        fig1 = go.Figure(data=[go.Pie(labels=d["id"], values=d["count"])])
        fig2 = px.bar(d, y='count', x='id')

        return ft.Container(
                        ft.Container(ft.Row([PlotlyChart(fig1, expand=True),
                                             PlotlyChart(fig2, expand=True)]),
                                     height=600),
        )