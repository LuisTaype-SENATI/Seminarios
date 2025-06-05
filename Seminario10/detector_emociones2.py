import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Cargar modelo y etiquetas
modelo = load_model("modelo_emociones.h5")
emociones = ['Enojo', 'Disgusto', 'Miedo', 'Feliz', 'Triste', 'Sorpresa', 'Neutral']
colores = {
    'Enojo': (0, 0, 255),
    'Disgusto': (0, 128, 0),
    'Miedo': (255, 0, 255),
    'Feliz': (0, 255, 0),
    'Triste': (255, 0, 0),
    'Sorpresa': (0, 255, 255),
    'Neutral': (128, 128, 128)
}


detector_rostros = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
camara = cv2.VideoCapture(0)

print("Presionar '.' para salir")

while True:
    ret, frame = camara.read()
    if not ret:
        break

    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rostros = detector_rostros.detectMultiScale(gris, 1.3, 5)

    for (x, y, w, h) in rostros:
        roi = gris[y:y + h, x:x + w]
        roi = cv2.resize(roi, (48, 48))
        roi = roi.astype("float32") / 255.0
        roi = np.expand_dims(roi, axis=0)
        roi = np.expand_dims(roi, axis=-1)

        prediccion = modelo.predict(roi)[0]
        emocion_idx = np.argmax(prediccion)
        emocion = emociones[emocion_idx]
        confianza = prediccion[emocion_idx]

        color = colores.get(emocion, (255, 255, 255))
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
        texto = f"{emocion} ({confianza*100:.1f}%)"
        cv2.putText(frame, texto, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

    cv2.imshow("Detector de Emociones", frame)
    if cv2.waitKey(1) & 0xFF == ord('.'):
        break

camara.release()
cv2.destroyAllWindows()
