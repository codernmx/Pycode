import math

from flask import Blueprint, jsonify,request
import pymysql
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
import numpy as np
from scipy.optimize import curve_fit
import math
ChinaTrend_api = Blueprint('ChinaTrend_api', __name__)

time = []

provinces = []
list = []

HB_curedCount = []
HB_deadCount = []
HB_confirmedCount = []
HB_confirmedNew = []
HB_curedNew = []
HB_deadNew = []

QG_curedCount = []
QG_deadCount = []
QG_confirmedCount = []
QG_confirmedNew = []
QG_curedNew = []
QG_deadNew = []
conn = pymysql.connect(host='49.232.153.152', user='root', password='137928', port=3306, db='yiqing',
                       charset='utf8mb4')
cursor = conn.cursor()
cursor.execute(
    "SELECT ROUND(AVG(province_confirmedCount)) as count ,ROUND(AVG(province_curedCount)),ROUND(AVG(province_deadCount)),updateTime "
    "from china GROUP BY provinceName,updateTime "
    "HAVING updateTime in (SELECT DISTINCT(updateTime) from china) AND provinceName like '%湖北%'");
result = cursor.fetchall()
for field in result:
    HB_confirmedCount.append(field[0])
    HB_curedCount.append(field[1])
    HB_deadCount.append(field[2])
    time.append(field[3])
HB_treatCount = [HB_confirmedCount[i] - HB_curedCount[i] - HB_deadCount[i] if (HB_confirmedCount[i] - HB_curedCount[
    i] - HB_deadCount[i]) > 0 else 0 for i in range(len(HB_confirmedCount))]
HB_confirmedNew = [
    HB_confirmedCount[i + 1] - HB_confirmedCount[i] if (HB_confirmedCount[i + 1] - HB_confirmedCount[i]) > 0 else 0
    for i in range(0, len(HB_confirmedCount) - 1)]
HB_curedNew = [HB_curedCount[i + 1] - HB_curedCount[i] if (HB_curedCount[i + 1] - HB_curedCount[i]) > 0 else 0 for i
               in range(0, len(HB_curedCount) - 1)]
HB_deadNew = [HB_deadCount[i + 1] - HB_deadCount[i] if (HB_deadCount[i + 1] - HB_deadCount[i]) > 0 else 0 for i in
              range(0, len(HB_deadCount) - 1)]
HB_confirmedNew.insert(0,0)
HB_curedNew.insert(0,0)
HB_deadNew.insert(0,0)
cursor.close()
cursor = conn.cursor()
cursor.execute(
    "SELECT overall.confirmedCount,overall.curedCount,overall.deadCount,time from overall ORDER BY time");
result = cursor.fetchall()
for field in result:
    QG_confirmedCount.append(field[0])
    QG_curedCount.append(field[1])
    QG_deadCount.append(field[2])
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

FHB_confirmedCount = [QG_confirmedCount[i] - HB_confirmedCount[i] for i in range(len(time))]
FHB_curedCount = [QG_curedCount[i] - HB_curedCount[i] for i in range(len(time))]
FHB_deadCount = [QG_deadCount[i] - HB_deadCount[i] for i in range(len(time))]
FHB_treatCount = [QG_treatCount[i] - HB_treatCount[i] for i in range(len(time))]

FHB_confirmedCount[20] = (FHB_confirmedCount[19] + FHB_confirmedCount[21]) / 2
FHB_curedCount[20] = (FHB_curedCount[19] + FHB_curedCount[21]) / 2
FHB_deadCount[20] = (FHB_deadCount[19] + FHB_deadCount[21]) / 2
FHB_treatCount[20] = (FHB_treatCount[19] + FHB_treatCount[21]) / 2
FHB_confirmedNew = [
    FHB_confirmedCount[i] - FHB_confirmedCount[i-1] if (FHB_confirmedCount[i] - FHB_confirmedCount[i-1]) > 0 else 0
    for i in
    range(len(FHB_confirmedCount))]
FHB_curedNew = [FHB_curedCount[i] - FHB_curedCount[i-1] if (FHB_curedCount[i] - FHB_curedCount[i-1]) > 0 else 0 for
                i in
                range(len(FHB_curedCount))]
