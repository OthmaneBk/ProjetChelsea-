from workflowData.Data2.collecte import collecte_data   
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

data_bio_player = collecte_data()


def func33():
    fig=plt.figure(figsize=(10, 6))
    sns.histplot(data_bio_player['age'].dropna(), bins=10)
    plt.title('Distribution des âges des joueurs')
    plt.xlabel('Âge')
    plt.ylabel('Nombre de joueurs')
    plt.tight_layout()
    plt.show()
    return fig