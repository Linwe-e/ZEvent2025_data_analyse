# ZEvent 2025 - Data Analysis

![ZEvent Logo](outputs/figures/dashboard_principal_ameliore.png)

Analyse complète des données ZEvent 2025, l'événement caritatif français qui a réuni des streamers pour lever des fonds.

## 🎯 Objectif

Analyser les données de ZEvent 2025 pour comprendre les patterns de donations, les performances des streamers et les tendances de l'événement.

## 🚀 Installation

```bash
# Cloner le repo
git clone https://github.com/Linwe-e/ZEvent2025_data_analyse.git
cd ZEvent2025_data_analyse

# Créer un environnement virtuel
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac

# Installer les dépendances
pip install -r requirements.txt
```

## 📝 Utilisation

```bash
# Lancer Jupyter Notebook
jupyter notebook
```

Puis ouvrez les notebooks dans l'ordre suivant :
1. `01_data_preparation.ipynb` - Préparation des données
2. `02_analysis.ipynb` - Analyse des données
3. `03_visualizations.ipynb` - Visualisations
4. `04_ZEvent_analysis.ipynb` - Analyse complète

## 🏗️ Structure

```
ZEvent2025_data_analyse/
├── data/
│   ├── raw/           # Données brutes (API ZEvent, SullyGnome CSV)
│   └── clean/         # Données nettoyées et prêtes pour analyse
├── notebooks/
│   ├── 01_data_preparation.ipynb    # Extraction et nettoyage
│   ├── 02_analysis.ipynb            # Analyses statistiques
│   └── 03_visualizations.ipynb      # Graphiques et rapports
├── outputs/           # Résultats et visualisations
└── requirements.txt
```

## 📊 Données

### Core Datasets (CSV)
| File | Description | Records | Source |
|------|-------------|---------|--------|
| `streamers_data.csv` | Basic streamer profiles | 326 | ZEvent API |
| `streamers_detailed_stats.csv` | Enhanced metrics | 319 | Cache API |
| `donations_evolution.csv` | Temporal donations | Time series | Cache API |
| `viewers_evolution.csv` | Temporal viewership | Time series | Cache API |
| `donation_goals.csv` | Individual objectives | Variable | ZEvent API |
| `event_schedule.csv` | Event programming | Variable | ZEvent API |

### Metadata Files (JSON)
| File | Description | Format |
|------|-------------|--------|
| `all_statistics.json` | Global event statistics | JSON |
| `individual_streamer_stats.json` | Raw individual stats | JSON |
| `donation_goals.json` | Raw donation goals | JSON |
| `event_schedule.json` | Raw event schedule | JSON |

## 🔢 Key Metrics

- **Total Donations**: €16,182,382.43
- **Event Duration**: 152.6 hours
- **Streamers**: 326 total, 319 with complete data
- **Period**: September 5-7, 2025
- **Data Quality**: 97.9% completion rate

## � Workflow d'analyse

1. **Préparation des données**
   - Lancer `01_data_preparation.ipynb` pour préparer les données
   
2. **Analyse statistique**
   - Lancer `02_analysis.ipynb` pour l'analyse statistique
   
3. **Visualisations**
   - Lancer `03_visualizations.ipynb` pour les graphiques
   
4. **Analyse complète**
   - Lancer `04_ZEvent_analysis.ipynb` pour l'analyse finale

## 📈 Résultats

Les notebooks génèrent :
- Statistiques descriptives complètes
- Analyses de corrélations
- Visualisations interactives
- Rapports exports-ready

## 🌐 Sources

- **API ZEvent** : zevent-api.gdoc.fr
- **SullyGnome** : Métriques Twitch complémentaires

### Key Notebooks
- `notebooks/01_data_preparation.ipynb` - Extraction et nettoyage des données
- `notebooks/02_analysis.ipynb` - Analyses statistiques détaillées
- `notebooks/03_visualizations.ipynb` - Visualisations et graphiques
- `notebooks/04_ZEvent_analysis.ipynb` - Analyse complète et rapport final

## 📈 Analyses disponibles

### 🎪 Performance des streamers
- Efficacité des donations et engagement de l'audience
- Top performeurs et tendances de croissance
- Performance individuelle vs collaborative

### ⏰ Patterns temporels
- Heures de pics de donations et de visionnage
- Impact de l'événement sur l'engagement
- Patterns circadiens et effets de weekend

### 🎯 Atteinte des objectifs
- Analyse des objectifs de donation
- Facteurs de succès et stratégies
- Efficacité de la gamification

### 🎮 Coordination d'événement
- Impact des activités programmées
- Collaboration entre streamers
- Optimisation de la programmation

## 🛠️ Stack technique

- **Traitement de données**: pandas, numpy
- **Visualisation**: matplotlib, seaborn, plotly
- **Analyse**: scipy, scikit-learn
- **Web Scraping**: requests, BeautifulSoup
- **Notebooks**: Jupyter, ipywidgets

## 📊 Sources de données

- **ZEvent API** (`zevent-api.gdoc.fr`) - Données non-officielles de l'événement
- **GitHub Cache** (`maniarr.github.io/cache.zevent.gdoc.fr`) - Statistiques historiques
- **SullyGnome** (`sullygnome.com`) - Analytiques Twitch (optionnel)

## 🤝 Contribuer

Ce projet suit les meilleures pratiques de data science :
- Code modulaire et réutilisable
- Documentation complète
- Validation de la qualité des données
- Pipeline d'analyse reproductible

## 📄 Licence

Ce projet est destiné à des fins éducatives et de recherche. Toutes les données sont publiquement disponibles et utilisées dans le respect des conditions d'utilisation.

## 🎯 Prochaines étapes

- [ ] Modélisation ML avancée pour la prédiction des donations
- [ ] Développement d'un tableau de bord en temps réel
- [ ] Analyse comparative des ZEvent à travers les années
- [ ] Analyse réseau des interactions entre streamers

---

*Conçu avec ❤️ pour la communauté ZEvent et l'analyse de données open-source*
