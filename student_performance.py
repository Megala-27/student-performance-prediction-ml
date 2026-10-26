import customtkinter as ctk
from sklearn.linear_model import LinearRegression
import pandas as pd
import math

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# SAMPLE DATASET
data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Marks": [35, 40, 50, 55, 60, 65, 70, 80, 85, 95]
}

df = pd.DataFrame(data)

# TRAIN MACHINE LEARNING MODEL
X = df[["Hours"]]
y = df["Marks"]

model = LinearRegression()
model.fit(X, y)

# PREDICTION FUNCTION
def predict_marks(event=None):
    try:
        value = hours_entry.get().strip()

        if not value:
            result_label.configure(
                text="Please enter study hours!",
                text_color="#FF6B6B"
            )
            message_label.configure(text="")
            return

        hours = float(value)

        if not math.isfinite(hours):
            result_label.configure(
                text="Please enter a valid number!",
                text_color="#FF6B6B"
            )
            message_label.configure(text="")
            return

        if not 0 <= hours <= 24:
            result_label.configure(
                text="Enter hours between 0 and 24!",
                text_color="#FF6B6B"
            )
            message_label.configure(text="")
            return

        prediction = model.predict(
            pd.DataFrame({"Hours": [hours]})
        )[0]

        prediction = max(0, min(100, prediction))

        if prediction >= 80:
            message = "Excellent Performance! 🌟"
            color = "#00E676"

        elif prediction >= 60:
            message = "Good Performance! 👍"
            color = "#FFD54F"

        else:
            message = "Keep Practicing! 💪"
            color = "#FF8A80"

        result_label.configure(
            text=f"Predicted Marks: {prediction:.2f} / 100",
            text_color=color
        )

        message_label.configure(
            text=message,
            text_color=color
        )

    except ValueError:
        result_label.configure(
            text="Please enter a valid number!",
            text_color="#FF6B6B"
        )
        message_label.configure(text="")

    except Exception:
        result_label.configure(
            text="Something went wrong!",
            text_color="#FF6B6B"
        )
        message_label.configure(text="")


# CLEAR FUNCTION
def clear_fields():
    hours_entry.delete(0, "end")

    result_label.configure(
        text="Your result will appear here",
        text_color="#67E8F9"
    )

    message_label.configure(text="")
    hours_entry.focus()


# MAIN APPLICATION
app = ctk.CTk()

app.title("Student Performance Prediction")

try:
    app.state("zoomed")
except Exception:
    app.geometry("1100x750")

app.resizable(True, True)
app.configure(fg_color="#15152B")

# MAIN CONTAINER
main_frame = ctk.CTkFrame(
    app,
    fg_color="transparent"
)

main_frame.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=20
)

# HEADING
title_label = ctk.CTkLabel(
    main_frame,
    text="🎓 Student Performance Predictor",
    font=("Arial", 30, "bold"),
    text_color="#A78BFA"
)

title_label.pack(pady=(35, 10))

# SUBTITLE
subtitle = ctk.CTkLabel(
    main_frame,
    text="AI & Machine Learning Project",
    font=("Arial", 18),
    text_color="#C4B5FD"
)

subtitle.pack(pady=5)

# MAIN CARD
card = ctk.CTkFrame(
    main_frame,
    width=500,
    height=390,
    corner_radius=25,
    fg_color="#242442"
)

card.pack(pady=30, padx=20)
card.pack_propagate(False)

# INPUT LABEL
input_label = ctk.CTkLabel(
    card,
    text="Enter Daily Study Hours",
    font=("Arial", 20, "bold"),
    text_color="white"
)

input_label.pack(pady=(30, 12))

# INPUT BOX
hours_entry = ctk.CTkEntry(
    card,
    placeholder_text="Example: 7",
    width=320,
    height=50,
    font=("Arial", 18),
    justify="center",
    corner_radius=12
)

hours_entry.pack(pady=8)
hours_entry.bind("<Return>", predict_marks)

# PREDICT BUTTON
predict_button = ctk.CTkButton(
    card,
    text="🔮 Predict Marks",
    command=predict_marks,
    width=250,
    height=50,
    corner_radius=12,
    font=("Arial", 18, "bold"),
    fg_color="#7C3AED",
    hover_color="#6D28D9"
)

predict_button.pack(pady=(20, 12))

# CLEAR BUTTON
clear_button = ctk.CTkButton(
    card,
    text="Clear",
    command=clear_fields,
    width=160,
    height=38,
    corner_radius=10,
    font=("Arial", 15),
    fg_color="#444466",
    hover_color="#555577"
)

clear_button.pack(pady=5)

# RESULT LABEL
result_label = ctk.CTkLabel(
    card,
    text="Your result will appear here",
    font=("Arial", 20, "bold"),
    text_color="#67E8F9"
)

result_label.pack(pady=(15, 5))

# MESSAGE LABEL
message_label = ctk.CTkLabel(
    card,
    text="",
    font=("Arial", 17, "bold")
)

message_label.pack(pady=5)

# FOOTER
footer = ctk.CTkLabel(
    main_frame,
    text="Powered by Python • Scikit-learn • Linear Regression",
    font=("Arial", 13),
    text_color="#A1A1AA"
)

footer.pack(pady=10)

# EXIT FULLSCREEN FUNCTION
def exit_fullscreen(event=None):
    app.attributes("-fullscreen", False)
    app.state("normal")
    app.geometry("1000x750")

app.bind("<Escape>", exit_fullscreen)

hours_entry.focus()

app.mainloop()

