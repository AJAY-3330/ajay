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


if __name__ == '__main__':
    while True:
        text: str = input('Text (or type "exit" to quit): ').strip()

        if text.lower() == 'exit':
            print("Exiting program.")
            break

        # Get the mood based on the input text
        mood: Mood = get_Mood(text, threshold=0.3)

        # Print the result
        print(f'{mood.emoji} ({mood.sentiment:.2f})')