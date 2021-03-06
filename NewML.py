from sklearn import svm
import pandas as pd
import numpy as np
from sklearn.externals import joblib
import sklearn.metrics as stats
from sklearn.metrics import classification_report
from sklearn.cross_validation import train_test_split

df = pd.read_csv(r"C:\Users\John\jhm4.github.io\MMM_bloom.csv", parse_dates=['Date'], infer_datetime_format=True)
df.to_pickle('MMM_df.pkl')
dfP = pd.read_csv(r"C:\Users\John\jhm4.github.io\MMM_price.csv", parse_dates=['Date'], infer_datetime_format=True)
dfP.to_pickle('MMM_dfP.pkl')
df = pd.read_pickle('MMM_df.pkl')
dfP = pd.read_pickle('MMM_dfP.pkl')

dfP = dfP[::-1]

BRO = df['BETA_RAW_OVERRIDABLE']
AO = df['ALPHA_OVERRIDABLE']
ABPM = df['ALPHA_FOR_BETA_PM']
VOL = df['VOLATILITY_10D']
EBITDA = df['EBITDA']
EPS = df['IS_EPS']
EVAL = df['CURR_ENTP_VAL']
CHG = df['CHG_NET_2D']
QR = df['QUICK_RATIO']
RISK = df['RISK_PREMIUM']
MOV50 = df['MOV_AVG_50D']
MOV10 = df['MOV_AVG_10D']

end = df.last_valid_index()
train_end = int(round(end*.7))

BRO_TR = BRO[:train_end]
BRO_TE = BRO[train_end:end]
AO_TR = AO[:train_end]
AO_TE = AO[train_end:end]
ABPM_TR = ABPM[:train_end]
ABPM_TE = ABPM[train_end:end]
VOL_TR = VOL[:train_end]
VOL_TE = VOL[train_end:end]
EBITDA_TR = EBITDA[:train_end]
EBITDA_TE = EBITDA[train_end:end]
EPS_TR = EPS[:train_end]
EPS_TE = EPS[train_end:end]
EVAL_TR = EVAL[:train_end]
EVAL_TE = EVAL[train_end:end]
CHG_TR = CHG[:train_end]
CHG_TE = CHG[train_end:end]
QR_TR = QR[:train_end]
QR_TE = QR[train_end:end]
RISK_TR = RISK[:train_end]
RISK_TE = RISK[train_end:end:]
MOV50_TR = MOV50[:train_end]
MOV50_TE = MOV50[train_end:end:]
MOV10_TR = MOV10[:train_end]
MOV10_TE = MOV10[train_end:end]

#Import and Reverse the Prices to get them in the correct order
price = dfP[' Adj Close']
price_TR = price[:train_end]
price_TE = price[train_end:end]

#Function to Update the SVM with new data sample
def update(day):
	day = day
	PorL = price_TE[day-44]-price_TE[day]
	global SVM_data
	global SVM_target
	#SVM_data = SVM_data.tolist()
	#SVM_target = SVM_target.tolist()
	#SVM_data.append(SVM_test)
	np.append(SVM_data, SVM_test)
	if PorL > 0:
		PL = 1
	else:
		PL = 0
	#SVM_target.append(np.array(PL))
	np.append(SVM_target, np.array(PL))
	SVM_data = np.array(SVM_data)
	SVM_target = np.array(SVM_target)
	clf.fit(SVM_data, SVM_target)
	joblib.dump(clf, 'MMM_Model.pkl')

#Create Training Target Array
SVM_target = []
SVM_data = []
j = 1510
while j > 454:
	if j > 453+44:
		if price_TR[j-44]-price_TR[j] > 0:
			SVM_target.append(1)
		else:
			SVM_target.append(0)
	else: 
		if price_TE[j-44]-price_TR[j]:
			SVM_target.append(1)
		else:
			SVM_target.append(0)
	j -= 1

#Convert into Numpy Array
SVM_target = np.array(SVM_target)

#Create the Training Data Arrays
end = len(BRO_TR)
j = 0
while j < end-1:
	X = []
	X.append(BRO_TR[j])    #Beta Raw Overridable
	#X.append(AO_TR[j])     #Alpha Overridable
	#X.append(ABPM_TR[j])   #Alpha for Beta PM
	#X.append(VOL_TR[j])    #10 Day Volatility
	#X.append(EBITDA_TR[j]) #EBITDA
	#X.append(EPS_TR[j])    #Earnings Per Share
	#X.append(EVAL_TR[j])   #Current Enterprise Value
	X.append(CHG_TR[j])    #2-Day Net Price Change
	X.append(QR_TR[j])     #Quick Ratio
	X.append(RISK_TR[j])   #Risk Premium
	#X.append(MOV50_TR[j])  #50-Day Moving Average
	X.append(MOV10_TR[j])  #10-Day Moving Average
	SVM_data.append(X)
	j += 1

#Convert into Numpy Array
SVM_data = np.array(SVM_data)

#Fit the Model
clf = svm.SVC(C=100, gamma=1/1056)
clf.fit(SVM_data, SVM_target)
joblib.dump(clf, 'MMM_Model.pkl')


f = open('MMM_Predictions.txt', 'w')

#Make Predictions of Test Data
end = len(BRO_TE)
j = BRO_TE.first_valid_index()+44
SVM_test = []
y_pred = []
i = 453
print(str(j))
print(str(BRO_TE.last_valid_index()))
while j < BRO_TE.last_valid_index():
	clf = joblib.load('MMM_Model.pkl')
	Xp = []
	Xp.append(BRO_TE[j-44])
	#Xp.append(AO_TE[j-44])
	#Xp.append(ABPM_TE[j-44])
	#Xp.append(VOL_TE[j-44])
	#Xp.append(EBITDA_TE[j-44])
	#Xp.append(EPS_TE[j-44])
	#Xp.nappend(EVAL_TE[j-44])
	Xp.append(CHG_TE[j-44])
	Xp.append(QR_TE[j-44])
	Xp.append(RISK_TE[j-44])
	#Xp.append(MOV50_TE[j-44])
	Xp.append(MOV10_TE[j-44])
	SVM_test = np.array(Xp)
	length = SVM_test.size
	SVM_test = np.reshape(SVM_test, (1, length))
	prediction = clf.predict(SVM_test)

	f.write(str(price_TE[i-1]-price_TE[i]))
	f.write(str(prediction))
	f.write('\n')

	#Create Array of Predictions
	if prediction == 1:
		y_pred.append(1)
	else:
		y_pred.append(0)

	update(i)	
	i -= 1
	j += 1


#Calculate Correct Targets
end = len(price_TE)
j = price_TE.first_valid_index()-44
y_true = []
while j > price_TE.last_valid_index():
	if price_TE[j]-price_TE[j+44] > 0:
		y_true.append(1)
	else:
		y_true.append(0)
	j -= 1
y_true = np.array(y_true)

##Calculate Profit or Loss
Actual = 0
Earned = 0
j = price_TE.first_valid_index()
i = 0
while j > price_TE.last_valid_index()+44:
	if y_pred[i] == 1:
		Earned = Earned + (price_TE[j-1]-price_TE[j])
	Actual = Actual + (price_TE[j-1]-price_TE[j])
	j-=1
	i+=1
#The profit that would have been earned if we bought the stock
#and didn't sell it until the end of the investment period
print("Actual: " + str(Actual))
#The profit from our series of investments over the investment period
print("Ours: " + str(Earned))
print(stats.accuracy_score(y_true, y_pred))

