from workflowData.Data2.collecte import collecte_data   
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

data_bio_player = collecte_data()

def func11():
    fig=plt.figure(figsize=(12, 6))
    position_counts = data_bio_player['position'].value_counts()
    sns.barplot(x=position_counts.index, y=position_counts.values)
    plt.title('Répartition des joueurs par position')
    plt.xlabel('Position')
    plt.ylabel('Nombre de joueurs')
    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig