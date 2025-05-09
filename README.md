🍎 Fruit Ripeness Detection
This project is a Fruit Ripeness Detection that uses TensorFlow, Tkinter,Google Collab and SQLite to predict whether a fruit (e.g., Banana, Strawberry, Papaya, Guava) is Ripe, Unripe and Rotten based on an uploaded image.

📌 Features
✔ Graphical User Interface (GUI) to upload an image and get a prediction.
✔ Trained CNN Model (best_model.keras) to classify fruit ripeness.
✔ labeled .txt file (fruit_labels.txt)
✔ SQLite Database for user authentication (Login System).

📌 Project Requirements
✅ System Requirements
Operating System: Windows 10/11
Python Version: 3.10 (TensorFlow does not support Python 3.11)
PIP Version: Latest (upgrade required)

📌 Installation Guide (From Scratch)

🔹 Step 1: Install Python 3.10
Download Python 3.10 from Python Official Site
During installation, check: ✅ Add Python to PATH
Verify Python installation:
❗ Run this command:
python --version

Upgrade pip:
❗ Run this command:
python -m pip install --upgrade pip

🔹 Step 2: Clone the Repository
If Git is installed, clone the project from GitHub:
❗ Run this command:
git clone https://github.com/RidaShahid287/FruitRipenessApp
cd FruitRipenessApp
If Git is NOT installed, download the project manually from GitHub.

🔹 Step 3: Create & Activate a Virtual Environment
Create a virtual environment:
❗ Run this command:
python -m venv fruit_env

Activate the virtual environment:
Windows:
❗ Run this command:
fruit_env\Scripts\activate

Mac/Linux:
❗ Run this command:
source fruit_env/bin/activate

🔹 Step 4: Install Required Dependencies
Run the following command to install TensorFlow, Tkinter, and other required packages:
❗ Run this command:
pip install -r requirements.txt


🔹 Step 5: Place Pretrained Model and Labels (If Downloaded via Colab)
If you have downloaded the pretrained model from the Google Colab notebook:
- Copy `best_model.keras` and `fruit_labels.txt` into the `models/` directory.

These files are generated during model training and can also be downloaded from Colab and manually placed here for the application to work correctly.


🔹 Step 6: Setting Up the Database
Ensure SQLite is installed (comes pre-installed with Python).
Create the SQLite database:
❗ Run this command:
python main.py
(This will generate fruit_classifier.db in the project folder.)
View the database using DB Browser for SQLite:
Download DB Browser for SQLite here
Open fruit_classifier.db to see the users' table.

🔹 Step 7: Run the GUI Application
To start the application:
❗ Run this command:
python main.py
This will launch a GUI where you can upload an image to classify it as Ripe, Unripe or Rotten.

🔹 Project Structure
FruitRipenessApp/
├── __pycache__/               # Compiled Python files
├── .git/                      # Git repository metadata
├── database/                  # Database-related files
├── dataset/                   # Dataset for training and testing
├── fruit_env/                 # Virtual environment (should be excluded from Git)
├── images/                    # Folder for storing fruit images
├── models/                    # Machine learning models
│   ├── best_model.keras       # Trained model file
│   └── fruit_labels.txt       # labeld file
├── .gitattributes             # Git LFS attributes (if any)
├── .gitignore                 # Git ignore file to exclude unnecessary files
├── all-files.txt              # List of all repository files
├── classify.py                # Script to classify fruit images
├── fruit_classifier.db        # Database file
├── main.py                    # Main entry point for the application
├── preprocess.py              # Preprocessing script for dataset
├── README.md                  # Project documentation
├── requirements.txt           # Dependencies and packages needed
└── notebook                   # Google Collab notebok for model train and agorithm

🔹 Dataset Images Link:
https://www.kaggle.com/datasets/dudinurdiyansah/fruit-ripeness-classifier

📌 Technologies Used
Python 3.10
TensorFlow (Deep Learning Model)
Keras (CNN Model)
Pillow (Image Processing)
Tkinter (GUI)
SQLite (Database for user login)

HAPPY CODING!!!
