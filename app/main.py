import os

from Fortuna import random_int, random_float
from flask import Flask, render_template, request
from pandas import DataFrame

from app.data import Database
from app.graph import chart
from app.machine import Machine

APP = Flask(__name__)
APP.db = Database()
options = ["Level", "Health", "Energy", "Sanity", "Rarity"]
filepath = os.path.join("app", "model.joblib")
if not os.path.exists(filepath):
    data = APP.db.dataframe()
    APP.model = Machine(data[options])
    APP.model.save(filepath)
else:
    APP.model = Machine.open(filepath)


@APP.route("/")
def home():
    return render_template("home.html")


@APP.route("/data")
def data():
    return render_template(
        "data.html",
        count=APP.db.count(),
        table=APP.db.table(),
    )


@APP.route("/view", methods=["GET", "POST"])
def view():
    x_axis = request.values.get("x_axis") or "Health"
    y_axis = request.values.get("y_axis") or "Energy"
    target = request.values.get("target") or "Rarity"
    graph = chart(
        df=APP.db.dataframe(),
        x=x_axis,
        y=y_axis,
        target=target,
    ).to_json()
    return render_template(
        "view.html",
        options=options,
        x_axis=x_axis,
        y_axis=y_axis,
        target=target,
        count=APP.db.count(),
        graph=graph,
    )


@APP.route("/model", methods=["GET", "POST"])
def model():
    level = request.values.get("level", type=int) or random_int(1, 20)
    health = request.values.get("health", type=float) or round(random_float(1, 250), 2)
    energy = request.values.get("energy", type=float) or round(random_float(1, 250), 2)
    sanity = request.values.get("sanity", type=float) or round(random_float(1, 250), 2)
    prediction, confidence = APP.model(DataFrame([{
        "Level": level,
        "Health": health,
        "Energy": energy,
        "Sanity": sanity,
    }]))
    info = APP.model.info()
    return render_template(
        "model.html",
        info=info,
        level=level,
        health=health,
        energy=energy,
        sanity=sanity,
        prediction=prediction,
        confidence=f"{confidence:.2%}",
    )
