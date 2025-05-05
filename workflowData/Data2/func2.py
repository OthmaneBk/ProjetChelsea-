from workflowData.Data2.collecte import collecte_data   
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

data_bio_player = collecte_data()


def func22():
    fig=plt.figure(figsize=(14, 8))
    nationality_counts = data_bio_player['nationality'].value_counts()
    sns.barplot(x=nationality_counts.index, y=nationality_counts.values)
    plt.title('Top 10 des nationalités des joueurs')
    plt.xlabel('Nationalité')
    plt.ylabel('Nombre de joueurs')
    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig