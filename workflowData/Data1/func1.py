from workflowData.collecte import collecte_data 
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

data_gps = collecte_data()

def func1():

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
    fig=plt.figure(figsize=(12, 6))
    sns.histplot(data=data_gps, x='distance', hue='session_type', bins=20, kde=True, element='step')
    plt.title('Figure 1: Distribution de la charge (distance totale) par type de session', fontsize=14)
    plt.xlabel('Distance totale (m)', fontsize=12)
    plt.ylabel('Fréquence', fontsize=12)
    plt.legend(title='Type de session', loc='upper right', frameon=True, fontsize=10)
    plt.tight_layout()
    return fig