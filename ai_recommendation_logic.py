import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = {
    "Course": [
        "Python",
        "Machine Learning",
        "Artificial Intelligence",
        "Web Development",
        "Cyber Security",
        "Data Analytics",
        "Cloud Computing",
        "UI UX Design"
    ],
    "Tags": [
        "programming python ai",
        "machine learning ai data science",
        "artificial intelligence machine learning python",
        "html css javascript programming",
        "security networking programming",
        "data science analytics statistics",
        "cloud aws security devops",
        "design creativity figma"
    ]
}

df = pd.DataFrame(data)

vectorizer = CountVectorizer()
vectors = vectorizer.fit_transform(df["Tags"])

user_input = input("Enter your interests: ").lower()

user_vector = vectorizer.transform([user_input])

similarity_scores = cosine_similarity(user_vector, vectors)[0]

df["Similarity"] = similarity_scores

recommendations = df.sort_values(by="Similarity", ascending=False)

print("\nTop Recommendations:\n")

for _, row in recommendations.head(5).iterrows():
    print(f"{row['Course']} : {round(row['Similarity'] * 100, 2)}% match")