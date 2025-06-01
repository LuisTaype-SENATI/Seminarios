from ultralytics import YOLO
import cv2

#Carga de modelo preentrenado de Yolo8
model = YOLO('yolov8n.pt')
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    results = model(frame)
    annotated = results[0].plot()

    #Mostrar imagen en detección
    cv2.imshow('Detección', annotated)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
