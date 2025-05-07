#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd

# Chargement des données
df = pd.read_csv("Recovery_status_Data.csv",delimiter=";")


df["sessionDate"] = pd.to_datetime(df["sessionDate"], format="%d/%m/%Y")
# Remplacement des valeurs manquantes dans "value" par 0 (selon la description des données)
df["value"] = df["value"].fillna(0)
# Filtrage des catégories liées à la récupération
recovery_categories = ["bio", "msk_joint_range", "msk_load_tolerance", "subjective", "soreness", "sleep"]
df_recovery = df[df["category"].isin(recovery_categories)]

# Séparation des métriques "_completeness" et "_composite"
df_composite = df_recovery[df_recovery["metric"].str.endswith("_composite")]
df_completeness = df_recovery[df_recovery["metric"].str.endswith("_completeness")]

def printInfo():
    # Vérification après nettoyage
    print(df.info())

    # Affichage des premières lignes après nettoyage
    print(df.head())


# In[11]:


import matplotlib.pyplot as plt
import seaborn as sns




# 1️⃣ Évolution des scores composites au fil du temps

# In[19]:


# import matplotlib.pyplot as plt
# import seaborn as sns

# plt.figure(figsize=(12, 6))
# sns.lineplot(data=df_composite, x="sessionDate", y="value", hue="category", marker="o")
# plt.title("Évolution des scores composites de récupération")
# plt.xlabel("Date")
# plt.ylabel("Score Composite (%)")
# plt.legend(title="Catégorie")
# plt.xticks(rotation=45)
# plt.show()

import matplotlib.pyplot as plt
import seaborn as sns


def funcIlyass1():
    # Créer une figure unique
    fig = plt.figure(figsize=(12, 6))

    # Tracer une courbe pour chaque catégorie
    for category in df_composite["category"].unique():
        data = df_composite[df_composite["category"] == category]
        sns.lineplot(data=data, x="sessionDate", y="value", marker="o", label=category)

    plt.title("Évolution du score composite par catégorie")
    plt.xlabel("Date")
    plt.ylabel("Score Composite (%)")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend(title="Catégorie")

    return fig


# In[ ]:

def box():
    plt.figure(figsize=(12, 6))

    # Boxplot
    sns.boxplot(data=df_composite, x="category", y="value", palette="coolwarm", width=0.6, hue="category", legend=False)

    # Scatter plot avec jitter pour éviter le chevauchement des points
    sns.stripplot(data=df_composite, x="category", y="value", color="black", jitter=True, alpha=0.5, size=2)

    plt.title("Distribution des scores composites par catégorie")
    plt.xlabel("Catégorie")
    plt.ylabel("Score Composite (%)")
    plt.xticks(rotation=45)
    plt.show()


#----------------------------------------------

def test():
    plt.figure(figsize=(12, 6))
    sns.violinplot(data=df_composite, x="category", y="value", palette="coolwarm", inner="quartile")
    plt.title("Distribution des scores composites par catégorie (Violin Plot)")
    plt.xlabel("Catégorie")
    plt.ylabel("Score Composite (%)")
    plt.xticks(rotation=45)
    plt.show()



    #----------------------------------------------

    plt.figure(figsize=(12, 6))
    sns.barplot(data=df_composite, x="category", y="value", palette="coolwarm", ci="sd")
    plt.title("Moyenne des scores composites par catégorie")
    plt.xlabel("Catégorie")
    plt.ylabel("Score Composite (%)")
    plt.xticks(rotation=45)
    plt.show()




    # In[14]:

def funcIlyass2():
        fig=plt.figure(figsize=(10, 6))
        sns.histplot(df_composite["value"], bins=20, kde=True, color="blue")
        plt.title("Distribution des scores composites de récupération")
        plt.xlabel("Score Composite (%)")
        plt.ylabel("Fréquence")
        return fig


# In[20]:


df_pivot = df_composite.pivot(index="sessionDate", columns="category", values="value")

def heat():
    plt.figure(figsize=(8, 6))
    sns.heatmap(df_pivot.corr(), annot=True, cmap="coolwarm", linewidths=0.5)
    plt.title("Corrélation entre les scores composites de récupération")
    plt.show()


# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Filtrer les catégories pertinentes
recovery_categories = ["sleep", "soreness", "subjective", "bio"]
df_recovery = df[df["category"].isin(recovery_categories)]

# Supprimer les valeurs manquantes
df_recovery = df_recovery.dropna(subset=["value"])

# Regrouper par date et catégorie
df_time_series = df_recovery.groupby(["sessionDate", "category"])["value"].mean().reset_index()

def funcIlyass3():
    # Visualisation
    fig=plt.figure(figsize=(14, 7))
    sns.lineplot(data=df_time_series, x="sessionDate", y="value", hue="category", marker="o", palette="Set1")

    plt.title("Évolution des indicateurs de récupération au fil du temps")
    plt.xlabel("Date")
    plt.ylabel("Valeur Moyenne")
    plt.xticks(rotation=45)
    plt.legend(title="Catégorie")

    return fig


# In[ ]:




