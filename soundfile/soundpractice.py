import librosa
import numpy as np
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

audio_paths = ['korean_q.mp3','korean_w.mp3','korean_e.mp3','korean_r.mp3','korean_a.mp3','korean_s.mp3','korean_d.mp3','korean_f.mp3','korean_z.mp3','korean_x.mp3','korean_c.mp3','korean_v.mp3','korean_t.mp3','korean_g.mp3','korean_y.mp3','korean_u.mp3','korean_i.mp3','korean_o.mp3','korean_p.mp3','korean_h.mp3','korean_j.mp3','korean_k.mp3','korean_l.mp3','korean_b.mp3','korean_n.mp3','korean_m.mp3']
labels = [path.split('_')[0] for path in audio_paths]

features = [extract_mfcc(path) for path in audio_paths]
X = np.array(features)
y = np.array(labels)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(X_train, y_train)
y_pred = knn_model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

new_audio_path = ['turtle.mp3'] 

for audio_path in new_audio_path:
    predicted_probabilities = predict_new_audio(knn_model, audio_path)
    print(f"Probabilities for {audio_path}:")
    for label, probability in zip(knn_model.classes_, predicted_probabilities):
        print(f"  {label} = {probability * 100:.2f}%")
    print("\n")
