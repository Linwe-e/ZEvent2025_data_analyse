# ZEvent 2025 - Data Organization

## Structure

- **raw/** - Données brutes extraites (API ZEvent, SullyGnome CSV)
- **clean/** - Données nettoyées et prêtes pour l'analyse

## Datasets principaux

### clean/streamers/
- `streamers_data.csv` - Données streamers consolidées
- `zevent_sullygnome_enriched.csv` - Données enrichies ZEvent + SullyGnome

### clean/temporal/
- `donations_evolution.csv` - Évolution des dons
- `viewers_evolution.csv` - Évolution des viewers

### clean/events/
- `donation_goals.csv` - Objectifs de dons
- `event_schedule.csv` - Planning des événements

## Sources
- **ZEvent API** : zevent-api.gdoc.fr
- **SullyGnome** : Données Twitch 30 jours (CSV manual)

## 📊 Current Datasets

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

## 📈 Data Structure

### Streamers Data
- `id`, `name`, `twitch_login`, `location`, `profile_url`
- `total_donations`, `avg_viewers`, `peak_viewers`
- `duration_seconds`, `donations_final`, `donations_start`

### Temporal Data
- `timestamp`, `datetime` (parsed)
- `donations` (cumulative euros)
- `viewers` (concurrent count)

## 🚀 Usage

```python
import pandas as pd

# Load main datasets
streamers = pd.read_csv('data/streamers_detailed_stats.csv')
donations = pd.read_csv('data/donations_evolution.csv')
viewers = pd.read_csv('data/viewers_evolution.csv')

# Convert datetime columns
donations['datetime'] = pd.to_datetime(donations['datetime'])
viewers['datetime'] = pd.to_datetime(viewers['datetime'])
```

## 📋 Data Quality Notes

- **Missing Data**: 7 streamers excluded due to incomplete statistics
- **Validation**: All files verified and ready for analysis
- **Format**: UTF-8 encoding, standard CSV format
- **Integrity**: Cross-validated with source APIs