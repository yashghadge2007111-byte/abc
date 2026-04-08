# Decision Tree Classification
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score

# Load dataset
X,y = load_iris(return_X_y=True)

# Split data
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# Model
model = DecisionTreeClassifier()
model.fit(X_train,y_train)

# Prediction
y_pred = model.predict(X_test)

# Result
print("Decision Tree Performance")
print("Accuracy:",accuracy_score(y_test,y_pred))
print("Precision:",precision_score(y_test,y_pred,average="macro"))
print("Recall:",recall_score(y_test,y_pred,average="macro"))
print("F1 Score:",f1_score(y_test,y_pred,average="macro"))
