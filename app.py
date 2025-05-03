import sys
import os
import certifi
import pymongo
import pandas as pd
from flask import Flask, request, render_template, redirect, url_for
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.pipeline.training_pipeline import TrainingPipeline
from networksecurity.utils.main_utils.utils import load_object
from networksecurity.utils.ml_utils.model.estimator import NetworkModel
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
mongo_db_url = os.getenv("MONGO_DB_URL")
print(mongo_db_url)

# MongoDB client setup
ca = certifi.where()
client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)

from networksecurity.constant.training_pipeline import DATA_INGESTION_DATABASE_NAME, DATA_INGESTION_COLLECTION_NAME

database = client[DATA_INGESTION_DATABASE_NAME]
collection = database[DATA_INGESTION_COLLECTION_NAME]

# Flask app setup
app = Flask(__name__, template_folder="./templates")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/train", methods=["GET"])
def train_route():
    try:
        train_pipeline = TrainingPipeline()
        train_pipeline.run_pipeline()
        return render_template("train_success.html")
    except Exception as e:
        raise NetworkSecurityException(e, sys)

@app.route("/predict", methods=["POST"])
def predict_route():
    try:
        if 'file' not in request.files:
            return "No file part", 400

        file = request.files['file']
        df = pd.read_csv(file)

        preprocessor = load_object("final_model/preprocessor.pkl")
        final_model = load_object("final_model/model.pkl")
        network_model = NetworkModel(preprocessor=preprocessor, model=final_model)

        print(df.iloc[0])
        y_pred = network_model.predict(df)
        print(y_pred)

        df['predicted_column'] = y_pred
        print(df['predicted_column'])

        os.makedirs("prediction_output", exist_ok=True)
        df.to_csv("prediction_output/output.csv", index=False)

        table_html = df.to_html(classes='table table-striped')
        return render_template("table.html", table=table_html)
    except Exception as e:
        raise NetworkSecurityException(e, sys)

if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)
