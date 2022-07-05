from sklearn import datasets
iris=datasets.load_iris()
iris_data=iris.data
iris_labels=iris.target

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(iris_data,iris_labels,test_size=0.30)

from sklearn.neighbors import KNeighborsClassifier
classifier=KNeighborsClassifier(n_neighbors=5) 
classifier.fit(x_train,y_train)
y_pred=classifier.predict(x_test)

#print(iris.target_names)

target_names = iris.target_names
for pred,actual in zip(y_pred,y_test):
     print("Prediction is "+str(target_names[pred])+", Actual is "+str(target_names[actual]))
print("*"*50,"\nClassification Score:", classifier.score(x_test,y_test),"\n","*"*50)

# from sklearn.metrics import classification_report,confusion_matrix
import  sklearn.metrics  as sm
# import classification_report,confusion_matrix
print('Confusion matrix is as follows')
print(sm.confusion_matrix(y_test,y_pred))
print('Accuracy Metrics')
print(sm.classification_report(y_test,y_pred))
