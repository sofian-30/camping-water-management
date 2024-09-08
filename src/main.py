import pandas as pd
import matplotlib.pyplot as plt

# Charger les données
sensors = pd.read_csv('data/sensors.csv')
records = pd.read_csv('data/records.csv')


sensors.head()

records.head()

# Vérifier les données manquantes pour chaque fichier
print("Données manquantes dans sensors.csv:")
print(sensors.isnull().sum())

print("\nDonnées manquantes dans records.csv:")
print(records.isnull().sum())

# Vérifier les doublons dans chaque fichier
print("\nDoublons dans sensors.csv:")
print(sensors.duplicated().sum())

print("\nDoublons dans records.csv:")
print(records.duplicated().sum())

# Afficher les doublons
doublons_sensors = sensors[sensors.duplicated()]
doublons_records = records[records.duplicated()]

print("\nDoublons dans sensors.csv:")
print(doublons_sensors)

print("\nDoublons dans records.csv:")
print(doublons_records)

# Statistiques descriptives pour identifier les valeurs aberrantes dans records.csv
print("\nStatistiques descriptives pour 'value' dans records.csv:")
print(records['value'].describe())

# Calculer le total d'eau consommée pour chaque capteur
totals = records.groupby('transmitter_addr')['value'].sum().reset_index()
totals.columns = ['sensor_addr', 'total']
totals.to_csv('/app/output/totals.csv', index=False) 

# Calculer les fuites d'eau
# Fusionner sensors avec records pour obtenir les valeurs par capteur parent
merged = pd.merge(sensors, records, left_on='sensor_addr', right_on='transmitter_addr', how='left')

# Calculer le total d'eau consommée pour chaque capteur parent
parent_totals = merged.groupby('parent_addr')['value'].sum().reset_index()
parent_totals.columns = ['sensor_addr', 'total']

# Calculer la fuite d'eau pour chaque capteur parent
leaks = pd.merge(totals, parent_totals, on='sensor_addr', how='outer', suffixes=('_child', '_parent'))
leaks['total'] = leaks['total_parent'] - leaks['total_child']
leaks = leaks[['sensor_addr', 'total']].dropna()
leaks.to_csv('/app/output/leaks.csv', index=False) 


# Visualiser les totaux d'eau consommée par chaque capteur
plt.figure(figsize=(12, 6))
plt.bar(totals['sensor_addr'], totals['total'], color='skyblue')
plt.xlabel('Adresse du Capteur')
plt.ylabel('Total d\'Eau Consommée (L)')
plt.title('Total d\'Eau Consommée par Capteur')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('/app/output/graphique_eau_capteur.png')  

# Visualiser les fuites d'eau après chaque capteur
plt.figure(figsize=(12, 6))
plt.bar(leaks['sensor_addr'], leaks['total'], color='salmon')
plt.xlabel('Adresse du Capteur')
plt.ylabel('Total d\'Eau Perdue (L)')
plt.title('Total d\'Eau Perdue par Fuite après chaque Capteur')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('/app/output/graphique_fuite_capteur.png')  

# Convertir le timestamp en date pour regrouper les données par jour
records['date'] = pd.to_datetime(records['timestamp'], unit='s').dt.date

# Calculer la consommation totale d'eau par jour pour chaque capteur
daily_totals = records.groupby(['transmitter_addr', 'date'])['value'].sum().reset_index()
daily_totals.columns = ['sensor_addr', 'date', 'total']

# Fusionner sensors avec les totaux journaliers pour obtenir les valeurs par capteur parent
merged_daily = pd.merge(sensors, daily_totals, left_on='sensor_addr', right_on='sensor_addr', how='left')

# Calculer la consommation totale d'eau par jour pour chaque capteur parent
parent_daily_totals = merged_daily.groupby(['parent_addr', 'date'])['total'].sum().reset_index()
parent_daily_totals.columns = ['sensor_addr', 'date', 'total']

# Calculer les fuites d'eau journalières pour chaque capteur parent
daily_leaks = pd.merge(daily_totals, parent_daily_totals, on=['sensor_addr', 'date'], how='outer', suffixes=('_child', '_parent'))
daily_leaks['leak'] = daily_leaks['total_parent'] - daily_leaks['total_child']

# Filtrer les résultats pour n'inclure que les fuites positives (pertes d'eau)
daily_leaks = daily_leaks[['sensor_addr', 'date', 'leak']].dropna()
daily_leaks = daily_leaks[daily_leaks['leak'] > 0]

# Sauvegarder les résultats dans un fichier CSV
daily_leaks.to_csv('/app/output/daily_leaks.csv', index=False)  

# Visualiser les fuites d'eau par jour pour chaque capteur
plt.figure(figsize=(12, 6))

# Itérer sur chaque capteur pour créer un graphique individuel
for sensor in daily_leaks['sensor_addr'].unique():
    sensor_data = daily_leaks[daily_leaks['sensor_addr'] == sensor]
    plt.plot(sensor_data['date'], sensor_data['leak'], label=sensor)

plt.xlabel('Date')
plt.ylabel('Total d\'Eau Perdue (L)')
plt.title('Fuites d\'Eau Journalières par Capteur')
plt.xticks(rotation=45)
plt.legend(title='Adresse du Capteur')
plt.tight_layout()
plt.savefig('/app/output/graphique_capteur_graphique.png') 

# Calculer les fuites d'eau totales par jour pour tout le réseau
total_daily_leaks = daily_leaks.groupby('date')['leak'].sum().reset_index()

# Visualiser les fuites d'eau totales par jour
plt.figure(figsize=(12, 6))
plt.plot(total_daily_leaks['date'], total_daily_leaks['leak'], color='red')
plt.xlabel('Date')
plt.ylabel('Total d\'Eau Perdue (L)')
plt.title('Fuites d\'Eau Totales Journalières dans le Réseau')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('/app/output/graphique_fuite_eau_jour.png') 