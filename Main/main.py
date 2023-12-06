import librosa
import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score

from inspector import *
from slicer import *
from correction import *

def extract_mfcc(audio_path):
    y, sr = librosa.load(audio_path, sr=None)
    mfccs = librosa.feature.mfcc(y=y, sr=sr)
    return np.mean(mfccs.T, axis=0)

def predict_new_audio(model, audio_path):
    new_feature = extract_mfcc(audio_path)
    return model.predict_proba([new_feature])[0]

def doProcess():
    topPath = "./sounddata/"
    cPath = topPath + "consonant/"
    vPath = topPath + "vowel/"

    cFolder = os.listdir(cPath)
    vFolder = os.listdir(vPath)

    cName = [path.split('_')[1] for path in cFolder]
    vName = [path.split('_')[1] for path in vFolder]

    for k in range(len(cFolder)):
        cFolder[k] = cPath + cFolder[k]

    for j in range(len(vFolder)):
        vFolder[j] = vPath + vFolder[j]

    cFiles = {}
    vFiles = {}

    for k in range(len(cFolder)):
        tmp_list = os.listdir(cFolder[k])

        for z in range(len(tmp_list)):
            tmp_list[z] = cFolder[k] + "/" + tmp_list[z]

        cFiles[cName[k]] = tmp_list

    for k in range(len(vFolder)):
        tmp_list = os.listdir(vFolder[k])

        for z in range(len(tmp_list)):
            tmp_list[z] = vFolder[k] + "/" + tmp_list[z]

        vFiles[vName[k]] = tmp_list

    features_cv = []
    labels_cv = []

    features = []
    labels = []

    features_c = []
    labels_c = []

    features_v = []
    labels_v = []

    # 자음/모음만 구분하기 위한 특성 추출
    for k in cFiles:
        for z in cFiles.get(k):
            features_cv.append(extract_mfcc(z))
            labels_cv.append("Consonant")

    for k in vFiles:
        for z in vFiles.get(k):
            features_cv.append(extract_mfcc(z))
            labels_cv.append("Vowel")

    # 모든 키룰 구분하기 위한 특성 추출
    for k in cFiles:
        for z in cFiles.get(k):
            features.append(extract_mfcc(z))
            features_c.append(extract_mfcc(z))
            labels.append(k)
            labels_c.append(k)

    for k in vFiles:
        for z in vFiles.get(k):
            features.append(extract_mfcc(z))
            features_v.append(extract_mfcc(z))
            labels.append(k)
            labels_v.append(k)

    # 학습 비율 일괄 지정을 위한 변수
    ts_size = 0.3

    # 자음/모음만 구분하는 모델
    Xcv = np.array(features_cv)
    ycv = np.array(labels_cv)

    X_train, X_test, y_train, y_test = train_test_split(Xcv, ycv, test_size=ts_size)

    rf_modelcv = RandomForestClassifier()
    rf_modelcv.fit(X_train, y_train)
    y_pred = rf_modelcv.predict(X_test)
    print("자음과 모음만을 구분하는 모델:", f1_score(y_test, y_pred, average="micro"))
    # ----------

    # 자음만 학습한 모델
    Xc = np.array(features_c)
    yc = np.array(labels_c)

    X_train, X_test, y_train, y_test = train_test_split(Xc, yc, test_size=ts_size)

    rf_modelc = RandomForestClassifier()
    rf_modelc.fit(X_train, y_train)
    y_pred = rf_modelc.predict(X_test)
    print("자음만을 구분하는 모델:", f1_score(y_test, y_pred, average="micro"))
    # ----------

    # 모음만 학습한 모델
    Xv = np.array(features_v)
    yv = np.array(labels_v)

    X_train, X_test, y_train, y_test = train_test_split(Xv, yv, test_size=ts_size)

    rf_modelv = RandomForestClassifier()
    rf_modelv.fit(X_train, y_train)
    y_pred = rf_modelv.predict(X_test)
    print("모음만을 구분하는 모델:", f1_score(y_test, y_pred, average="micro"))
    # ----------

    # 모든 키를 학습하는 모델
    X = np.array(features)
    y = np.array(labels)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=ts_size)

    rf_model = RandomForestClassifier()
    rf_model.fit(X_train, y_train)
    y_pred = rf_model.predict(X_test)
    print("모든 키를 구분하는 모델:", f1_score(y_test, y_pred, average="micro"))
    # ----------

    new_audio_path = os.listdir('./testdata/turtle')

    for k in range(len(new_audio_path)):
        new_audio_path[k] = "./testdata/turtle/" + new_audio_path[k]

    output_dict = {}

    for audio_path in new_audio_path:
        tmp_dict_cv = {}
        tmp_dict = {}
        tmp_con = 0
        tmp_vow = 0
        predicted_probabilities = predict_new_audio(rf_modelcv, audio_path)
        print(f"Probabilities for {audio_path}:")
        for label, probability in zip(rf_modelcv.classes_, predicted_probabilities):
            tmp_dict_cv[label] = probability * 100
            print(f"  {label} = {probability * 100:.2f}%")

            if(label == "Consonant"):
                tmp_con = probability * 100
            else:
                tmp_vow = probability * 100

        if(tmp_con > tmp_vow): # 자음일 경우
            c_prob = predict_new_audio(rf_modelc, audio_path)
            print(f"Consonant Probabilities for {audio_path}:")
            for labelc, probc in zip(rf_modelc.classes_, c_prob):
                tmp_dict[labelc] = probc * 100
                print(f"  {labelc} = {probc * 100:.2f}%")

        elif(tmp_con < tmp_vow): # 모음일 경우
            v_prob = predict_new_audio(rf_modelv, audio_path)
            print(f"Vowel Probabilities for {audio_path}:")
            for labelv, probv in zip(rf_modelv.classes_, v_prob):
                tmp_dict[labelv] = probv * 100
                print(f"  {labelv} = {probv * 100:.2f}%")

        else: # 같은 경우
            prob = predict_new_audio(rf_model, audio_path)
            print(f"All Keys Probabilities for {audio_path}:")
            for labelcv, probcv in zip(rf_model.classes_, prob):
                tmp_dict[labelcv] = probcv * 100
                print(f"  {labelcv} = {probcv * 100:.2f}%")


        print("\n")

        sorted_dict = sorted(tmp_dict.items(), key=lambda item: item[1], reverse=True)

        top5_dict = {}
        for k in range(0, 5):
            top5_dict[sorted_dict[k][0]] = sorted_dict[k][1]

        output_dict[audio_path] = top5_dict

    return output_dict

if __name__ == '__main__':
    final_rst = doProcess()
    print(final_rst)

