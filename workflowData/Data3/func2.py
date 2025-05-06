from workflowData.Data3.collecte import collecte_data   
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

data_Individual_Priority = collecte_data()


def func222():

    target_counts = data_Individual_Priority['Target'].value_counts()
    target_counts

    fig=plt.figure(figsize=(10, 6))
    sns.barplot(x=target_counts.index, y=target_counts.values)
    plt.title('Distribution des objectifs')
    plt.xlabel('Objectif')
    plt.ylabel('Nombre')
    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig