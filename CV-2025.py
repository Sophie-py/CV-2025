# Importation des modules
import streamlit as st

# Titre du projet
st.markdown("<h1 style='color: indigo;'>Anne-Sophie</h1>", unsafe_allow_html=True)

# Ajouter un sommaire ou menu de navigation à gauche
st.sidebar.markdown(
    """
    <style>
    .circle-image {
        width: 150px;
        height: 150px;
        border-radius: 50%;
        object-fit: cover;
    }
    </style>
    <img class="circle-image" src="Photo_profil.png">
    """, unsafe_allow_html=True
)

with st.sidebar:
    menu_option = st.radio("**MON CV**", ["Présentation", "Chef de projets informatiques", "Administratrice de bases de données", "Data Analyst", "Doctorat en médecine coréenne"])

if menu_option == "Présentation":
    st.subheader("Présentation")
    with st.expander("Etudes"):
        st.write("- **Ingénierie informatique** - Université Sorbonne Paris Descartes")
        st.write("- **Doctorat Médecine coréenne** - Université Paris 7")     

    with st.expander("Compétences"):
        st.write(" ")
        # Afficher le texte en fonction des compétences
        if st.checkbox("Gestion de projet"):
            st.write("- Méthode Agile, Scrum")
            st.write("- Gestion budgétaire")
            st.write("- Technique de planification, Trello, Gantt")
            st.write("- Pilotage d'équipes")
            st.write("- Contrôle qualité")
            st.write("- Conduite de réunions")
        if st.checkbox("Outils"):
            st.write("- Bureautique : Microsoft 365 (Word, Excel, Powerpoint, SharePoint, OneDrive)")
            st.write("- Communication : Google Meet, Teams, Zoom")
            st.write("- Vidéos : Loom, Vidyard")
            st.write("- Ticketing : GLPI, Redmine, JIRA")
            st.write("- Développement : Visual Studio Code, GitHub")
            st.write("- Business Intelligence : Power BI, Tableau")
        if st.checkbox("Logiciels"):
            st.write("- CRM, SIRH, CMS")
            st.write("- SIGB, GED")
        if st.checkbox("Langages informatiques"):
            st.write("- SQL")
            st.write("- Python")
        if st.checkbox("Bases de données"):
            st.write("- MySQL")
            st.write("- PostgreSQL") 

    with st.expander("Langues"):
        st.write("- Français  ⭐⭐⭐⭐⭐")
        st.write("- Anglais    ⭐⭐⭐")
        st.write("- Coréen     ⭐⭐⭐")
        st.write("- Allemand ⭐")
        st.write("- Chinois    ⭐")

    with st.expander("Centres d'intérêt"):
        st.write("- **Secourisme**")
        st.write("- Sauveteur Secouriste du Travail")
        st.write("- Habilitation électrique")
        st.write("- **Bénévolat**")
        st.write("- Médecins du Monde (Desk Urgences)")
        st.write("- Restos du Coeur")
        st.write("- **Sports**")
        st.write("- Ski, Surf")
        st.write("- Trampoline")
        st.write("- Tennis de table (vice-championne départementale 1995)")
        st.write("- **Écriture**")
        st.write("- Prix de rédaction en langue coréenne 2001 et 2002")
        st.markdown(
            '- [Mon site de voyages](https://asophieaucanada.e-monsite.com)')

    with st.expander("Coordonnées"):
        # Afficher le symbole de téléphone avec Unicode
        st.markdown("""
            <style>
            .phone-container {
                display: flex;
                align-items: center;
            }
            .phone-container span {
                font-size: 15px;  /* Taille du symbole */
                margin-right: 10px;  /* Espace entre le symbole et le texte */
            }
            </style>

            <div class="phone-container">
                <span>☎</span> <!-- Symbole de téléphone -->
                <span>+33 6 64 87 97 50</span>
            </div>
        """, unsafe_allow_html=True)

        # Afficher le symbole d'email avec Unicode
        st.markdown("""
            <style>
            .email-container {
                display: flex;
                align-items: center;
            }
            .email-container span {
                font-size: 15px;  /* Taille du symbole */
                margin-right: 10px;  /* Espace entre le symbole et le texte */
            }
            </style>

            <div class="email-container">
                <span>✉</span> <!-- Symbole d'email -->
                <span>asophiedachet@hotmail.com</span>
            </div>
        """, unsafe_allow_html=True)

        # Afficher le symbole de localisation avec Unicode
        st.markdown("""
            <style>
            .location-container {
                display: flex;
                align-items: center;
            }
            .location-container span {
                font-size: 15px;  /* Taille du symbole */
                margin-right: 5px;  /* Espace entre le symbole et le texte */
            }
            </style>

            <div class="location-container">
                <span>📍</span> <!-- Symbole de localisation -->
                <span>Nice, France</span>
            </div>
        """, unsafe_allow_html=True)

elif menu_option == "Chef de projets informatiques":
    st.subheader("Chef de projets informatiques")
    with st.expander("Mon coeur de métier"):
        st.write("Chef de projets informatiques depuis 8 ans, je suis passionnée par la stratégie d’évolution digitale et l’accompagnement des entreprises dans leur déploiement de solutions applicatives.")
        st.write("Au cours de mes différentes missions au sein de structures complexes (éditeurs de logiciels SaaS ou intégrateurs) aux secteurs d’activités variés, j’ai apporté une expertise complète englobant toutes les phases du cycle de vie des projets, depuis les premières analyses des besoins des clients, à la livraison des solutions produits jusqu'au support technique, tout en garantissant la qualité et la satisfaction des clients.")
        st.write("Mon approche allie à la fois des compétences techniques et une vision fonctionnelle et métier basée sur le modèle Agile, avec une capacité à coordonner les équipes et à prioriser les enjeux de chaque projet.")
        st.write("J’ai également acquis tout au long de ma carrière professionnelle une expérience précieuse en relation client, avec un accompagnement personnalisé aux utilisateurs dans la conduite au changement.")
                             
    with st.expander("2021-2024 Xerox France"):
        st.write(" ")
        if st.checkbox("Contexte", key="checkbox_1"):
            st.write("- Pilotage de projets clients ETI / PME / TPE et collectivités.")
            st.write("- Déploiement des solutions GED et de numérisation sur toute la France en partenariat avec les éditeurs de logiciels.")
            st.write("- Gestion du support client en TMA (Maintenance évolutive et corrective).")
        if st.checkbox("Responsabilités", key="checkbox_2"):
            st.write("- Organisation, planification et suivi des projets")
            st.write("- Reporting régulier de l’avancement des projets auprès des parties prenantes internes et externes")
            st.write("- Suivi des ressources, délais et budgets planifiés sur les projets")
            st.write("- Analyse fonctionnelle et appui à l’équipe commerciale pour définir les besoins des clients et proposer des solutions adaptées à l’aide de démonstrations interactives")
            st.write("- Animation des comités de pilotage avec les utilisateurs décisionnaires et des groupes de travail en interne")
            st.write("- Rédaction des cahiers des charges et des documents internes pour formaliser les demandes et exigences des clients")
            st.write("- Configuration technique personnalisée et recettage des applications")
            st.write("- Mise en production en veillant à ce que la solution soit fonctionnelle et prête à l’usage des clients")
            st.write("- Formation des clients avec rédaction de manuels utilisateurs et création de tutos-vidéos")
            st.write("- Échanges réguliers avec les clients")
            st.write("- Gestion du support de TMA et accompagnement des clients en collaboration avec l’équipe technique pour garantir une utilisation optimale de la solution")
            st.write("- Rédaction de procédures/modes opératoires en vue de contribuer à l’amélioration continue de la qualité des produits et services.")
        if st.checkbox("Environnement technique", key="checkbox_3"):
            st.write("- Outils de gestion projet : Trello, Gantt")
            st.write("- Outils de ticketing : JIRA")
            st.write("- Outils vidéos : Loom, Vidyard")
            st.write("- Logiciels : GED, CRM, SIRH")
            st.write("- Langages/Bases de données : SQL, PostgreSQL")
    
    with st.expander("2020 Esokia Webagency"):
        st.write(" ")
        if st.checkbox("Contexte", key="checkbox_4"):
            st.write("- Poste de Chef de projet et Product Owner")
            st.write("- Définition du produit pour la création d’une nouvelle plateforme internationale")
            st.write("- Gestion des projets de sites e-commerce")
        if st.checkbox("Responsabilités", key="checkbox_5"):
            st.write("- Analyse fonctionnelle pour la conception du produit")
            st.write("- Définition des objectifs, coûts et délais de réalisation des livrables (applications, modules, développement spécifiques, fonctionnalités)")
            st.write("- Définition des besoins en ressources humaines et en compétences techniques")
            st.write("- Définition du planning de production")
            st.write("- Organisation des user stories et des sprint planning")
            st.write("- Animation des comités de pilotage avec le client")
            st.write("- Rédaction de supports de documentation")
            st.write("- Supervision et coordination des équipes techniques intervenant aux projets (développeurs back/front, UX/UI designers, testeurs QA)")
            st.write("- Pilotage des campagnes de tests et participation aux tests")
            st.write("- Contrôle qualité et validation des livrables")
            st.write("- Livraison du produit")
            st.write("- Formation des clients pour garantir une adoption réussie du produit")
            st.write("- Suivi client et gestion de support TMA avec transmission des demandes correctives ou évolutives à l’équipe de développement")
        if st.checkbox("Environnement technique", key="checkbox_6"):
            st.write("- Outils de gestion projet : Trello, Confluence, GANTT")
            st.write("- Outils de ticketing : Redmine, JIRA")
            st.write("- Logiciels : CMS (Symfony, Drupal, Laravel)")

    with st.expander("2018-2019 Sharp Center"):
        st.write(" ")
        if st.checkbox("Contexte", key="checkbox_7"):
            st.write("- Conduite de projets de solutions de numérisation et de GED")
            st.write("- Installation des logiciels sur mesure et accompagnement aux entreprises locales, TPE et PME")
            st.write("- Service après-vente")
        if st.checkbox("Responsabilités", key="checkbox_8"):
            st.write("- Expertise conseil en gestion électronique documentaire")
            st.write("- Étude des besoins d’avant-vente et réalisation d’audits")
            st.write("- Rédaction des spécifications techniques et fonctionnelles")
            st.write("- Paramétrages des solutions sur mesure en compatibilité aux logiciels métiers connectés")
            st.write("- Accompagnement des clients dans les phases de recette et de validation des tests")
            st.write("- Déploiement des paramétrages sur les serveurs clients")
            st.write("- Formation aux utilisateurs")
            st.write("- Support technique en coordination avec les éditeurs de logiciels")
            st.write("- Maintenance des systèmes déployés")
            st.write("- Garantie de la qualité et de la performance des solutions")
        if st.checkbox("Environnement technique", key="checkbox_9"):
            st.write("- Outils de gestion projet : Trello, Gantt")
            st.write("- Outils de ticketing : GLPI")
            st.write("- Outils de numérisation : Papercut (contrôle d’impression), Autostore (capture de données)")
            st.write("- Logiciels : Sharepoint, GED, CRM, SIRH")
            st.write("- Langages/Bases de données : SQL, PostgreSQL")

    with st.expander("2017 Atexo Editions"):
        st.write(" ")
        if st.checkbox("Contexte", key="checkbox_10"):
            st.write("- Expertise fonctionnelle et technique aux Pôles Delivery et Service Clients en coordination avec les équipes R&D et les Product Owners")
            st.write("- Lien direct avec les clients Grands comptes publics (Ministères, Régions et Départements, grandes villes et agglomérations, grands établissements publics).")
        if st.checkbox("Responsabilités", key="checkbox_11"):
            st.write("- Configuration technique avancée des progiciels")
            st.write("- Réalisation et déploiement de scripts ")
            st.write("- Reprise des données en langage SQL sur les serveurs clients")
            st.write("- Mise à jour des spécifications techniques et fonctionnelles")
            st.write("- Participation aux ateliers de paramétrage avec l’équipe de développement")
            st.write("- Suivi des campagnes de tests et assistance à la recette interne")
            st.write("- Vérification de la qualité des livrables")
            st.write("- Support technique et remontée des demandes clients")
            st.write("- Maintenance corrective des applications en production")
            st.write("- Proposition d’améliorations et de capitalisation des produits")
            st.write("- Garantie de la satisfaction client")
        if st.checkbox("Environnement technique", key="checkbox_12"):
            st.write("- Outils de ticketing : Redmine, JIRA")
            st.write("- Logiciels : CRM")
            st.write("- Langages/Bases de données : SQL, MySQL, PostgreSQL")

