# Iris Flower Classification using Decision Tree

A Machine Learning project that classifies Iris flowers into different species using the Decision Tree Classification algorithm from Scikit-learn.

## Features

* Loads the Iris dataset from Scikit-learn
* Splits the dataset into training and testing sets
* Trains a Decision Tree Classifier
* Evaluates model performance using accuracy score
* Generates a classification report
* Displays the confusion matrix
* Predicts the species of a new sample flower

## Technologies Used

* Python 3
* Pandas
* Scikit-learn

## Project Structure

```
Iris-Flower-Classification/
│
├── iris_classification.py
└── README.md
```

## Installation

Install the required libraries:

```bash
pip install pandas scikit-learn
```

## Run the Program

```bash
python iris_classification.py
```

## Dataset

The project uses the built-in Iris dataset available in Scikit-learn. It contains 150 samples of iris flowers with four features:

* Sepal Length
* Sepal Width
* Petal Length
* Petal Width

Target Classes:

* Setosa
* Versicolor
* Virginica

## Model Used

Decision Tree Classifier

## Performance Metrics

* Accuracy Score
* Classification Report
* Confusion Matrix

## Sample Prediction

Input:

```python
sample = [[5.1, 3.5, 1.4, 0.2]]
```

Output:

```
Predicted Class: setosa
```

## Future Improvements

* Use Random Forest Classifier
* Visualize the Decision Tree
* Create a GUI using Tkinter
* Deploy using Flask or Streamlit
* Add support for custom datasets

## Author

Tulsi Khatri

## License

This project is created for educational and internship purposes.
