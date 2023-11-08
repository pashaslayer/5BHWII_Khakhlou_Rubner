import pandas as pd


# Auftragsspezifische Daten
MEK = 26  # Materialeinzelkosten in €/Stück
tMW = 35  # Fertigungszeit mechanische Werkstätte in Minuten/Stück
tCNC = 18  # Fertigungszeit am CNC-Bearbeitungszentrum in Minuten/Stück
tMO = 15  # Fertigungszeit Montage in Minuten/Stück
Transportkosten = 300  # Sonderkosten des Vertriebs in €

# Unternehmensspezifische Daten
FStMW = 26  # Fertigungsstundensatz mechanische Werkstätte in €/h
FStMO = 22  # Fertigungsstundensatz Montage in €/h
MStCNC = 95  # Maschinenstundensatz CNC-Bearbeitungszentrum in €/h
MGKZ = 5 / 100  # Materialgemeinkostenzuschlagssatz
FGKZMW = 45 / 100  # Fertigungsgemeinkostenzuschlagssatz mechanische Werkstätte
FGKZMO = 60 / 100  # Fertigungsgemeinkostenzuschlagssatz Montage
VerwGKZ = 8 / 100  # Verwaltungsgemeinkostenzuschlagssatz
VertrGKZ = 12 / 100  # Vertriebsgemeinkostenzuschlagssatz
Gewinn = 10 / 100  # Gewinn
Skonto = 2 / 100  # Skonto
Rabatt = 5 / 100  # Rabatt

# Berechnung der Herstellkosten
Materialkosten = MEK
Herstellkosten_MW = FStMW * (tMW / 60)  # Umrechnung von Minuten in Stunden
Herstellkosten_CNC = MStCNC * (tCNC / 60)  # Umrechnung von Minuten in Stunden
Herstellkosten_MO = FStMO * (tMO / 60)  # Umrechnung von Minuten in Stunden

# Berechnung der Gemeinkosten
Materialgemeinkosten = Materialkosten * MGKZ
Fertigungsgemeinkosten_MW = Herstellkosten_MW * FGKZMW
Fertigungsgemeinkosten_MO = Herstellkosten_MO * FGKZMO

# Berechnung der Gesamtkosten
Gesamtkosten = Herstellkosten_MW + Herstellkosten_CNC + Herstellkosten_MO + Materialgemeinkosten + Fertigungsgemeinkosten_MW + Fertigungsgemeinkosten_MO

# Berechnung der Verwaltungs- und Vertriebskosten
Verwaltungsgemeinkosten = Gesamtkosten * VerwGKZ
Vertriebsgemeinkosten = Transportkosten + (Gesamtkosten * VertrGKZ)

# Berechnung des Netto-Verkaufspreises
Netto_Verkaufspreis = Gesamtkosten + Verwaltungsgemeinkosten + Vertriebsgemeinkosten
Netto_Verkaufspreis *= (1 + Gewinn)  # Gewinnzuschlag
Netto_Verkaufspreis *= (1 - Skonto)  # Skonto
Netto_Verkaufspreis *= (1 - Rabatt)  # Rabatt

# Erstellen eines DataFrames für die Ergebnisse
data = {
    'Kostenelement': ['Materialkosten', 'Herstellkosten (MW)', 'Herstellkosten (CNC)', 'Herstellkosten (MO)',
                      'Materialgemeinkosten', 'Fertigungsgemeinkosten (MW)', 'Fertigungsgemeinkosten (MO)',
                      'Gesamtkosten', 'Verwaltungsgemeinkosten', 'Vertriebsgemeinkosten', 'Netto-Verkaufspreis'],
    'Kosten in €': [Materialkosten, Herstellkosten_MW, Herstellkosten_CNC, Herstellkosten_MO, Materialgemeinkosten,
                     Fertigungsgemeinkosten_MW, Fertigungsgemeinkosten_MO, Gesamtkosten, Verwaltungsgemeinkosten,
                     Vertriebsgemeinkosten, Netto_Verkaufspreis]
}

df = pd.DataFrame(data)

# Schreiben der Ergebnisse in eine Excel-Datei
with pd.ExcelWriter('Zuschlagskalkulation_Ergebnisse.xlsx') as writer:
    df.to_excel(writer, sheet_name='Ergebnisse', index=False)

print("Ergebnisse wurden in 'Zuschlagskalkulation_Ergebnisse.xlsx' gespeichert.")
