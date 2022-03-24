import math

from flask import Blueprint, jsonify,request
import pymysql
import json
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
import numpy as np
from scipy.optimize import curve_fit

WorldTTrend_api = Blueprint('WorldTTrend_api', __name__)

time = []

countries = []
list = []

QG_curedCount = []
QG_deadCount = []
QG_confirmedCount = []
QG_confirmedNew = []
QG_curedNew = []
QG_deadNew = []
conn = pymysql.connect(host='127.0.0.1', user='root', password='137928', port=3306, db='yiqing',
                       charset='utf8mb4')
cursor = conn.cursor()
cursor.execute(
    "SELECT overall.confirmedCount,overall.curedCount,overall.deadCount,time from overall ORDER BY time");
result = cursor.fetchall()
for field in result:
    QG_confirmedCount.append(field[0])
    QG_curedCount.append(field[1])
    QG_deadCount.append(field[2])
    time.append(field[3])
QG_treatCount = [QG_confirmedCount[i] - QG_curedCount[i] - QG_deadCount[i] if (QG_confirmedCount[i] - QG_curedCount[
    i] - QG_deadCount[i]) > 0 else 0 for i in range(len(QG_confirmedCount))]
QG_confirmedNew = [
    QG_confirmedCount[i + 1] - QG_confirmedCount[i] if (QG_confirmedCount[i + 1] - QG_confirmedCount[i]) > 0 else 0
    for i in range(0, len(QG_confirmedCount) - 1)]
QG_curedNew = [QG_curedCount[i + 1] - QG_curedCount[i] if (QG_curedCount[i + 1] - QG_curedCount[i]) > 0 else 0 for i
               in range(0, len(QG_curedCount) - 1)]
QG_deadNew = [QG_deadCount[i + 1] - QG_deadCount[i] if (QG_deadCount[i + 1] - QG_deadCount[i]) > 0 else 0 for i in
              range(0, len(QG_deadCount) - 1)]
QG_confirmedNew.insert(0,0)
QG_curedNew.insert(0,0)
QG_deadNew.insert(0,0)
cursor.close()
conn.close()

conn = pymysql.connect(host='127.0.0.1', user='root', password='137928', port=3306, db='yiqing',
                       charset='utf8mb4')
cursor = conn.cursor()
sql = "SELECT DISTINCT(countryName) from abroad "
cursor.execute(sql);
result = cursor.fetchall()
for field in result:
    countries.append(field[0])

for field in countries:
    time_all = []
    confirmedCount = []
    new_confirmedCount = []
    confirmedCount = []
    new_confirmedCount = []
    curedCount = []
    new_curedCount = []
    deadCount = []
    new_deadCount = []
    sql = "SELECT ROUND(AVG(province_confirmedCount)),updateTime,ROUND(AVG(province_curedCount)),ROUND(AVG(province_deadCount)) from abroad GROUP BY countryName,updateTime HAVING updateTime in (SELECT DISTINCT(updateTime) from abroad) AND countryName like '%" + \
          field + "%' ORDER BY updateTime"
    cursor.execute(sql);
    result = cursor.fetchall()

    for field in result:
        confirmedCount.append(field[0])
        time_all.append(field[1])
        curedCount.append(field[2])
        deadCount.append(field[3])
    for i in time:
        for j in time_all:
            if (i < time_all[0]):
                new_confirmedCount.append(0)
                new_curedCount.append(0)
                new_deadCount.append(0)
                break
            if( i == j):
                new_confirmedCount.append(confirmedCount[time_all.index(j)])
                new_curedCount.append(curedCount[time_all.index(j)])
                new_deadCount.append(deadCount[time_all.index(j)])
                break
            elif (i<j and j>time_all[0]):
                new_confirmedCount.append(confirmedCount[time_all.index(j)-1])
                new_curedCount.append(curedCount[time_all.index(j) - 1])
                new_deadCount.append(deadCount[time_all.index(j) - 1])
                break
            elif (i>j and j==len(time_all)-1):
                new_confirmedCount.append(confirmedCount[j])
                new_curedCount.append(curedCount[j])
                new_deadCount.append(deadCount[j])
                break
    for i in range(len(new_confirmedCount),len(time)):
        new_confirmedCount.append(new_confirmedCount[-1])
        new_curedCount.append(new_curedCount[-1])
        new_deadCount.append(new_deadCount[-1])
    result = {"confirmedCount": new_confirmedCount,"curedCount": new_curedCount,"deadCount": new_deadCount,"time":time}
    list.append(result)
