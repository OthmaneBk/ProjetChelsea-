from workflowData.Data3.collecte import collecte_data   
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

data_Individual_Priority = collecte_data()

def fun333():
    performance_counts = data_Individual_Priority['Performance Type'].value_counts()
    performance_counts

    fig=plt.figure(figsize=(10, 6))
    plt.pie(performance_counts, labels=performance_counts.index, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')
    plt.title('Répartition des types de performance')
    plt.tight_layout()
    return fig