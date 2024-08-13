#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
from openpyxl import load_workbook

# Exemple de liste de projets (remplacez par votre liste réelle)
liste_projets = [
    "Projet Evaluation/diagnostic du niveau de maturité relativement AUX normes ISO 9001, 45001, 14001 et implémentation du Système de Management de Qualité 9001 de Cl ENERGIES",
    "Evaluation /diagnostic et opérationnalisation du SMCA ISO 22301 de l’ONEP",
    "Etude pour la mise en œuvre, le suivi et le contrôle des services de vérification de la conformité des produits embarqués à destination de la Côte d’Ivoire",
    "Diagnostic et implémentation du SMQ ISO 9001 à l’UIPA (Université Internationale Privée d’Abidjan)"
    "Etude d’impact socio-économique du projet / coût d’opportunité d’un tel projet (réhabilitation d’un siège de l’Inspection Générale d’Etat) en sous-traitance avec le cabinet pyramide",
    "Mécanismes de financement des charges récurrentes (coûts d’entretien et de fonctionnement de bâtiment et des équipements y afférents) dans le cadre du projet de réhabilitation d’un siège de l’Inspection Générale de l’Etat) en sous-traitance avec le cabinet Pyramide"
    "Etude sur la structure du prix du pain",
    "PAR complémentaire",
    "Métro d’Abidjan Ligne 1",
    "PAR Travaux d’assainissement du canal d’Anoumambo",
    "Etude Economique et Financière sur la problématique de la tarification de la livraison et du positionnement des conteneurs aux Ports Autonomes d’Abidjan et de San-Pedro (FEDERMAR)",
    "Elargissement de l’Assiette fiscale",
    "PROJET GREEN 2000",
    "Construction et exploitation de centre de service et formation agricole en Côte d’Ivoire",
    "PROJET : MABY",
    " Etude relative à l’élaboration d’un cadre de gestion et de gouvernance des marchés de Bouaké et de Yopougon",
    "Etudes organisationnelles financières Construction de 500 logements sociaux et Economiques à Songon-Kassemblé phase pilote",
    "Projet de mise en place d’un cadre de gestion intégrée de l’information Géospatiale",
    "Projet Régional d’Electrification de 20 000 villages dans l’espace CEDEAO (PRODEL 20 000)",
    "Réalisation d’Etude de faisabilité technico-Economique et Environnementale pour la gestion en mode PPP des stations d’épuration publiques d’eaux usées des zones Industrielles en Côte d’Ivoire",
    "Révision des conventions de concession des opérateurs de transport lagunaire",
    "Evaluation des préjudices d’exploitation de SITARAIL relatifs aux interruptions temporaires de circulation dans le cadre de la réalisation des travaux de construction du Métro ligne 1 d’Abidjan",
    "Etude relative à la Promotion et au Développement du Tourisme et de l’Artisanat dans le District Autonome de la Vallée du BANDAMA",
    "Actualisation de la Banque de Données des Prix de Référence (BDPR)",
    "Schéma directeur d’aménagement et de développement territorial du Denguélé",
    "Elaboration du plan stratégique de développement de la commune de Yamoussoukro",
    "Recrutement d’un cabinet pour le renforcement des capacités des agents de la direction des régimes économiques sur l’exploitation des fiches techniques de production dans le domaine du perfectionnement actif",
    "Vérification des instruments de métrologie",
    "Etude portant sur la réalisation du Cadastre du district autonome de Woroba( étude visant à évaluer le potentiel de développement économique et social du district autonome du Woroba,",
    "Evaluation et Diagnostic du niveau de maturité du Ministère de l'Economie du Plan et du Développement relativement aux exigences du système de management de la qualité (SMQ) ISO 9001:2015 puis implémentation du système",
    "Evaluation du dispositif de contrôle interne du Ministère de l'Economie du Plan et du Développement selon les référentiels COSO et ISO 31000",
    "Etude Diagnostique de l’Opérationnalisation de l’ANAQ-ESR en vue du Renforcement de la qualité des Formations et de l’Employabilité des Jeunes Diplômés de l’Enseignement Supérieur",
    "Evaluation du guichet unique du commerce extérieur de Côte d’Ivoire",
    "Projet de construction d'une écloserie de haute qualité, d'un centre de formation et d'une usine",
    "Projet STEP (Construction de stations d'épuration d'eaux usées des zones industrielles)",
    "PLAN D'ACTION ET DE REINSTALLATION (PAR) SUITE AUX TRAVAUX D'ASSAINISSEMENT DU CANAL D'ANOUMAMBO"
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

