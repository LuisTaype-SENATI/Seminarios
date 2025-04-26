import cv2

prototxt = "model/MobileNetSSD_deploy.prototxt.txt"
model = "model/MobileNetSSD_deploy.caffemodel"



classes = {0:"backgroud", 1:"dog",
          2:"bird", 3:"mouse", 4:"pajaro"}


net = cv2.dnn.readNetFromCaffe(prototxt, model)


image = cv2.imread("imagenes/imagen18.jpg")
height, width, _ = image.shape
image_resized = cv2.resize(image, (300, 300))


blob = cv2.dnn.blobFromImage(image_resized, 0.007843, (300, 300), (127.5, 127.5, 127.5))
print("blob.shape:", blob.shape)

net.setInput(blob)
detections = net.forward()

for detection in detections[0][0]:
     print(detection)

     if detection[1] > 0.45:
          label = classes[detection[0]]
          print("Label:", label)
          box = detection[3:7] * [width, height, width, height]
          x_start, y_start, x_end, y_end = int(box[0]), int(box[1]), int(box[2]), int(box[3])
          cv2.putText(image, "Conf: {:.2f}".format(detection[2] * 100), (x_start, y_start - 5), 1, 1.2, (255, 0, 0), 2)
          cv2.putText(image, label, (x_start, y_start - 25), 1, 1.2, (255, 0, 0), 2)

     cv2.rectangle(image, (x_start, y_start), (x_end, y_end), (0, 255, 0), 2)
          
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()