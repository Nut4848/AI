import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

# === Part 1: Load Data ===
mnist = tf.keras.datasets.mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

print("train_images shape:", train_images.shape)
print("train_labels shape:", train_labels.shape)
print("test_images shape:", test_images.shape)
print("test_labels shape:", test_labels.shape)

# Displaying first 9 images (Optional visual check)
fig = plt.figure(figsize=(10, 10))
nrows = 3
ncols = 3
for i in range(9):
    fig.add_subplot(nrows, ncols, i+1)
    plt.imshow(train_images[i])
    plt.title("Digit: {}".format(train_labels[i]))
    plt.axis(False)
plt.show()

# === Part 2: Preprocessing ===
# Normalize pixel values to be between 0 and 1
train_images = train_images / 255.0
test_images = test_images / 255.0

print("First Label before conversion:")
print(train_labels[0])

# One-hot encoding
train_labels = tf.keras.utils.to_categorical(train_labels)
test_labels = tf.keras.utils.to_categorical(test_labels)

print("First Label after conversion:")
print(train_labels[0])

# === Part 3: Build Model ===
model = tf.keras.Sequential([
    # Flatten Layer: converts 28x28 images to 1D array (784 inputs)
    tf.keras.layers.Flatten(input_shape=(28, 28)), 
    
    # Hidden Layer: 512 units, relu activation
    tf.keras.layers.Dense(units=512, activation='relu'),
    
    # Output Layer: 10 units (for digits 0-9), softmax activation
    tf.keras.layers.Dense(units=10, activation='softmax')
])

# === Part 4: Compile Model ===
model.compile(
    loss='categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)

# === Part 5: Train Model ===
history = model.fit(
    x=train_images,
    y=train_labels,
    epochs=10
)

# Plotting Loss
plt.plot(history.history['loss'])
plt.xlabel('epochs')
plt.legend(['loss'])
plt.show()

# Plotting Accuracy
plt.plot(history.history['accuracy'], color='orange')
plt.xlabel('epochs')
plt.legend(['accuracy'])
plt.show()

# === Part 6: Evaluate ===
test_loss, test_accuracy = model.evaluate(
    x=test_images,
    y=test_labels
)
print("Test Loss: %.4f" % test_loss)
print("Test Accuracy: %.4f" % test_accuracy)

# === Part 7: Prediction ===
predicted_probabilities = model.predict(test_images)
predicted_classes = tf.argmax(predicted_probabilities, axis=-1).numpy()

index = 11

# Show the image being predicted
plt.imshow(test_images[index])
plt.show()

# Print results
print("Probabilities predicted for image at index", index)
print(predicted_probabilities[index])
print()
print("Predicted class for image at index", index)
print(predicted_classes[index])