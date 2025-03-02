import re


STOP_WORDS = {
    "a", "an", "the", "and", "or", "but", "if", "while", "is", "am", "are",
    "was", "were", "be", "been", "being", "of", "to", "in", "that", "it",
    "for", "on", "with", "as", "at", "by", "from", "this", "these", "those",
    "i", "you", "he", "she", "they", "we", "my", "your", "his", "her", "their"
}

def preprocess_text(text):
    
    text = text.lower()
    text = re.sub(r'[^\w\s%]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    tokens = text.split()
    filtered_tokens = [token for token in tokens if token not in STOP_WORDS]
    processed_text = ' '.join(filtered_tokens)
    return processed_text

