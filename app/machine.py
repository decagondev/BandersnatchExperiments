from pandas import DataFrame
from sklearn.ensemble import RandomForestClassifier
import datetime
import joblib


class Machine:

    def __init__(self, df: DataFrame):
        """This instantiates the machine learning model. The object takes a dataframe as its parameter."""
        self.name = "Random Forest Model"
        target = df["Rarity"]
        features = df.drop(columns=["Rarity"])
        self.model = RandomForestClassifier()
        self.model.fit(features, target)
        self.timestamp = datetime.datetime.now()

    def __call__(self, feature_basis: DataFrame):
        """When called the object will return the predicted Rarity and the model's confidence."""
        prediction, *_ = self.model.predict(feature_basis)
        probability, *_ = self.model.predict_proba(feature_basis)
        return prediction, max(probability)

    def save(self, filepath):
        """This function saves the model to the given filepath. The function takes a filepath as its parameter."""
        joblib.dump(self, filepath)

    @staticmethod
    def open(filepath):
        """This function loads a saved instance of a model. The function takes a filepath as its parameter."""
        model = joblib.load(filepath)
        return model

    def info(self):
        return f"{self.name}"