from workflowData.Data3.collecte import collecte_data   
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

data_Individual_Priority = collecte_data()



def func111():
    fig, ax = plt.subplots(figsize=(12, 6))
    
    priority_counts = data_Individual_Priority.groupby(['Priority', 'Category']).size().unstack().fillna(0)
    priority_counts.plot(kind='bar', stacked=True, ax=ax)
    
    ax.set_title('Répartition des priorités par catégorie')
    ax.set_xlabel('Priorité')
    ax.set_ylabel('Nombre')
    plt.xticks(rotation=45)
    ax.legend(title='Catégorie')
    plt.tight_layout()
    
    return fig