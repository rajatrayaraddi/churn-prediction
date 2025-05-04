# Customer Churn Prediction

This repository contains code and analysis for predicting customer churn using a variety of machine learning techniques. The project includes preprocessing, exploratory data analysis (EDA), feature engineering, model evaluation, and ensemble learning with a stacking classifier.

## Project Structure

- **`churn_prediction.ipynb`** — Main notebook containing the complete pipeline: EDA, preprocessing, model training, evaluation, and comparison.
- **`/data/`** — Directory for storing dataset files.
- **`dataset_scrape.py`** — Script to download the dataset directly from Hugging Face.

## Dataset

- **Primary Source:** A raw dataset was sourced from [Hugging Face](https://huggingface.co/datasets/aai510-group1/telco-customer-churn).
- **Cleaned Version:** A cleaned and structured version of the dataset is available at [Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn).
- You can either use the version provided in `/data` or scrape the latest version yourself using `dataset_scrape.py`.

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/churn-prediction.git
   cd churn-prediction

2. Install the dependencies:
   `pip install -r requirements.txt`

3. (Optional) Generate your own dataset:
   `python dataset_scrape.py`

4. Run the notebook
   `jupyter notebook churn_prediction.ipynb`
   
## License
This project is for academic and educational purposes only.
