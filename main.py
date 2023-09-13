import os
import gensim
from gensim.summarization import summarize

def load_medical_records(file_path):
    """Load medical records from a text file."""
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            records = file.read().split('\n\n')
        return records
    else:
        print(f"File not found: {file_path}")
        return []

def summarize_medical_records(records):
    """Summarize medical records using Gensim."""
    summaries = []
    for record in records:
        summary = summarize(record)
        summaries.append(summary)
    return summaries

def main():
    file_path = "sample_records.txt"
    records = load_medical_records(file_path)

    if not records:
        return

    summaries = summarize_medical_records(records)

    for i, summary in enumerate(summaries, start=1):
        print(f"Summary for Medical Record {i}:\n{summary}\n")

if __name__ == "__main__":
    main()
