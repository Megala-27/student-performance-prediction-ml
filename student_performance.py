import customtkinter as ctk
from sklearn.linear_model import LinearRegression
import pandas as pd

# Appearance settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Sample dataset
data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Marks": [35, 40, 50, 55, 60, 65, 70, 80, 85, 95]
}

df = pd.DataFrame(data)

# Train ML model
X = df[["Hours"]]
y = df["Marks"]

model = LinearRegression()
model.fit(X, y)


# Prediction function
def predict_marks():
    try:
        hours = float(hours_entry.get())

        if hours < 0 or hours > 24:
            result_label.configure(
                text="Enter hours between 0 and 24!",
                text_color="#FF6B6B"
            )
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


# Create GUI window
app = ctk.CTk()
app.title("Student Performance Prediction")
app.geometry("600x520")
app.resizable(False, False)

app.configure(fg_color="#15152B")

# Heading
title_label = ctk.CTkLabel(
    app,
    text="🎓 Student Performance Predictor",
    font=("Arial", 25, "bold"),
    text_color="#A78BFA"
)
title_label.pack(pady=(35, 10))

subtitle = ctk.CTkLabel(
    app,
    text="AI & Machine Learning Project",
    font=("Arial", 15),
    text_color="#C4B5FD"
)
subtitle.pack(pady=5)

# Main card
card = ctk.CTkFrame(
    app,
    width=440,
    height=300,
    corner_radius=20,
    fg_color="#242442"
)
card.pack(pady=25, padx=40, fill="x")
card.pack_propagate(False)

# Input label
input_label = ctk.CTkLabel(
    card,
    text="Enter Daily Study Hours",
    font=("Arial", 17, "bold"),
    text_color="white"
)
input_label.pack(pady=(25, 10))

# Input box
hours_entry = ctk.CTkEntry(
    card,
    placeholder_text="Example: 7",
    width=280,
    height=45,
    font=("Arial", 16),
    justify="center",
    corner_radius=12
)
hours_entry.pack(pady=5)

# Predict button
predict_button = ctk.CTkButton(
    card,
    text="🔮 Predict Marks",
    command=predict_marks,
    width=220,
    height=45,
    corner_radius=12,
    font=("Arial", 17, "bold"),
    fg_color="#7C3AED",
    hover_color="#6D28D9"
)
predict_button.pack(pady=15)

# Results
result_label = ctk.CTkLabel(
    card,
    text="Your result will appear here",
    font=("Arial", 19, "bold"),
    text_color="#67E8F9"
)
result_label.pack(pady=5)

message_label = ctk.CTkLabel(
    card,
    text="",
    font=("Arial", 16, "bold")
)
message_label.pack(pady=5)

# Footer
footer = ctk.CTkLabel(
    app,
    text="Powered by Python • Scikit-learn • Linear Regression",
    font=("Arial", 12),
    text_color="#A1A1AA"
)
footer.pack(pady=5)

# Start application
app.mainloop()
