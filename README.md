# Pain Detection Using Vision Transformers

## Overview
This repository contains code for a project focused on pain detection using Vision Transformers on a subset of 2000 images from the BioVid dataset. The primary transformer encoder utilized in this project is **FastViT** from the Keras CV Attention Models repository ([Keras CV Attention Models](https://github.com/leondgarse/keras_cv_attention_models)).

## Authors
- **Christoforos Seas**
- **Eliada Polydorou**

This project was part of the **EPL445** course at the University of Cyprus, under the supervision of **Constantinos Pattichis**.


## Usage
- The script `data_analysis.py` is used for analyzing the dataset and generating visualizations.
- The Jupyter Notebook `pain_detection.ipynb` contains the complete workflow for training the pain detection model, including data loading, preprocessing, model definition, training, and evaluation.

## Results
The project evaluates the performance of the pain detection model using various metrics, including accuracy, precision, recall, and F1-score. The results are saved in the `results/` folder.


