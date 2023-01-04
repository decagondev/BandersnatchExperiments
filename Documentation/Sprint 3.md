# Sprint 3: Machine Learning Model
- A. Notebook Model Training & Tuning
- B. Machine Learning Interface Class
- C. Model Serialization
- D. API Model Integration

## A. Notebook Model Training & Tuning
- [ ] Create a notebook for model testing and tuning
- [ ] Train and tune at least 3 models using the data generated in an earlier Sprint
- [ ] Measure the accuracy of the models and report info about your best model 
- [ ] Write a paragraph or two about your best model

---

## B. Machine Learning Interface Class
- Starter File: `app/machine`
- Suggested ML Library: Scikit-learn

- [ ] Does the __init__ function properly initialize the machine learning model and store it as an attribute?
- [ ] Does the class properly handle and store the target and feature data when initializing the model?
- [ ] Does the __call__ function take in a DataFrame of feature data and return a prediction and the probability of the prediction?

### Example Machine Learning Interface
```python
from pandas import DataFrame
from sklearn.ensemble import RandomForestClassifier


class Machine:

    def __init__(self, df: DataFrame):
        self.name = "Random Forest Classifier"
        target = df["Rarity"]
        features = df.drop(columns=["Rarity"])
        self.model = RandomForestClassifier()
        self.model.fit(features, target)

    def __call__(self, pred_basis: DataFrame):
        prediction, *_ = self.model.predict(pred_basis)
        return prediction

```

---

## C. Model Serialization
- [ ] Does the save function properly save the machine learning model to the specified filepath using joblib?
- [ ] Does the open function properly load a saved machine learning model from the specified filepath using joblib?

---

## D. API Model Integration
- [ ] Does the info function return a string with the name of the base model and the timestamp of when it was initialized?
