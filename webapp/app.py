from flask import Flask, render_template

app = Flask(__name__)

PROJECT_TITLE = "Vibe Code App 1"
PROJECT_TAGLINE = "Notes & solutions to Advances in Financial Machine Learning"

CHAPTER_PROGRESS = [
    ("Chapter 2 - Financial Data Structures", "[3/5]"),
    ("Chapter 3 - Meta-Labeling", "[5/5]"),
    ("Chapter 4 - Sample Weights", "[7/7]"),
    ("Chapter 5 - Fractionally Differentiated Features", "[5/6]"),
    ("Chapter 6 - Ensemble Methods", "[5/5]"),
    ("Chapter 7 - Cross-Validation in Finance", "[5/5]"),
    ("Chapter 8 - Feature Importance", "[5/5]"),
    ("Chapter 9 - Hyper-Parameter Tuning with Cross-Validation", "[6/6]"),
    ("Chapter 10 - Bet Sizing", "[4/7]"),
    ("Chapter 11 - The Dangers of Backtesting", "[5/5]"),
    ("Chapter 12 - Backtesting through Cross-Validation", "[5/5]"),
    ("Chapter 13 - Backtesting on Synthetic Data", "[2/6]"),
    ("Chapter 14 - Backtest Statistics", "[7/7]"),
    ("Chapter 15 - Understanding Strategy Risk", "[4/6]"),
    ("Chapter 16 - Machine Learning Asset Allocation", "[3/5]"),
    ("Chapter 17 - Structural Breaks", "[0/5]"),
    ("Chapter 18 - Entropy Features", "[0/5]"),
    ("Chapter 19 - Microstructural Effects", "[0/12]"),
    ("Chapter 20 - Multiprocessing and Vectorization", "[0/6]"),
]

ACKNOWLEDGEMENTS = [
    "Huge thanks to Marcos Lopez de Prado for the book and guidance.",
    "Gratitude to hudson-and-thames for their solutions and mlfinlab package.",
    "Shoutout to Vibe Code Dad for inspiring the personal touch of this project.",
]


@app.route("/")
def index():
    return render_template(
        "index.html",
        title=PROJECT_TITLE,
        tagline=PROJECT_TAGLINE,
        chapters=CHAPTER_PROGRESS,
        acknowledgements=ACKNOWLEDGEMENTS,
    )


if __name__ == "__main__":
    app.run(debug=True)
