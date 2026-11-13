# Handwritten Digit Recognition with CNN

Convolutional neural network project for the Kaggle Digit Recognizer dataset.

The notebook metadata records Python 3.10.10. TensorFlow 2.11.0 is pinned as a starting point for a compatible Python 3.10 environment.

## Setup
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook
```

Open `digit-recognizer-cnn-98-25-accuracy.ipynb.txt` after importing or renaming it to `.ipynb`. The notebook expects the Kaggle Digit Recognizer CSV files at the paths referenced in its cells.

The saved notebook output records 98.25% test accuracy. This is a historical notebook result, not a freshly reproduced run or Kaggle leaderboard score. Multiclass predictions now use `argmax` directly on model probabilities.
