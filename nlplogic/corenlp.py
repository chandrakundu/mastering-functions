from textblob import TextBlob
import wikipedia


def search_wikipedia(search_term):
    """
    Search Wikipedia for a given term
    """
    print(f"Searching Wikipedia for {search_term}")
    return wikipedia.summary(search_term)


def summarize_wikipedia(search_term):
    """
    Summarize a Wikipedia article
    """
    print(f"Summarizing Wikipedia article for {search_term}")
    return wikipedia.summary(search_term)


def get_text_blob(text):
    """
    Get a TextBlob object for a given text
    """
    # print(f"Getting TextBlob object for {text}")
    return TextBlob(text)


def get_phrases(name):
    """Find wikipedia name and return the phrases"""
    text = summarize_wikipedia(name)
    blob = get_text_blob(text)
    phrases = blob.noun_phrases
    return phrases


if __name__ == "__main__":
    print(get_phrases("Golden State Warriors"))
