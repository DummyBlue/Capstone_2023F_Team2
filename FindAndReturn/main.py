import librosa
import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

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

    features = []
    labels = []

    for k in cFiles:
        for z in cFiles.get(k):
            features.append(extract_mfcc(z))
            labels.append(k)

    for k in vFiles:
        for z in vFiles.get(k):
            features.append(extract_mfcc(z))
            labels.append(k)

    # Machine-Learning Part START
    
    X = np.array(features)
    y = np.array(labels)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    knn_model = KNeighborsClassifier(n_neighbors=5)
    knn_model.fit(X_train, y_train)
    y_pred = knn_model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))

    new_audio_path = os.listdir('./testdata/turtle')

    for k in range(len(new_audio_path)):
        new_audio_path[k] = "./testdata/turtle/" + new_audio_path[k]

    output_dict = {}

    for audio_path in new_audio_path:
        tmp_dict = {}
        predicted_probabilities = predict_new_audio(knn_model, audio_path)
        print(f"Probabilities for {audio_path}:")
        for label, probability in zip(knn_model.classes_, predicted_probabilities):
            tmp_dict[label] = probability * 100
            print(f"  {label} = {probability * 100:.2f}%")
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

