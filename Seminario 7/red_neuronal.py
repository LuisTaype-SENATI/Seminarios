import numpy as np
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
from sklearn.preprocessing import StandardScaler

# Ejemplo de edad, peso, ejercicio para el entranamiento
X = np.array([
    [25, 70, 5],[45, 85, 1],[35, 60, 3],[50, 90, 0],[23, 65, 6],[60, 80, 0]
])

# 0 = no hipertensión y 1 = hipertensión
y = np.array([0, 1, 0, 1, 0, 1])  

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Modelo simple con 3 capas
model = Sequential([
    Dense(8, activation='relu', input_shape=(3,)),
    Dense(4, activation='relu'),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X_scaled, y, epochs=100, verbose=0)

# Solicitamos datos
print("Ingresa tus datos para predecir hipertensión:")

try:
    edad = float(input("Edad: "))
    peso = float(input("Peso: "))
    ejercicio = float(input("Horas de ejercicio por semana: "))
except ValueError:
    print("Ingrese un número valido.")
    exit()

user_data = np.array([[edad, peso, ejercicio]])
user_data_scaled = scaler.transform(user_data)

# S e realiza la predicción
prediccion = model.predict(user_data_scaled)[0][0]
probabilidad = prediccion * 100

if prediccion >= 0.5:
    print(f"Probabilidad de hipertensión: {probabilidad:.2f}% Resultado: (+) POSITIVO")
else:
    print(f"Probabilidad de hipertensión: {probabilidad:.2f}% Resultado: (-) NEGATIVO")
