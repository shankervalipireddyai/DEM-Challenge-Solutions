
from sklearn import datasets
from sklearn.svm import SVC
import pickle
import pandas as pd
import warnings

warnings.filterwarnings("ignore",category=FutureWarning, module='sklearn',lineno=196)


iris = datasets.load_iris()
X = iris.data 
y = iris.target

df = pd.DataFrame(data=X,columns=iris.feature_names)
df['target'] = y

df = df.sample(frac=1).reset_index(drop=True)
clf =SVC(probability=True)
clf.fit(df.drop(columns='target'),df.target)

filename = 'iris_model.sav'
pickle.dump(clf, open(filename, 'wb'))
