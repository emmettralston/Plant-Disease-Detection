# Plant Disease Detection System

This repository contains two Raspberry Pi applications for automated greenhouse monitoring:

* **Real-time leaf disease identification** using a TensorFlow Lite image classification model and an attached USB camera or Pi Camera module.
* **Humidity-driven irrigation control** that toggles a relay-controlled water pump based on readings from a DHT11 sensor.

An accompanying Jupyter notebook (`ModelTraining.ipynb`) is included for retraining the image classifier.

## Project structure

| File | Description |
| --- | --- |
| `Plant_Disease_Detection.py` | Captures live frames from a camera, runs inference with a `.tflite` model, and displays the predicted class on both the video feed and an I²C LCD. |
| `HumiditySensor_WaterPump.py` | Monitors temperature and humidity, turns the pump relay on below the humidity threshold (60%) and off otherwise. |
| `ModelTraining.ipynb` | Notebook for training or fine-tuning the plant disease classifier before exporting to TensorFlow Lite. |

## Hardware requirements

- Raspberry Pi with GPIO access
- Pi Camera or USB camera supported by OpenCV
- I²C LCD display (compatible with the `drivers` module used in the scripts)
- DHT11 temperature/humidity sensor
- Relay module controlling a water pump

## Software prerequisites

Install the following packages on your Raspberry Pi (preferably in a virtual environment):

```bash
sudo apt update
sudo apt install python3-opencv python3-pip
pip3 install tflite-runtime adafruit-circuitpython-dht RPi.GPIO
```

> **Note:** The `drivers` module is assumed to be available on the Pi for LCD control. If you are using a different LCD library, update the import and display calls accordingly.

## Usage

### 1. Plant disease detection

1. Copy or place your trained TensorFlow Lite model at the path referenced in the script (`/home/eg1004/Desktop/leaf_link/model_updated.tflite`). Update the `model_path` argument if you store it elsewhere.
2. Connect the camera and LCD to the Pi.
3. Run the script:

   ```bash
   python3 Plant_Disease_Detection.py
   ```

4. Press `q` in the OpenCV preview window to quit.

The predicted class is displayed on both the LCD and the preview window. Adjust the class labels in the script to match your model outputs if needed.

### 2. Humidity-based irrigation control

1. Wire the DHT11 sensor to GPIO D4 and the pump relay to BCM pin 17.
2. Start the controller:

   ```bash
   python3 HumiditySensor_WaterPump.py
   ```

3. The pump turns on when humidity drops below 60% and off otherwise. Modify the threshold or pins in the script to match your setup.

### 3. Model training notebook

Open `ModelTraining.ipynb` in Jupyter Lab/Notebook to review or adapt the training workflow. Export the trained model to TensorFlow Lite and deploy it to the Pi for inference with the detection script.

## Safety considerations

- Double-check relay wiring before powering the pump.
- Ensure the Pi and pump share a safe common ground and use proper isolation.
- Stop the scripts with `Ctrl+C` when you need to service sensors or hardware.

## License

This project does not currently include a license. Add one if you intend to distribute or open-source your work.

