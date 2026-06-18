# Course Recommendation System using Python

A simple recommendation system built using Python and Scikit-learn that suggests courses based on user interests. The project uses CountVectorizer and Cosine Similarity to find the most relevant courses.

## Features

* Takes user interests as input
* Converts text data into numerical vectors using CountVectorizer
* Calculates similarity using Cosine Similarity
* Recommends the top matching courses
* Displays similarity percentages
* Simple and lightweight implementation

## Technologies Used

* Python 3
* Pandas
* Scikit-learn

## Project Structure

```text
Course-Recommendation-System/
│
├── course_recommendation.py
└── README.md
```

## Installation

Install the required libraries:

```bash
pip install pandas scikit-learn
```

## Run the Program

```bash
python course_recommendation.py
```

## Available Courses

* Python
* Machine Learning
* Artificial Intelligence
* Web Development
* Cyber Security
* Data Analytics
* Cloud Computing
* UI UX Design

## How It Works

1. Stores course names and their tags.
2. Converts tags into vectors using CountVectorizer.
3. Takes user interests as input.
4. Calculates cosine similarity between user input and course tags.
5. Sorts the courses according to similarity scores.
6. Displays the top 5 recommendations.

## Sample Input

```text
Enter your interests: python ai data science
```

## Sample Output

```text
Top Recommendations:

Machine Learning : 86.6% match
Artificial Intelligence : 81.65% match
Python : 57.74% match
Data Analytics : 40.82% match
Cloud Computing : 0.0% match
```

## Algorithm Used

* CountVectorizer
* Cosine Similarity

## Future Improvements

* Add more courses and categories
* Build a graphical user interface using Tkinter
* Create a web application using Flask or Streamlit
* Use TF-IDF Vectorizer for better recommendations
* Store course data in a database
* Deploy the project online

## Author

Tulsi Khatri

## License

This project is created for educational and internship purposes.
