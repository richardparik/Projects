from tkinter import *
from tkinter import filedialog
import customtkinter
from PIL import Image, ImageTk
import webbrowser
import os, sys
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array


# Function to preprocess the image and make predictions
def preprocess_and_predict(img_path):
    try:
        # Load and preprocess the image
        print(f"Loading image from: {img_path}")
        img = Image.open(img_path).convert("RGB").resize((224, 224))  # Convert to RGB and resize
        print("Image successfully loaded and resized to (224, 224).")

        img_array = img_to_array(img) / 255.0  # Normalize pixel values
        print("Image converted to array and normalized (values scaled between 0 and 1).")

        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
        print(f"Image array shape after adding batch dimension: {img_array.shape}")

        # Make prediction using the model
        print("Making predictions...")
        predictions = model.predict(img_array, verbose=0)
        print(f"Raw predictions from the model: {predictions}")

        # Extract the predicted class and its certainty
        predicted_class = np.argmax(predictions) + 1  # Find the index of the highest probability (+1 because classes start at 1)
        certainty = predictions[0][predicted_class - 1] * 100  # Get certainty in percentage
        predicted_label = label_map[str(predicted_class)]
        print(f"Prediction: {predicted_label}, Certainty: {certainty:.2f}%")

        return predicted_label, certainty

    except FileNotFoundError:
        print("Error: The image file was not found. Please check the file path and try again.")
        return "Error: File Not Found", 0

    except AttributeError as e:
        print(f"Error: There was a problem with the file. It might not be a valid image file. {str(e)}")
        return "Error: Invalid File", 0

    except ValueError as e:
        print(f"Error: The image might not be compatible with the model. {str(e)}")
        return "Error: Incompatible Image", 0

    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        return "Error: Unexpected Issue", 0

# Function to open a file dialog for selecting an image
def choose_file():
    global selected_file, img_thumbnail
    selected_file = filedialog.askopenfilename(title="Select an Image File", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if selected_file:
        # Display the selected file as a miniature (thumbnail)
        img = Image.open(selected_file).convert("RGB").resize((150, 150))
        img_thumbnail = ImageTk.PhotoImage(img)
        thumbnail_label.configure(image=img_thumbnail)
        file_label.configure(text=f"Selected File: {selected_file}")  # Display the file path

# Function to evaluate the selected image
def evaluate_image():
    if selected_file:
        print(f"File selected for evaluation: {selected_file}")
        predicted_label, certainty = preprocess_and_predict(selected_file)
        print(f"Prediction: {predicted_label}, Certainty: {certainty}")
        result_label.configure(text=f"Predicted Label: {predicted_label} ({certainty:.2f}% certainty)", text_color="white")
    else:
        result_label.configure(text="No file selected! Please choose a file first.", text_color="red")

# Resource path function for packaging
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Label mapping for predictions
label_map = {
    '1': 'Meningioma',
    '2': 'Glioma',
    '3': 'Pituitary'
}

# Load the pre-trained model
model_path = resource_path("brain_tumor_model_final.keras")
model = load_model(model_path)
print("Model loaded successfully")

# Main window
window = customtkinter.CTk()
window.minsize(700, 500)
window.resizable(False, False)
window.title("Brain Tumor App")
icon_path = resource_path("icon_brain.ico")
window.iconbitmap(icon_path)
window.config(bg="#5b5b5b")
my_font = customtkinter.CTkFont(family="Cambria", size=16, weight="bold")
customtkinter.set_appearance_mode("Dark")

# Canvas
canvas = customtkinter.CTkCanvas(window, width=470, height=220, bg="#d3d3d3")
canvas.pack(pady=(10, 0))
brain_img = Image.open(resource_path("canvas_brain.png"))
canvas.image = ImageTk.PhotoImage(Image.open(resource_path("canvas_brain.png")))
canvas.create_image(0, 0, anchor="nw", image=canvas.image)

# Frame
GPS_frame = customtkinter.CTkFrame(window, fg_color="#5b5b5b")
GPS_frame.pack(pady=10)

# Buttons for links
github_icon = customtkinter.CTkImage(Image.open(resource_path("icon_github.png")))
colab_icon = customtkinter.CTkImage(Image.open(resource_path("icon_colab.png")))
slides_icon = customtkinter.CTkImage(Image.open(resource_path("icon_slides.png")))
kaggle_icon = customtkinter.CTkImage(Image.open(resource_path("icon_kaggle.png")))

github_button = customtkinter.CTkButton(
    GPS_frame, text=" GitHub repository",
    image=github_icon,
    fg_color="#5b5b5b", border_spacing=3, corner_radius=8, border_color="black",
    hover_color="#707070", font=my_font, text_color="white",
    command=lambda: webbrowser.open("https://github.com/richardparik/Projects/tree/master/FINAL%20project")
)
github_button.pack(pady=5)

colab_button = customtkinter.CTkButton(
    GPS_frame, text=" Colab notebook",
    image=colab_icon,
    fg_color="#5b5b5b", border_spacing=3, corner_radius=8, border_color="black",
    hover_color="#707070", font=my_font, text_color="white",
    command=lambda: webbrowser.open("https://colab.research.google.com/github/richardparik/Projects/blob/master/FINAL%20project/Final_project.ipynb")
)
colab_button.pack(pady=5)

final_pres_button = customtkinter.CTkButton(
    GPS_frame, text=" Final presentation",
    image=slides_icon,
    fg_color="#5b5b5b", border_spacing=3, corner_radius=8, border_color="black",
    hover_color="#707070", font=my_font, text_color="white",
    command=lambda: webbrowser.open("https://docs.google.com/presentation/d/1mnFfKyp6MdNfgLgWNUqYdjkljmHksM0cNtp4gPG4Wws/edit?slide=id.p#slide=id.p")
)
final_pres_button.pack(pady=5)

kaggle_button = customtkinter.CTkButton(
    GPS_frame, text=" Kaggle dataset",
    image=kaggle_icon,
    fg_color="#5b5b5b", border_spacing=3, corner_radius=8, border_color="black",
    hover_color="#707070", font=my_font, text_color="white",
    command=lambda: webbrowser.open("https://www.kaggle.com/datasets/denizkavi1/brain-tumor")
)
kaggle_button.pack(pady=5)

# File selection label
file_label = customtkinter.CTkLabel(window, text="No file selected.", font=my_font)
file_label.pack(pady=10)

# Thumbnail display
thumbnail_label = Label(window, bg="#5b5b5b")
thumbnail_label.pack(pady=10)

# Buttons for file selection and evaluation
choose_file_button = customtkinter.CTkButton(
    window, text="Choose File",
    fg_color="#5b5b5b", border_spacing=3, corner_radius=8, border_color="black",
    hover_color="#707070", font=my_font, text_color="white",
    command=choose_file
)
choose_file_button.pack(pady=10)

run_button = customtkinter.CTkButton(
    window, text="Run",
    fg_color="#5b5b5b", border_spacing=3, corner_radius=8, border_color="black",
    hover_color="#707070", font=my_font, text_color="white",
    command=evaluate_image
)
run_button.pack(pady=10)

# Result label
result_label = customtkinter.CTkLabel(window, text="", font=my_font)
result_label.pack(pady=20)

# Main program
selected_file = None  # Global variable to store the selected file path
img_thumbnail = None  # Global variable to store the thumbnail image
window.mainloop()
