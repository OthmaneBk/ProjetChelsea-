from workflowData.Data3.collecte import collecte_data   
import matplotlib
matplotlib.use("Agg")
import pandas as pd

data_Individual_Priority = collecte_data()

def func444():
    Tracking_Target = pd.crosstab(data_Individual_Priority['Tracking'], data_Individual_Priority['Target'])
    Tracking_Target

    return Tracking_Target