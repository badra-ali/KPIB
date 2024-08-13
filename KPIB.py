#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
from openpyxl import load_workbook

# Exemple de liste de projets (remplacez par votre liste réelle)
liste_projets = [
    "Projet 1",
    "Projet 2",
    "Projet 3",
    "Projet 4",
    "Projet 5"
]

# Fonction pour ajouter une entrée dans le fichier Excel
def ajouter_donnee(collaborateur, projets_selectionnes, fichier_excel):
    # Charger le fichier Excel s'il existe déjà, sinon en créer un nouveau
    try:
        df = pd.read_excel(fichier_excel, sheet_name='Projets')
    except FileNotFoundError:
        df = pd.DataFrame(columns=['Collaborateur', 'Projets'])

    # Créer une nouvelle entrée
    nouvelle_entree = pd.DataFrame({
        'Collaborateur': [collaborateur],
        'Projets': [', '.join(projets_selectionnes)]
    })

    # Ajouter la nouvelle entrée au DataFrame existant
    df = pd.concat([df, nouvelle_entree], ignore_index=True)

    # Sauvegarder dans le fichier Excel
    with pd.ExcelWriter(fichier_excel, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Projets', index=False)

# Interface Streamlit
st.title("Assignation des Collaborateurs aux Projets")

# Entrées utilisateur
collaborateur = st.text_input("Nom du Collaborateur")
fichier_excel = st.text_input("Chemin du fichier Excel centralisé", "projets_collaborateurs.xlsx")

# Liste de projets avec cases à cocher
projets_selectionnes = st.multiselect("Sélectionnez les projets qui vous concernent", liste_projets)

# Bouton pour soumettre
if st.button("Enregistrer"):
    if collaborateur and projets_selectionnes:
        ajouter_donnee(collaborateur, projets_selectionnes, fichier_excel)
        st.success("Données enregistrées avec succès!")
    else:
        st.error("Veuillez remplir tous les champs et sélectionner au moins un projet.")

# Afficher les données existantes
if st.checkbox("Afficher les projets existants"):
    try:
        df = pd.read_excel(fichier_excel, sheet_name='Projets')
        st.dataframe(df)
    except FileNotFoundError:
        st.warning("Aucun fichier trouvé. Enregistrez une première entrée pour créer le fichier.")

