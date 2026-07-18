from EmotionDetection import emotion_detector

def test_emotion_detection():
    test_cases = {
        "I am glad this happened": "joy",
        "I am really mad about this": "anger",
        "I feel disgusted just hearing about this": "disgust",
        "I am so sad about this": "sadness",
        "I am really afraid that this will happen": "fear"
    }

    for text, expected in test_cases.items():
        result = emotion_detector(text)
        actual = result["dominant_emotion"]

        if actual == expected:
            print(f"PASS: '{text}' -> {actual}")
        else:
            print(f"FAIL: '{text}' -> Expected {expected}, Got {actual}")

if __name__ == "__main__":
    test_emotion_detection()