FHB_deadNew = [FHB_deadCount[i] - FHB_deadCount[i-1] if (FHB_deadCount[i] - FHB_deadCount[i-1]) > 0 else 0 for i in
               range(len(FHB_deadCount))]
FHB_confirmedNew.insert(0,0)
FHB_curedNew.insert(0,0)
FHB_deadNew.insert(0,0)
conn = pymysql.connect(host='49.232.153.152', user='root', password='137928', port=3306, db='yiqing',
                       charset='utf8mb4')
cursor = conn.cursor()
sql = "SELECT DISTINCT(provinceName) from china where provinceName != '中国'"
cursor.execute(sql);
result = cursor.fetchall()
for field in result:
    provinces.append(field[0])
    sql = "SELECT ROUND(AVG(province_confirmedCount)) as count ,ROUND(AVG(province_curedCount)),ROUND(AVG(province_deadCount)),updateTime from china GROUP BY provinceName,updateTime HAVING updateTime in (SELECT DISTINCT(updateTime) from china) AND provinceName like '%" + \
          field[0] + "%'"
    cursor.execute(sql);
    result = cursor.fetchall()
    confirmedCount = []
    curedCount = []
    deadCount = []
    time_all = []
    for field in result:
        confirmedCount.append(field[0])
        curedCount.append(field[1])
        deadCount.append(field[2])
        time_all.append(field[3])
    new_confirmedCount = []
    new_curedCount = []
    new_deadCount = []
    for i in time:
        for j in time_all:
            if(i == j):
                new_confirmedCount.append(confirmedCount[time_all.index(j)])
                new_curedCount.append(curedCount[time_all.index(j)])
                new_deadCount.append(deadCount[time_all.index(j)])
                break
            elif (i<j):
                new_confirmedCount.append(confirmedCount[time_all.index(j)-1])
                new_curedCount.append(curedCount[time_all.index(j)-1])
                new_deadCount.append(deadCount[time_all.index(j) - 1])
                break
            elif (i>j and j==len(time_all)-1):
                new_confirmedCount.append(confirmedCount[time_all.index(j)])
                new_curedCount.append(curedCount[time_all.index(j)])
                new_deadCount.append(deadCount[time_all.index(j)])
    new_confirmedCount = [new_confirmedCount[i] if i<len(new_curedCount) else new_confirmedCount[-1] for i in range(len(time))]
    new_curedCount = [new_curedCount[i] if i < len(new_curedCount) else new_curedCount[-1] for i in range(len(time))]
    new_deadCount = [new_deadCount[i] if i < len(new_deadCount) else new_deadCount[-1] for i in range(len(time))]
    treatCount = [new_confirmedCount[i] - new_curedCount[i] - new_deadCount[i] if (new_confirmedCount[i] - new_curedCount[i] - new_deadCount[i]) > 0 else 0
                  for i in range(len(new_confirmedCount))]
    confirmedNew = [
        new_confirmedCount[i + 1] - new_confirmedCount[i] if (new_confirmedCount[i + 1] - new_confirmedCount[i]) > 0 else 0
        for i in range(0, len(new_confirmedCount) - 1)]
    curedNew = [new_curedCount[i + 1] - new_curedCount[i] if (new_curedCount[i + 1] - new_curedCount[i]) > 0 else 0 for i
                in range(0, len(new_curedCount) - 1)]
    deadNew = [new_deadCount[i + 1] - new_deadCount[i] if (new_deadCount[i + 1] - new_deadCount[i]) > 0 else 0 for i in
               range(0, len(new_deadCount) - 1)]
    confirmedNew.insert(0,0)
    curedNew.insert(0, 0)
    deadNew.insert(0, 0)
    result = {"time": time, "confirmedCount": new_confirmedCount, "curedCount": new_curedCount,
              "deadCount": new_deadCount,
              "treatCount": treatCount, "confirmedNew": confirmedNew, "curedNew": curedNew, "deadNew": deadNew}
    list.append(result)
cursor.close()
conn.close()

