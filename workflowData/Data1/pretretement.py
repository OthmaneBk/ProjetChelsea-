from workflowData.Data1.collecte import collecte_data


data_gps = collecte_data()

def pretretement():
    data_gps.drop(columns=['opposition_code','opposition_full'],axis=1,inplace=True)
    #mathes joue
    data_gps[data_gps["md_minus_code"] == 0]

    # séprere les données en deux types categorique et numérique
    categorical_vars = data_gps.select_dtypes(include=['object']).columns.tolist()
    numerical_vars = data_gps.select_dtypes(include=['int64', 'float64']).columns.tolist()

    data_gps.isnull().sum()

    # Identifier les lignes dupliquées
    duplicate_rows = data_gps[data_gps.duplicated()]