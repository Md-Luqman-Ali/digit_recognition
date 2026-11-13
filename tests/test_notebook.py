import json
from pathlib import Path

ROOT = Path(__file__).parents[1]

def test_digit_submission_does_not_apply_argmax_twice():
    notebook = json.loads(
        (ROOT / "digit-recognizer-cnn-98-25-accuracy.ipynb").read_text(encoding="utf-8")
    )
    assert notebook["nbformat"] == 4
    code = "\n".join(
        cell.get("source", "") if isinstance(cell.get("source", ""), str)
        else "".join(cell.get("source", []))
        for cell in notebook["cells"]
    )
    assert "y_pred = [np.argmax(x) for x in y_pred]" not in code
    assert "np.argmax(y_probabilities, axis=1)" in code
