from sklearn import svm
import pandas as pd
import numpy as np
from sklearn.externals import joblib
import sklearn.metrics as stats
from sklearn.metrics import classification_report
from sklearn.cross_validation import train_test_split

dfA = pd.read_csv(r"C:\Users\John\jhm4.github.io\AUD_bloom.csv", parse_dates=['Date'], infer_datetime_format=True)
dfD = pd.read_csv(r"C:\Users\John\jhm4.github.io\DAX_bloom.csv", parse_dates=['Date'], infer_datetime_format=True)
dfP = pd.read_csv(r"C:\Users\John\jhm4.github.io\MMM_price2.csv", parse_dates=['Date'], infer_datetime_format=True)
dfA.to_pickle('AUD_df.pkl')
dfD.to_pickle('DAX_df.pkl')
dfP.to_pickle('MMM_dfP2.pkl')
dfA = pd.read_pickle('AUD_df.pkl')
dfD = pd.read_pickle('DAX_df.pkl')
dfP = pd.read_pickle('MMM_dfP2.pkl')

AUD = dfA['PX_CLOSE_1D']
AUDd = dfA['Date']
DAX = dfD['PX_CLOSE_1D']
DAXd = dfD['Date']
MMM = dfP[' Adj Close']
MMMd = dfP['Date']
MMM = MMM[::-1]
MMMd = MMMd[::-1]

end = round(AUD.last_valid_index()*.7)
end2 = round(DAX.last_valid_index()*.7)
end3 = round(MMM.first_valid_index()*.7)

AUD_TR = AUD[:end]
AUD_TE = AUD[end:AUD.last_valid_index()+1]
DAX_TR = DAX[:end2]
DAX_TE = DAX[end2:DAX.last_valid_index()+1]
MMM_TR = MMM[:end3]
MMM_TE = MMM[end3:MMM.first_valid_index()+1]
#print(MMM_TE.first_valid_index())
#print(MMM_TE.last_valid_index())
#print(DAX_TR[DAX_TR.last_valid_index()])



SVM_target = []
i = MMM.first_valid_index()
while i > MMM_TR.last_valid_index():
	if (MMM_TR[i-1]-MMM_TR[i]) > 0:
		SVM_target.append(1)
	else:
		SVM_target.append(0)
	i-=1
SVM_target = np.array(SVM_target)


SVM_data = []
i = 0
while i < end-1:
	X = []
	a = 0
	b = 0
	X.append(float(AUD_TR[i+1])-float(AUD_TR[i]))
	X.append(DAX_TR[i+1]-DAX_TR[i])
	SVM_data.append(X)
	i+=1

SVM_data = np.array(SVM_data)

clf = svm.SVC(C=100, gamma=1/1000)
clf.fit(SVM_data, SVM_target)
joblib.dump(clf, 'ADM_Model.pkl')

f = open('NewML2_Predictions.txt', 'w')

a = 1.0
b = 0.0
#print(str((a+b)/2.0))

i = AUD_TE.first_valid_index()
j = MMM_TE.first_valid_index()
y_true = []
y_pred = []
while i < AUD_TE.last_valid_index():
	X = []
	a = 0.0
	b = 0.0
	X.append(float(AUD_TE[i+1])-float(AUD_TE[i]))
	X.append(DAX_TE[i+1]-DAX_TE[i])
	#print("a: " + str(a) + " b: " + str(b))
	#print(str((a+b)/2.0))
	#print(str(b))
	SVM_test = np.array(X)
	length = SVM_test.size
	SVM_test = np.reshape(SVM_test, (1, length))
	prediction = clf.predict(SVM_test)

	y_pred.append(prediction)

	if (MMM_TE[j-1]-MMM_TE[j]) > 0:
		y_true.append(1)
	else:
		y_true.append(0)

	
	f.write(str(MMM_TE[j-1]-MMM_TE[j]) + " ")
	f.write(str(float(AUD_TE[i+1])-float(AUD_TE[i])) + " ")
	f.write(str(DAX_TE[i+1]-DAX_TE[i]) + " ")
	#f.write(str((a+b)/2.0)+ " ")
	f.write(str(prediction))
	f.write('\n')

	j-=1
	i+=1
Actual = 0
Earned = 0
j = MMM_TE.first_valid_index()
i = 0
while j > MMM_TE.last_valid_index():
	if y_pred[i] == 1:
		Earned = Earned + (MMM_TE[j-1]-MMM_TE[j])
	Actual = Actual + (MMM_TE[j-1]-MMM_TE[j])
	i+=1
	j-=1

print(str(Actual))
print(str(Earned))

print(stats.accuracy_score(y_true, y_pred))