elif menu_option == "Administratrice de bases de données":
    st.subheader("Administratrice de bases de données")
    with st.expander("2014-2017 BULAC"):
        st.write("Ingénieur d’étude (BAP E)")
        if st.checkbox("Contexte", key="checkbox_13"):
            st.write("- Administration fonctionnelle du Système d’Information de Gestion de Bibliothèque en binôme avec l’administrateur technique au sein de la DSI")
            st.write("- Gestion de la base de données numérique couvrant plus de 350 langues encodées")
            st.write("- Coordination entre les équipes métiers internes, la Direction Technique du Bâtiment, le PC Sécurité, les partenaires externes et le public")
        if st.checkbox("Responsabilités", key="checkbox_14"):
            st.write("- Gestion du projet de développement de l’infrastructure du SIGB")
            st.write("- Analyse des besoins des utilisateurs pour améliorer les fonctionnalités du SIGB")
            st.write("- Coordination des groupes de travail sur l’évolution du logiciel : signalement des ressources numériques et enrichissement des interfaces")
            st.write("- Participation aux comités de direction et de pilotage projet")
            st.write("- Lancement des campagnes de recettes des développements pour valider les montées de version")
            st.write("- Refonte de la documentation et des procédures internes")
            st.write("- Gestion du paramétrage du SIGB")
            st.write("- Contrôle des données, exploitation des requêtes SQL pour extractions statistiques et mises à jour des données des tables du SIGB")
            st.write("- Supervision des échanges de données entre le SIGB et les webservices")
            st.write("- Pilotage du SIGB en interaction avec les 15 bibliothèques partenaires")
            st.write("- Collaboration à la communauté professionnelle du SIGB au niveau national")
        if st.checkbox("Environnement technique", key="checkbox_15"):
            st.write("- Outils de ticketing : GLPI")
            st.write("- Logiciels : SIGB Koha")
            st.write("- Langages/Bases de données : SQL, PostgreSQL")
            st.write("- Systèmes d'exploitation : Windows, Ubuntu")

