print("Machine Learning with Python")
# Steps of Machine Learning Programs:
# 1. Import the Data.
# 2. Clean the Data.
# 3. Split the Data into Training/Test Sets. (80% for training 20% for testing).
# 4. Create a Model.
# 5. Train the Model.
# 6. Make Predictions.
# 7. Evaluate and Improve.

# Libraries and tools:
# scikit learn, tenserflow, pytorch, keras, pandas, numpy, scipy, matplotlib, etc.
# jupyter, anaconda, etc.


# Jupyter Notebook:
# import pandas as pd
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# import joblib

# music_data_frame = pd.read_csv('music.csv')

# # input data set & output data set
# X = music_data_frame.drop(columns= ['genre'])
# y = music_data_frame['genre']
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

# model = DecisionTreeClassifier()
# model.fit(X_train, y_train)

# # Persisting Models
# joblib.dump(model, 'music-recommender.joblib')

# predictions = model.predict(X_test)
# score = accuracy_score(y_test, predictions)
# score

# Persisting Models
# import joblib

# model = joblib.load('music-recommender.joblib')

# predictions = model.predict([ [21, 1], [22, 2]])
# predictions
# # score = accuracy_score(y_test, predictions)
# # score
