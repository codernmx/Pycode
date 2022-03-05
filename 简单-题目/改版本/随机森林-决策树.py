import pandas as pd
import numpy as np
from sklearn. model_selection import train_test_split
from sklearn. tree import DecisionTreeClassifier
from sklearn. ensemble import RandomForestClassifier
from sklearn. model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
from sklearn. metrics import classification_report
from sklearn. metrics import confusion_matrix
from sklearn. metrics import roc_curve, auc
import matplotlib. pyplot as plt
import seaborn as sns
import warnings
warnings. filterwarnings("ignore")

df = pd.read_csv("pima-indians-diabetes.csv")

# df

df.isnull().sum()  #处理数据删除非 0

df.describe()  #describe计算的字段有count（非空值数）

for i in df.columns:
    print('%s的值为'%i)
    print(np.unique(df[i]))

# for i in df.columns:
#      if i !='class':
#         df[i].plot.hist(bins=15,title=i)
#         plt.show()
#
# y = df['class']
# x = df. drop (columns=['class'])
#
# train,test,train_y,test_y=train_test_split(x,y,random_state=123)
# dt_clf=DecisionTreeClassifier(random_state=123)
# dt_clf.fit(train,train_y)
# print('决策树精度:%.6f' % accuracy_score(test_y,dt_clf.predict(test)))
#
#
# rf_clf = RandomForestClassifier(random_state=123,n_jobs=-1)
# parameters={'n_estimators':(100,150,200),'criterion':('gini','entropy')}
# grid_clf = GridSearchCV(rf_clf, parameters)
# grid_clf.fit(train, train_y)
#
#
# rf_clf=RandomForestClassifier(random_state=123)
# rf_clf.fit(train,train_y)
# print('随机森林精度:%.6f' % accuracy_score(test_y,rf_clf.predict(test)))
#
# print('分类报告:')
# print(classification_report(test_y,grid_clf.predict(test),target_names=['0','1']))
#
# print ('混淆矩阵:')
# confusion_matrix(test_y,grid_clf.predict(test))
#
# fpr,tpr,thersholds=roc_curve(test_y,grid_clf.predict(test),pos_label=1)
# roc_auc=auc(fpr,tpr)
#
#
# #使用matlab绘制图
# plt.plot(fpr,tpr,'k-',label='ROC={0:.2f}'.format(roc_auc))
# plt.plot([0,1],[0,1],color="navy",linestyle="--")
# plt.xlim([0,1])
# plt.ylim([0,1])
# plt.xlabel('FPR')
# plt.ylabel('TPR')
# plt.title('ROC Curve')
# plt.legend(loc="lower right")
# plt.show()