cursor.close()
conn.close()
with open('service/country.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
c = {val:key for key,val in data.items()}

@WorldTTrend_api.route('/sjdt/getAllCountries',methods=['GET'])
def getAllCountries():
    countries_new = countries.copy()
    countries_eng = []
    confirmedCount = []
    sum_data = []
    for i in range(len(time)):
        data_confirmedCount = []
        for j in range(len(countries)):
            data_confirmedCount.append(list[j]['confirmedCount'][i])
        data_confirmedCount.append(QG_confirmedCount[i])
        confirmedCount.append(data_confirmedCount)
        sum_data.append(sum(data_confirmedCount))
    countries_new.append('中国')
    for i in countries_new:
        if(c.get(i)):
            countries_eng.append(c[i])
        else:
            countries_eng.append(i)
    result = {"countries": countries_new,"countries_eng":countries_eng,"time":time,"confirmedCount":confirmedCount,"sum_data":sum_data}
    return jsonify(result)

@WorldTTrend_api.route('/sjdt/getAllCountriesTreatCount',methods=['GET'])
def getAllCountriesTreatCount():
    countries_new = countries.copy()
    countries_eng = []
    treatCount = []
    sum_data = []
    for i in range(len(time)):
        data_treatCount = []
        for j in range(len(countries)):
            data_treatCount.append(list[j]['confirmedCount'][i]-list[j]['curedCount'][i]-list[j]['deadCount'][i])
        data_treatCount.append(QG_treatCount[i])
        treatCount.append(data_treatCount)
        sum_data.append(sum(data_treatCount))
    countries_new.append('中国')
    for i in countries_new:
        if(c.get(i)):
            countries_eng.append(c[i])
        else:
            countries_eng.append(i)
    result = {"countries": countries_new,"countries_eng":countries_eng,"time":time,"confirmedCount":treatCount,"sum_data":sum_data}
    return jsonify(result)


@WorldTTrend_api.route('/sjdt/nnQQ',methods = ['GET'])
def nnQQ():
    confirmedCount = []
    sum_data = []
    for i in range(len(time)):
        data_confirmedCount = []
        for j in range(len(countries)):
            data_confirmedCount.append(list[j]['confirmedCount'][i])
        data_confirmedCount.append(QG_confirmedCount[i])
        confirmedCount.append(data_confirmedCount)
        sum_data.append(sum(data_confirmedCount))
    l = []
    for i in range(len(sum_data)):
        l.append([i, float(sum_data[i])])
    a = np.array(l).astype(np.int)
    x = a[:, 0]  # get the first column from a
    y = a[:, 1]  ##get the second column from a
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
    X_train = X_train.reshape(-1, 1)
    y_train = y_train
    model_mlp = MLPRegressor(
    hidden_layer_sizes=(1000,),  activation='relu', solver='lbfgs', alpha=0.0001, batch_size='auto',
    learning_rate='invscaling', learning_rate_init=0.001, power_t=0.5, max_iter=8000, shuffle=True,
    random_state=1, tol=0.0001, verbose=False, warm_start=False, momentum=0.9, nesterovs_momentum=True,
    early_stopping=False,beta_1=0.9, beta_2=0.999, epsilon=1e-08)
    model_mlp.fit(X_train, y_train)
    x1 = x.reshape(-1, 1)
    x = x1
    mlp_score = model_mlp.score(x1, y)
    print('sklearn多层感知器-回归模型得分', mlp_score)  # 预测正确/总数
    result = model_mlp.predict(x1)
    for i in range(len(x1),len(x1)+10):
        result = np.append(result, model_mlp.predict(i))
        x1 = np.append(x1, np.array(i))
    response = {"mlp_score": mlp_score, "y_train": y.tolist(), "result": result.tolist(), "x1":x1.tolist(), "x":x.tolist()}
    return jsonify(response)

@WorldTTrend_api.route('/sjdt/logisticQQ',methods = ['GET'])
def logisticQQ():
    confirmedCount = []
    sum_data = []
    for i in range(len(time)):
        data_confirmedCount = []
        for j in range(len(countries)):
            data_confirmedCount.append(list[j]['confirmedCount'][i])
        data_confirmedCount.append(QG_confirmedCount[i])
        confirmedCount.append(data_confirmedCount)
        sum_data.append(sum(data_confirmedCount))
    predict_y = predict(sum_data)
    response = { "y_train": sum_data, "result": predict_y.tolist(), "x1":np.arange(len(sum_data)+10).tolist()}
    return jsonify(response)

def logistic_function(t, K, P0, r):
    t0 = 0
    exp = np.exp(r * (t - t0))
    return (K * exp * P0) / (K + (exp - 1) * P0)

def predict(data):
    predict_days = 10  # 预测未来天数
    confirm = data.copy()
    x = np.arange(len(confirm))
    # 用最小二乘法估计拟合
    popt, pcov = curve_fit(logistic_function, x, confirm)
    # 近期情况预测
    predict_x = x.tolist() + [x[-1] + i for i in range(1, 1 + predict_days)]
    predict_x = np.array(predict_x)
    predict_y = logistic_function(predict_x, popt[0], popt[1], popt[2])
    return predict_y

@WorldTTrend_api.route('/sjdt/seir',methods = ['GET'])
def seir():
    S, E, I, R = [], [], [], []
    N = 7585204179  # 人口总数
    I.append(1)
    S.append(N - I[0])
    E.append(0)
    R.append(0)
    r = 20  # 传染者接触人数
    r2 = 30
    beta = 0.03  # 传染者传染概率
    beta2 = 0.03  # 易感染者被潜伏者感染的概率
    alpha = 0.14  # 潜伏者患病概率 1/7
    gamma = 0.1  # 康复概率
    T = [i for i in range(0, 150)]
    for i in range(0, len(T) - 1):
        S.append(S[i] - r * beta * S[i] * I[i] / N - r2 * beta2 * S[i] * E[i] / N)
        E.append(E[i] + r * beta * S[i] * I[i] / N + r2 * beta2 * S[i] * E[i] / N - alpha * E[i])
        I.append(I[i] + alpha * E[i] - gamma * I[i])  # 计算累计确诊人数
        R.append(R[i] + gamma * I[i])
    response = {"T": T, "S": S, "E": E, "I": I,
                "R": R}
    return jsonify(response)

import joblib
@WorldTTrend_api.route('/sjdt/nnfhf',methods = ['GET'])
def nnfhf():
    treatCount = []
    sum_data = []
    for i in range(len(time)):
        data_treatCount = []
        for j in range(len(countries)):
            data_treatCount.append(list[j]['confirmedCount'][i] - list[j]['curedCount'][i] - list[j]['deadCount'][i])
        data_treatCount.append(QG_treatCount[i])
        treatCount.append(data_treatCount)
        sum_data.append(sum(data_treatCount))
    l = []
    for i in range(len(sum_data)):
        l.append([i, float(sum_data[i])])
    a = np.array(l).astype(np.int)
    x = a[:, 0]  # get the first column from a
    y = a[:, 1]  ##get the second column from a
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
    X_train = X_train.reshape(-1, 1)
    y_train = y_train
    model_mlp = joblib.load('model/model_mlp5.pkl')
    x1 = x.reshape(-1, 1)
    x = x1

    mlp_score = model_mlp.score(x1, y)
    print('sklearn多层感知器-回归模型得分', mlp_score)  # 预测正确/总数
    result = model_mlp.predict(x1)
    for i in range(len(x1), len(x1) + 10):
        result = np.append(result, model_mlp.predict(i))
        x1 = np.append(x1, np.array(i))
    normal = result.copy();
    count = []
    normal = [c * 0.95 * 0.9 * 0.32 * 3.5 for c in normal]
    ICU_all = [900000 / (1 + math.exp((c - 20) * (-0.2343))) for c in range(22)]
    ICU = []
    society = []
    for i in range(21):
        society.append(result[i] * 0.2 + result[i] * 0.01 * 0.008 * 2 + 7500)
        ICU.append(ICU_all[i + 1] - ICU_all[i])
    for i in range(21, 35):
        society.append(result[i] * 0.2 + result[i] * 0.01 * 0.008 * 2 + 7500 + 50000)
        ICU.append(ICU[-1])
    for i in range(35, len(x1)):
        society.append(result[i] * 0.2 + result[i] * 0.01 * 0.008 * 2 + 7500)
        ICU.append(result[i] * 0.2 * 5.7)
    for i in range(len(normal)):
        count.append(normal[i] + society[i] + ICU[i])
    response = {"mlp_score": mlp_score, "society": society, "ICU": ICU, "y_train": y.tolist(), "normal": normal,
                "count": count, "result": result.tolist(), "x1": x1.tolist(), "x": x.tolist()}
    return jsonify(response)