@ChinaTrend_api.route('/ztqs/hb',methods=['GET'])
def hb():
    result = {"time": time,"confirmedCount":HB_confirmedCount,"curedCount":HB_curedCount,"deadCount":HB_deadCount,
              "treatCount":HB_treatCount,"confirmedNew":HB_confirmedNew,"curedNew":HB_curedNew,"deadNew":HB_deadNew}
    return jsonify(result)

@ChinaTrend_api.route('/ztqs/qg',methods=['GET'])
def qg():
    result = {"time": time,"confirmedCount":QG_confirmedCount,"curedCount":QG_curedCount,"deadCount":QG_deadCount,
              "treatCount":QG_treatCount,"confirmedNew":QG_confirmedNew,"curedNew":QG_curedNew,"deadNew":QG_deadNew}
    return jsonify(result)

@ChinaTrend_api.route('/ztqs/qgysbh',methods=['GET'])
def qgysbh():
    suspectedCount = []
    suspectedIncr = []
    time = []
    conn = pymysql.connect(host='192.168.85.133', user='root', password='123456', port=3306, db='yiqing',
                           charset='utf8mb4')
    cursor = conn.cursor()
    sql = "SELECT overall.suspectedCount,overall.suspectedIncr,time from overall ORDER BY time;"
    cursor.execute(sql);
    result = cursor.fetchall()
    for field in result:
        suspectedCount.append(field[0])
        suspectedIncr.append(field[1])
        time.append(field[2])
    cursor.close()
    conn.close()
    result = {"time": time,"suspectedCount":suspectedCount,"suspectedIncr":suspectedIncr}
    return jsonify(result)

@ChinaTrend_api.route('/ztqs/fhb',methods=['GET'])
def fhb():
    result = {"time": time,"confirmedCount":FHB_confirmedCount,"curedCount":FHB_curedCount,"deadCount":FHB_deadCount,
              "treatCount":FHB_treatCount,"confirmedNew":FHB_confirmedNew,"curedNew":FHB_curedNew,"deadNew":FHB_deadNew}
    return jsonify(result)

@ChinaTrend_api.route('/ztqs/ljsw',methods=['GET'])
def ljsw():
    ljsw_qg = [ round(QG_deadCount[i]/QG_confirmedCount[i] * 100,2) for i in range(len(QG_deadCount))]
    ljsw_fhb = [round( FHB_deadCount[i]/FHB_confirmedCount[i] *100,2) for i in range(len(FHB_deadCount))]
    ljsw_hb = [round(HB_deadCount[i]/HB_confirmedCount[i]*100,2) for i in range(len(HB_deadCount))]
    result = {"time": time[1:],"qg":ljsw_qg[1:],"fhb":ljsw_fhb[1:],"hb":ljsw_hb[1:]}
    return jsonify(result)

@ChinaTrend_api.route('/ztqs/ljzy',methods=['GET'])
def ljzy():
    ljsw_qg = [ round(QG_curedCount[i]/QG_confirmedCount[i] * 100,2) for i in range(len(QG_curedCount))]
    ljsw_fhb = [round( FHB_curedCount[i]/FHB_confirmedCount[i] *100,2) for i in range(len(FHB_curedCount))]
    ljsw_hb = [round(HB_curedCount[i]/HB_confirmedCount[i]*100,2) for i in range(len(HB_curedCount))]
    result = {"time": time[1:],"qg":ljsw_qg[1:],"fhb":ljsw_fhb[1:],"hb":ljsw_hb[1:]}
    return jsonify(result)

@ChinaTrend_api.route('/ztqs/data',methods=['GET'])
def data():
    limit = int(request.args['limit'])
    page = int(request.args['page'])
    page = (page-1)*limit
    conn = pymysql.connect(host='192.168.85.133', user='root', password='123456', port=3306, db='yiqing',
                           charset='utf8mb4')

    cursor = conn.cursor()
    cursor.execute("select count(*) from china");
    count = cursor.fetchall()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("select * from china limit "+str(page)+","+str(limit));
    data_dict = []
    result = cursor.fetchall()
    for field in result:
        data_dict.append(field)
    table_result = {"code": 0, "msg": None, "count": count[0], "data": data_dict}
    cursor.close()
    conn.close()
    return jsonify(table_result)

