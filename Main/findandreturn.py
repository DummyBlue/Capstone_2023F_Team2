import librosa
import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score
from sklearn.model_selection import GridSearchCV

params = { 'n_estimators' : [10, 100],
           'max_depth' : [6, 8, 10, 12],
           'min_samples_leaf' : [8, 12, 18],
           'min_samples_split' : [8, 16, 20]
            }

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
            labels.append(k)

    for k in vFiles:
        for z in vFiles.get(k):
            features.append(extract_mfcc(z))
            labels.append(k)

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

    # 모든 키를 학습하는 모델
    X = np.array(features)
    y = np.array(labels)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=ts_size)

    rf_model = RandomForestClassifier()

    # GridSearch를 이용한 하이퍼파라미터 튜닝 수행
    grid_cv = GridSearchCV(rf_model, param_grid=params, cv=3, n_jobs=-1)
    grid_cv.fit(X_train, y_train)

    print('최적 하이퍼 파라미터: ', grid_cv.best_params_)
    print('최고 예측 정확도: {:.4f}'.format(grid_cv.best_score_))

    tmp_params = grid_cv.best_params_
    print(tmp_params)

    rf_model_custom = RandomForestClassifier(n_estimators=tmp_params['n_estimators'], max_depth=tmp_params['max_depth'], min_samples_leaf=tmp_params['min_samples_leaf'], min_samples_split=tmp_params['min_samples_split'])

    rf_model_custom.fit(X_train, y_train)
    y_pred = rf_model_custom.predict(X_test)
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

        prob = predict_new_audio(rf_model_custom, audio_path)
        print(f"All Keys Probabilities for {audio_path}:")
        for labelcv, probcv in zip(rf_model_custom.classes_, prob):
            tmp_dict[labelcv] = probcv * 100
            print(f"  {labelcv} = {probcv * 100:.2f}%")

        print("\n")

        sorted_dict = sorted(tmp_dict.items(), key=lambda item: item[1], reverse=True)

        top5_dict = {}
        for k in range(0, 5):
            top5_dict[sorted_dict[k][0]] = sorted_dict[k][1]

        output_dict[audio_path] = top5_dict

    return output_dict