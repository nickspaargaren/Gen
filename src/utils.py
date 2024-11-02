from pathvalidate import sanitize_filepath
import hashlib


def create_safe_filename(prompt, max_length=50):
    sanitized_prompt = sanitize_filepath(prompt)
    if len(sanitized_prompt) > max_length:
        prompt_hash = hashlib.sha1(prompt.encode()).hexdigest()[:10]
        return f"{sanitized_prompt[:max_length]}_{prompt_hash}"
    return sanitized_prompt