elif menu_option == "Data Analyst":
    st.subheader("Data Analyst")
    with st.expander("Formation"):
        st.write("**Data Analyst** - DataScientest / Ecole des Mines")
    with st.expander("Objectif professionnel"):
        st.write("Passionnée par la data et les évolutions technologiques, j'ai souhaité enrichir mes connaissances informatiques en complément de mon métier de Chef de projets.")
        st.write("Forte de mon expérience de DBA et en tant que nouvelle Data Analyste, j'aspire à accompagner tout type d'entreprise dans ses prises de décisions grâce à une gestion et une analyse des données stratégique.")
    with st.expander("Missions"):
        st.write("- Collecte des données et pré-processing")
        st.write("- Analyse des données (descriptives, exploratoires, statistiques)")
        st.write("- Visualisation des données avec des outils interactifs")
        st.write("- Modélisation prédictive basée sur les données historiques pour anticiper des tendances de l'entreprise")
        st.write("- Communication des résultats et support décisionnel")
        st.write("- Mise en place des KPI et reporting pour une vision en temps réel des indicateurs clés")
        st.write("- Automatisation de flux de travail pour gagner en productivité et en rentabilité")
        st.write("- Veille technologique et aide aux utilisateurs des données")

    with st.expander("Compétences techniques"):
        st.write("- Langages : Python (Pandas, NumPy), SQL")
        st.write("- Outils BI : Power BI, Tableau")
        st.write("- Data Visualisation : Matplotlib, Seaborn, Plotly, Streamlit")
        st.write("- Machine Learning : Scikit-learn")

else:  # "Doctorat en médecine coréenne"
    st.subheader("Doctorat en médecine coréenne")
    with st.expander("Formation et stage"):
        st.write("- Doctorat Médecine coréenne - Université Paris 7")
        st.write("- Stage à l'Institut de Médecine Coréenne Traditionnelle (Séoul, Corée du Sud)")
    with st.expander("Interventions à congrès"):
        st.write("- 2008 : 3rd International Congress on Complementary Medicine Research, Sydney (Australia)")
        st.write("_Interfaces of Korean Traditional Medicine in Contemporary Practice_")
        st.write("- 2006 : The World Congress of the Academy of Korean Studies, University of Cheju (South Korea)")
        st.write("_The Wave of Korean Manupuncture_")
        st.write("- 2006 : 6th International Congress of Traditional Asian Medicine, University of Texas (U.S.)")
        st.write("_Sense and Substance in Korean Traditional Medicine_")
        st.write("- 2005 : 22nd Conference of the Association for Korean Studies in Europe, University of Sheffield (U.K.)")
        st.write("_Manupuncture : A new practice in South Korea_")
    with st.expander("Publications"):
        st.write("- _The Wave of Korean Manupuncture : Interfaces of Traditional Medicine in Contemporary Practice_")
        st.write("in Proceedings of the World Congress of Korean Studies, University of Cheju (South Korea), 2006")
        st.write("세계한국학대회 – 논문집 : 문화교류의 역사와 현실, 실크로드에서 한류까지")
        st.write("Vol. I, pp. 115–121. Texte de la communication en anglais. Bibliographie en coréen")
