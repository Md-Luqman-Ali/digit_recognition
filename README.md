# Handwritten Digit Recognition with CNN

A convolutional neural network notebook for the Kaggle Digit Recognizer dataset.

## Notebook and dataset

Open `digit-recognizer-cnn-98-25-accuracy.ipynb` (the standard Jupyter notebook file is already included).

Download the Digit Recognizer data from Kaggle and place the CSV files where the notebook's data-loading cells expect them. The notebook uses the competition's training and test CSV data; check and update the paths in the first data-loading cells for your environment.

## Environment

The notebook metadata records Python 3.10.10 and the requirements pin TensorFlow 2.11.0 as the original starting point. That TensorFlow release is generally suited to Python 3.10 on supported Linux environments; native Windows GPU support is not available for TensorFlow 2.11. For a reproducible setup, use a compatible Linux environment such as WSL2 or a matching Conda environment, and consult TensorFlow's platform support matrix before installing.

```bash
python -m venv .venv
# Windows PowerShell: .venv\\Scripts\\Activate.ps1
# Windows cmd: .venv\\Scripts\\activate.bat
# macOS/Linux: source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
jupyter notebook
```

## Reported result

The saved notebook output records 98.25% test accuracy. This is a historical notebook result, not a freshly reproduced run or a Kaggle leaderboard score. Re-run the complete notebook to reproduce and validate it in your environment. Multiclass predictions use `argmax` directly on model probabilities.

## Limitations

Performance depends on preprocessing, random seeds, training configuration, and the exact dataset split. The included notebook and historical output are provided for learning and portfolio review.

## Stack

Python · TensorFlow/Keras · NumPy · Pandas · Matplotlib · Seaborn · scikit-learn · Jupyter
