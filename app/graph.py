import pandas as pd
import numpy as np
from altair import Chart, Color, Scale

from pandas.core.frame import DataFrame


def chart(df: DataFrame, x: str, y: str, target: str) -> Chart:
    number_type_data = pd.DataFrame({
        x: df[x],
        y: df[y],
        target: np.random.choice(["Level", "Health", "Energy", "Sanity", "Rarity"], len(df))

    })
    chart_title = f"{x} by {y} for {target}"
    chart = Chart(number_type_data).mark_point(opacity=0.12).encode(

        x=x,
        y=y,
        color=Color(x, scale=Scale(scheme='rainbow'))
    )
    chart_title_text = f'{chart_title}'
    chart_with_title = chart.properties(title=chart_title_text)
    chart_with_title.properties(title=chart_title)

    return chart_with_title
