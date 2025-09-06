import io
import csv
import json

def save_to_csv(posts: dict) -> io.StringIO:
    """Save posts to CSV (for download in Streamlit)."""
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Platform", "Post"])
    for platform, post in posts.items():
        writer.writerow([platform, post])
    return io.StringIO(output.getvalue())

def save_to_json(posts: dict) -> io.StringIO:
    """Save posts to JSON (for download in Streamlit)."""
    output = io.StringIO()
    json.dump(posts, output, indent=4)
    return io.StringIO(output.getvalue())
