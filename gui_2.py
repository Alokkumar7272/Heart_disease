import tkinter as tk
from tkinter import messagebox
import pickle

# Load the trained heart disease prediction model
model = pickle.load(open(r'C:\Users\Alok Kumar\OneDrive\Desktop\Heart Disease\random_forest.pkl', "rb"))

# Function to handle button click event and make prediction
def predict():
    # Get input values from textboxes
    age = int(age_entry.get())
    sex = int(sex_var.get())
    cp = int(cp_var.get())
    trestbps = int(trestbps_entry.get())
    chol = int(chol_entry.get())
    fbs = int(fbs_var.get())
    restecg = int(restecg_var.get())
    thalach = int(thalach_entry.get())
    exang = int(exang_var.get())
    oldpeak = float(oldpeak_entry.get())
    slope = int(slope_var.get())
    ca = int(ca_entry.get())
    thal = int(thal_var.get())

    # Prepare input data for prediction
    input_data = [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]

    # Make prediction
    prediction = model.predict(input_data)

    # Show prediction result in a message box
    if prediction[0] == 0:
        messagebox.showinfo("Prediction Result", "No heart disease detected.")
    else:
        messagebox.showinfo("Prediction Result", "Heart disease detected.")

# Create main window
root = tk.Tk()
root.title("Heart Disease Prediction")

# Create input labels
age_label = tk.Label(root, text="Age:")
age_label.grid(row=0, column=0, sticky="e")
sex_label = tk.Label(root, text="Sex:")
sex_label.grid(row=1, column=0, sticky="e")
# Add more labels for other input features

# Create input textboxes
age_entry = tk.Entry(root)
age_entry.grid(row=0, column=1)
sex_var = tk.IntVar()
sex_entry = tk.Radiobutton(root, text="Male", variable=sex_var, value=1)
sex_entry.grid(row=1, column=1)
sex_entry = tk.Radiobutton(root, text="Female", variable=sex_var, value=0)
sex_entry.grid(row=1, column=2)
# Add more textboxes and input components for other input features

# Create prediction button
predict_button = tk.Button(root, text="Predict", command=predict)
predict_button.grid(row=13, columnspan=2)

# Start the main event loop
root.mainloop()