@ChinaTrend_api.route('/ztqs/getAllProvinces',methods=['GET'])
def getAllProvinces():
    result = {"provinces": provinces,"list": list}
    return jsonify(result)

@ChinaTrend_api.route('/ztqs/ssdt',methods=['GET'])
def ssdt():
    confirmedCount = []
    province = [provinces[i][0:3]  if ("黑龙江" in provinces[i] or "内蒙古" in provinces[i]) else provinces[i][0:2] for i in range(len(provinces))]
    for i in range(len(time)):
        data_confirmedCount = []
        for j in range(len(province)):
            data_confirmedCount.append(list[j]['confirmedCount'][i])
        confirmedCount.append(data_confirmedCount)
    result = {"provinces": province,"QG_confirmedCount":QG_confirmedCount,"time":time,"confirmedCount":confirmedCount}
    return jsonify(result)

@ChinaTrend_api.route('/ztqs/dqqz',methods=['GET'])
def dqqz():
    confirmedCount = []
    province = [provinces[i][0:3]  if ("黑龙江" in provinces[i] or "内蒙古" in provinces[i]) else provinces[i][0:2] for i in range(len(provinces))]
    for i in range(len(time)):
        data_confirmedCount = []
        for j in range(len(province)):
            data_confirmedCount.append(list[j]['treatCount'][i])
        confirmedCount.append(data_confirmedCount)
    result = {"provinces": province,"QG_confirmedCount":QG_confirmedCount,"time":time,"confirmedCount":confirmedCount}
    return jsonify(result)

@ChinaTrend_api.route('/ztqs/lssw',methods=['GET'])
def lssw():
    confirmedCount = []
    province = [provinces[i][0:3]  if ("黑龙江" in provinces[i] or "内蒙古" in provinces[i]) else provinces[i][0:2] for i in range(len(provinces))]
    for i in range(len(time)):
        data_confirmedCount = []
        for j in range(len(province)):
            data_confirmedCount.append(list[j]['deadCount'][i])
        confirmedCount.append(data_confirmedCount)
    result = {"provinces": province,"QG_confirmedCount":QG_confirmedCount,"time":time,"confirmedCount":confirmedCount}
    return jsonify(result)

@ChinaTrend_api.route('/ztqs/nnHB',methods = ['GET'])
def nnHB():
    l = []
    for i in range(len(HB_confirmedCount)):
        l.append([i, float(HB_confirmedCount[i])])
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

@ChinaTrend_api.route('/ztqs/nnChina',methods = ['GET'])
def nnChina():
    l = []
    for i in range(len(QG_confirmedCount)):
        l.append([i, float(QG_confirmedCount[i])])
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
import joblib
@ChinaTrend_api.route('/ztqs/nnfhf',methods = ['GET'])
def nnfhf():
    l = []
    for i in range(len(QG_treatCount)):
        l.append([i, float(QG_treatCount[i])])
    a = np.array(l).astype(np.int)
    x = a[:, 0]  # get the first column from a
    y = a[:, 1]  ##get the second column from a
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
    X_train = X_train.reshape(-1, 1)
    y_train = y_train
    model_mlp = joblib.load('model/model_mlp4.pkl')
    x1 = x.reshape(-1, 1)
    x = x1

    mlp_score = model_mlp.score(x1, y)
    print('sklearn多层感知器-回归模型得分', mlp_score)  # 预测正确/总数
    result = model_mlp.predict(x1)
    for i in range(len(x1),len(x1)+10):
        result = np.append(result, model_mlp.predict(i))
        x1 = np.append(x1, np.array(i))
    normal = result.copy();
    count = []
    normal = [c*0.95*0.9*0.32*3.5 for c in normal]
    ICU_all = [900000/(1+math.exp((c-20)*(-0.2343))) for c in range(22)]
    ICU = []
    society = []
    for i in range(21):
        society.append(result[i]*0.2+result[i]*0.01*0.008*2+7500)
        ICU.append(ICU_all[i+1] - ICU_all[i])
    for i in range(21,35):
        society.append(result[i]*0.2+result[i]*0.01*0.008*2+7500+50000)
        ICU.append(ICU[-1])
    for i in range(35,len(x1)):
        society.append(result[i] * 0.2 + result[i] * 0.01 * 0.008 * 2 + 7500)
        ICU.append(result[i]*0.2*5.7)
    for i in range(len(normal)):
        count.append(normal[i]+society[i]+ICU[i])
    response = {"mlp_score": mlp_score,"society":society,"ICU":ICU, "y_train": y.tolist(),"normal":normal ,"count":count, "result": result.tolist(), "x1":x1.tolist(), "x":x.tolist()}
    return jsonify(response)

