import re


# This is not necessary because we got the right output but for some best practice for our email we wrote this.


def clean_text(text):
    # Remove HTML tags
    text = re.sub(r"<[^>]*?>", "", text)
    # Remove URLs
    text = re.sub(
        r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",
        "",
        text,
    )
    # Remove special characters
    text = re.sub(r"[^a-zA-Z0-9 ]", "", text)
    # Replace multiple spaces with a single space
    text = re.sub(r"\s{2,}", " ", text)
    # Trim leading and trailing whitespace
    text = text.strip()
    # Remove extra whitespace
    text = " ".join(text.split())
    return text
