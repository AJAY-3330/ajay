import tkinter as tk
from textblob import TextBlob
from dataclasses import dataclass

@dataclass
class Mood:
    emoji: str
    sentiment: float


def get_Mood(input_text: str, *, threshold: float) -> Mood:
    # Get sentiment polarity using TextBlob
    sentiment: float = TextBlob(input_text).sentiment.polarity
    
    # Set friendly and hostile thresholds
    friendly_threshold: float = threshold
    hostile_threshold: float = -threshold

    # Return Mood based on sentiment
    if sentiment >= friendly_threshold:
        return Mood('😊', sentiment)  # Friendly mood
    elif sentiment <= hostile_threshold:
        return Mood('😡', sentiment)  # Hostile mood
    else:
        return Mood('😐', sentiment)  # Neutral mood


def on_analyze_click():
    # Get text input from the user
    input_text = text_entry.get().strip()

    if input_text.lower() == 'exit':
        root.quit()  # Exit the program

    # Get the mood based on the input text
    mood = get_Mood(input_text, threshold=0.3)

    # Update the result label with the emoji and sentiment score
    result_label.config(text=f'{mood.emoji} ({mood.sentiment:.2f})')


# Setting up the Tkinter window
root = tk.Tk()
root.title("Mood Analyzer")

# Create a label and entry widget for user input
text_entry_label = tk.Label(root, text="Enter Text:")
text_entry_label.pack(pady=30)

text_entry = tk.Entry(root, width=40)
text_entry.pack(pady=30)

# Create a button to trigger the analysis
analyze_button = tk.Button(root, text="Analyze Mood", command=on_analyze_click)
analyze_button.pack(pady=30)

# Create a label to display the result (emoji and sentiment score)
result_label = tk.Label(root, text="", font=('Arial', 44))
result_label.pack(pady=30)

# Start the Tkinter event loop
root.mainloop()