@ChinaTrend_api.route('/ztqs/nnfhf2',methods = ['GET'])
def nnfhf2():
    l = []
    for i in range(len(QG_treatCount)):
        l.append([i, float(QG_treatCount[i])])
    a = np.array(l).astype(np.int)
    x = a[:, 0]  # get the first column from a
    y = a[:, 1]  ##get the second column from a
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
    X_train = X_train.reshape(-1, 1)
    y_train = y_train
    model_mlp = joblib.load('model/model_mlp3.pkl')
    x1 = x.reshape(-1, 1)
    x = x1

    mlp_score = model_mlp.score(x1, y)
    print('sklearn多层感知器-回归模型得分', mlp_score)  # 预测正确/总数
    result = model_mlp.predict(x1)
    for i in range(len(x1),len(x1)+10):
        result = np.append(result, model_mlp.predict(i))
        x1 = np.append(x1, np.array(i))
    normal = result.copy();

    normal = [c*0.95*0.9*0.32*3.5 for c in normal]
    ICU_all = [900000/(1+math.exp((c-20)*(-0.2343))) for c in range(22)]
    ICU = []
    count = []
    society = []
    for i in range(21):
        society.append(result[i]*0.2+result[i]*0.01*0.008*2+7500)
        ICU.append(ICU_all[i+1] - ICU_all[i])
    for i in range(21,35):
        society.append(result[i]*0.2+result[i]*0.01*0.008*2+7500+50000)
        ICU.append(ICU[-1])
    for i in range(35,len(x1)):
        society.append(result[i] * 0.2 + result[i] * 0.01 * 0.008 * 2 + 7500)
        ICU.append(result[i]*0.2*5.7)
    for i in range(len(normal)):
        count.append(normal[i]+society[i]+ICU[i])
    response = {"mlp_score": mlp_score,"society":society,"ICU":ICU, "y_train": y.tolist(),"normal":normal, "count":count, "result": result.tolist(), "x1":x1.tolist(), "x":x.tolist()}
    return jsonify(response)

@ChinaTrend_api.route('/ztqs/seir',methods = ['GET'])
def seir():
    S, E, I, R = [], [], [], []
    N = 59270000  # 人口总数
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
    T = [i for i in range(0, 100)]
    for i in range(0, len(T) - 1):
        S.append(S[i] - r * beta * S[i] * I[i] / N - r2 * beta2 * S[i] * E[i] / N)
        E.append(E[i] + r * beta * S[i] * I[i] / N + r2 * beta2 * S[i] * E[i] / N - alpha * E[i])
        I.append(I[i] + alpha * E[i] - gamma * I[i])  # 计算累计确诊人数
        R.append(R[i] + gamma * I[i])
    response = {"T": T, "S": S, "E": E, "I": I,
                "R": R}
    return jsonify(response)

@ChinaTrend_api.route('/ztqs/qgseir',methods = ['GET'])
def qgseir():
    S, E, I, R = [], [], [], []
    N = 1400050000  # 人口总数
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
    T = [i for i in range(0, 100)]
    for i in range(0, len(T) - 1):
        S.append(S[i] - r * beta * S[i] * I[i] / N - r2 * beta2 * S[i] * E[i] / N)
        E.append(E[i] + r * beta * S[i] * I[i] / N + r2 * beta2 * S[i] * E[i] / N - alpha * E[i])
        I.append(I[i] + alpha * E[i] - gamma * I[i])  # 计算累计确诊人数
        R.append(R[i] + gamma * I[i])
    response = {"T": T, "S": S, "E": E, "I": I,
                "R": R}
    return jsonify(response)