def emotion_detector(text_to_analyze):

    if text_to_analyze.strip() == "":
        return None

    text = text_to_analyze.lower()

    emotions = {
        "anger": 0,
        "disgust": 0,
        "fear": 0,
        "joy": 0,
        "sadness": 0
    }

    if "happy" in text:
        emotions["joy"] = 1
    elif "angry" in text:
        emotions["anger"] = 1
    elif "sad" in text:
        emotions["sadness"] = 1
    elif "fear" in text:
        emotions["fear"] = 1
    elif "disgust" in text:
        emotions["disgust"] = 1

    dominant_emotion = max(emotions, key=emotions.get)
    emotions["dominant_emotion"] = dominant_emotion

    return emotions