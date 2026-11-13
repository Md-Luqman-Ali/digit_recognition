# Handwritten Digit Recognition with CNN

A convolutional neural network (CNN) notebook for recognizing handwritten digits from the Kaggle Digit Recognizer dataset.

<p align="center">
  <img src="https://img.shields.io/badge/Project-Deep%20Learning-6C63FF?style=for-the-badge" alt="Deep learning project">
  <img src="https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10">
  <img src="https://img.shields.io/badge/Framework-TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white" alt="TensorFlow">
</p>

## Project overview

The notebook demonstrates an image-classification workflow for the ten digit classes (0–9), including dataset preparation, neural-network training and prediction.

**Notebook:** `digit-recognizer-cnn-98-25-accuracy.ipynb`  
**Dataset:** [Kaggle Digit Recognizer](https://www.kaggle.com/competitions/digit-recognizer)  
**Live web demo:** Not currently published.

## Dataset setup

1. Download the competition data from Kaggle.
2. Place the training and test CSV files in the locations expected by the notebook.
3. Review the first data-loading cells and update file paths for your environment.
4. Run the notebook cells in sequence.

The competition training file contains labelled digit images; the test file contains unlabelled images for prediction.

## Model workflow

1. Load and inspect pixel data.
2. Normalize and reshape image features.
3. Prepare digit labels for multiclass classification.
4. Train a convolutional neural network.
5. Evaluate on the notebook's validation/test split.
6. Generate class predictions using the model output probabilities.

## Reported result

The saved notebook output records **98.25% accuracy**. This is a historical result recorded in the notebook, not a freshly reproduced experiment and not a Kaggle leaderboard score. Re-run the notebook to validate the result in your environment.

## Environment

The notebook metadata records Python 3.10.10. The requirements file uses TensorFlow 2.11.0 as the original starting point. Use a compatible Python 3.10 environment and check the TensorFlow platform support matrix before installation. For this older TensorFlow version, a Linux environment such as WSL2 may be the most practical route on a Windows computer.

```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# macOS/Linux
# source .venv/bin/activate

python -m pip install --upgrade pip
pip install -r requirements.txt
jupyter notebook
```

## Technology

Python · TensorFlow/Keras · NumPy · Pandas · Matplotlib · Seaborn · scikit-learn · Jupyter Notebook

## Limitations

- Reproducibility depends on dataset paths, random seeds, preprocessing and training configuration.
- The recorded accuracy should be independently reproduced before being presented as a verified benchmark.
- This is an educational deep-learning project, not a production handwriting-recognition service.

## Author

**Md Luqman Ali** · [GitHub](https://github.com/Md-Luqman-Ali) · [LinkedIn](https://www.linkedin.com/in/mdluqmanali/)
