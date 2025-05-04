from workflowData.collecte import collecte_data
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

data_gps = collecte_data()

def func3():
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
    accel_metrics = ['accel_decel_over_2_5', 'accel_decel_over_3_5', 'accel_decel_over_4_5']
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    for i, metric in enumerate(accel_metrics):
        sns.histplot(data=data_gps, x=metric, bins=15, hue="session_type", kde=True, ax=axes[i])
        if i == 0:
            axes[i].set_title('Figure 4.1: Accélérations/décélérations modérées (>2.5 m/s²)', fontsize=12)
        elif i == 1:
            axes[i].set_title('Figure 4.2: Accélérations/décélérations élevées (>3.5 m/s²)', fontsize=12)
        else:
            axes[i].set_title('Figure 4.3: Accélérations/décélérations intenses (>4.5 m/s²)', fontsize=12)

        # Conserver la légende générée automatiquement avec les types de session
        handles, labels = axes[i].get_legend_handles_labels()
        axes[i].legend(handles, labels, title='Type de session', loc='upper right', frameon=True)

        axes[i].set_xlabel('Nombre d\'accélérations/décélérations', fontsize=10)
        axes[i].set_ylabel('Fréquence', fontsize=10)

    plt.suptitle('Figure 4: Distribution des accélérations et décélérations à différentes intensités', fontsize=16)
    plt.tight_layout()
    return fig