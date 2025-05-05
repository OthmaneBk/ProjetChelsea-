from workflowData.collecte import collecte_data
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

data_gps = collecte_data()


print(data_gps.columns)


def func2():

    # Configuration du style
    plt.style.use('ggplot')
    sns.set_palette('deep')

    # Préparation des données
    data_gps['session_type'] = 'Match'  # Valeur par défaut

    # Étiqueter d'abord les entraînements post-match
    data_gps.loc[data_gps['md_plus_code'].notna() & (data_gps['md_plus_code'] > 0) &
                (data_gps['md_minus_code'] >= 0 | data_gps['md_minus_code'].isna()), 'session_type'] = 'Entraînement post-match'
    
       # Puis donner priorité aux entraînements pré-match (écrase les étiquettes post-match si md_minus_code < 0)
    data_gps.loc[data_gps['md_minus_code'].notna() & (data_gps['md_minus_code'] < 0), 'session_type'] = 'Entraînement pré-match'
    
    # Création du graphique
    metrics = ['distance_over_21', 'distance_over_24', 'distance_over_27']
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    for i, metric in enumerate(metrics):
        sns.histplot(data=data_gps, x=metric, bins=15, hue="session_type", kde=True, ax=axes[i])
        if i == 0:
            axes[i].set_title('Figure 2.1: Courses à haute intensité (>21 km/h)', fontsize=12)
        elif i == 1:
            axes[i].set_title('Figure 2.2: Courses à très haute intensité (>24 km/h)', fontsize=12)
        else:
            axes[i].set_title('Figure 2.3: Courses à intensité maximale (>27 km/h)', fontsize=12)

        # Ne pas écraser la légende générée automatiquement
        handles, labels = axes[i].get_legend_handles_labels()
        axes[i].legend(handles, labels, title='Type de session', loc='upper right', frameon=True)

        axes[i].set_xlabel('Distance (m)', fontsize=10)
        axes[i].set_ylabel('Fréquence', fontsize=10)

    plt.suptitle('Figure 2: Distribution des distances parcourues à différentes intensités de course par type de session', fontsize=16)
    plt.tight_layout()
    return fig