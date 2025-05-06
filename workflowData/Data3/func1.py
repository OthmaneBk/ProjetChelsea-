from workflowData.Data3.collecte import collecte_data   
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

data_Individual_Priority = collecte_data()



def func111():
    priority_counts = data_Individual_Priority.groupby(['Priority', 'Category']).size().unstack().fillna(0)

    fig=plt.figure(figsize=(12, 6))
    priority_counts.plot(kind='bar', stacked=True)
    plt.title('Répartition des priorités par catégorie')
    plt.xlabel('Priorité')
    plt.ylabel('Nombre')
    plt.xticks(rotation=45)
    plt.legend(title='Catégorie')
    plt.tight_layout()
    return fig