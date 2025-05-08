# Network Security Machine Learning Project

## Overview
This project focuses on developing a machine learning model for network security prediction using data stored in MongoDB. It involves data ingestion, preprocessing, model training, prediction, and results visualization. The web interface is built using Flask, allowing users to upload data, run predictions, and view results.

## Features
- **Data Ingestion**: The system ingests data from MongoDB using `pymongo` and stores it locally.
- **Data Transformation**: Data is cleaned, transformed, and processed to be suitable for model training.
- **Model Training**: Machine learning models are trained using `scikit-learn` for prediction tasks.
- **Prediction**: The model can predict results based on user-uploaded CSV files.
- **Web Interface**: The system uses Flask to interact with users, allowing them to upload CSV files for prediction and view results through an HTML interface.

## Technologies Used
- **Python 3.7+**
- **Flask**: Web framework for building the API.
- **MongoDB**: Database for storing network security data.
- **scikit-learn**: Machine learning library for model training.
- **MLFlow**: For model tracking and versioning.
- **pandas**: Data manipulation and analysis.
- **certifi**: For handling SSL/TLS certificates with MongoDB.

## Setup Instructions

### Prerequisites
1. **Python 3.7+**: Ensure Python is installed on your system.
2. **MongoDB**: A MongoDB instance should be available with your network security data.

### Steps to Run the Project Locally

1. **Clone the repository**:
 ```bash
   git clone https://github.com/mayank-vk/Network-Security.git
   cd Network-Security

