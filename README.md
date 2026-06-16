# SpaceX Falcon 9 First Stage Landing Prediction
### IBM Applied Data Science Capstone | Harshpreet Singh

---

## Objective
Predict whether SpaceX Falcon 9 first stage will successfully land — enabling cost estimation (reused booster saves ~$62M vs $165M new rocket).

## Repository Structure
- notebooks/01_spacex_api_data_collection.ipynb
- notebooks/02_webscraping_data_collection.ipynb
- notebooks/03_data_wrangling.ipynb
- notebooks/04_eda_visualization.ipynb
- notebooks/05_eda_sql.ipynb
- notebooks/06_interactive_folium.ipynb
- notebooks/07_plotly_dash.py
- notebooks/08_ml_predictive_analysis.ipynb
- data/spacex_launch_dash.csv
- data/spacex_web_scraped.csv

## Key Results
- Best Model: Decision Tree — 87.5% test accuracy (GridSearchCV, max_depth=6)
- Top Predictors: Flight Number and Payload Mass
- Success Rate by Orbit: ISS/VLEO = 100%, GTO = 43%, MEO/HEO = 0%
- Best Site: KSC LC-39A — 100% success rate

## Model Comparison
| Model | Test Accuracy |
|---|---|
| Logistic Regression | 83.3% |
| Support Vector Machine | 83.3% |
| Decision Tree (Best) | 87.5% |
| K-Nearest Neighbors | 83.3% |
