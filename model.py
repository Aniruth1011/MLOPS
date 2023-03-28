import pandas as pd
from sklearn.naive_bayes import GaussianNB
data = pd.read_csv(r"C:\Users\aniru\Downloads\MLT\NN\Churn_Modelling\Churn_Modelling.csv")

x = data[['Age' , 'Tenure' , 'Balance' , 'NumOfProducts' , 'EstimatedSalary' ]]
y = data['Exited']
nve = GaussianNB()
nve.fit(x , y)
import pickle

pickle.dump(nve,open('model.pkl','wb'))
