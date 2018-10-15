import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

#Confusion matrix to calculate statistics (accuracy, precision, ...)
def buildConfusionMatrix(y_predicted,y_test):
    TP = 0
    TN = 0
    FP = 0
    FN = 0
    for i in range(len(y_test) - 1):
        if y_predicted[i] == y_test.iloc[i] and y_test.iloc[i] == 1:
            TP += 1
        elif y_predicted[i] == y_test.iloc[i] and y_test.iloc[i] == 0:
            TN += 1
        elif y_predicted[i] != y_test.iloc[i] and y_test.iloc[i] == 1:
            FN += 1
        else:
            FP += 1
    return ([TP, TN, FP, FN])



file_path= r'final.csv'    #File path
data = pd.read_csv(file_path)   #Reading file in dataFrame
#print(data.columns)     #To check data is correctly loaded


data=data.fillna(-1)  #Fills Null values with -1 to run classifier correctly

X = data.loc[:, data.columns != 'label']    #Identify X as all columns except last one (label)
y = data['label']  #the target is the label column 

###### To use Random Forest classifier #########################
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(max_depth=None, random_state=None)


###### To use SVM classifier #########################
#Uncomment the next 2 lines and comment the previous 2 lines if you want to use
# SVM classifier
#from sklearn import svm
#clf = svm.SVC(kernel='linear')


#Splitting data to 30% test and 70% train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=40)

clf.fit(X_train, y_train)   #Running model
y_predicted = clf.predict(X_test)   #Predicting test data


[TP, TN, FP, FN] = buildConfusionMatrix(y_predicted,y_test) #building confusion matrix

#Metrics calculation
accuracy = (float(TP) + TN) / (TP + TN + FP + FN)
precision = (float(TP) / (TP + FP))
f_score = (2.0 * TP) / (2 * TP + FP + FN)
recall = (float(TP)) / (TP + FN)
rmse = mean_squared_error(y_test, y_predicted)

#Printing the results
print("Accuracy= ",round(accuracy*100,3),"%")
print("Precision= ", round(precision*100,3),"%")
print("F-score= ",round(f_score*100,3),"%")
print("Recall= ",round(recall*100,3),"%")
print("RMSE= ",rmse)