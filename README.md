# Pain Detection Using FastVit Algorithm

## Overview
This repository contains code for a project focused on pain detection using Vision Transformers on a subset of 2000 images from the BioVid dataset. The primary transformer encoder utilized in this project is **FastViT** from the Keras CV Attention Models repository ([Keras CV Attention Models](https://github.com/leondgarse/keras_cv_attention_models)).

## Authors
- **Christoforos Seas**
- **Eliada Polydorou**

This project was part of the **EPL445** course at the University of Cyprus, under the supervision of **Constantinos Pattichis**.

## Required Packages
To run the code and analyze the dataset, you need to install the following Python packages:
```bash
pip install keras_cv_attention_models
pip install tensorflow
pip install pandas
pip install matplotlib
```

## Usage
- The script `data_analysis.py` is used for analyzing the dataset and generating visualizations.
- The Jupyter Notebook `pain_detection.ipynb` contains the complete workflow for training the pain detection model, including data loading, preprocessing, model definition, training, and evaluation.

 ## Results
The project evaluates the performance of the pain detection model using various metrics, including accuracy, precision, recall, and F1-score. The results are saved in the `results/` folder.

If you want to see the complete procedure of the project and how the results were obtained, please refer to the following:
- The **Presentation of the project**: [Presentation of the project.pdf](./Presentation%20of%20the%20project.pdf) provides a detailed overview of the methodology.
- The **Research Paper**: [Pain Detection Using Vision Transformers_Research paper.pdf](./Pain%20Detection%20Using%20Vision%20Transformers_Research%20paper.pdf) focuses on the research aspects and findings.


