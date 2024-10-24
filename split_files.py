import sys
import os
import pandas as pd
from sklearn.model_selection import train_test_split

def process_tsv(input_file):
    # Determine the output directory based on the input file's path
    input_dir = os.path.dirname(input_file)
    wavs_dir = os.path.join(input_dir, "wavs")
    output_file = input_file.replace('.tsv', '_processed.tsv')

    # Read the TSV file and process it
    lines = []
    with open(input_file, 'r', encoding='utf-8') as infile:
        for line in infile:
            parts = line.strip().split('\t')
            if len(parts) == 2:
                file_id = parts[0]
                text = parts[1]
                new_line = f"{os.path.join(wavs_dir, f'{file_id}.wav')}|{text}\n"
                lines.append(new_line)

    # Convert to DataFrame for easier manipulation
    df = pd.DataFrame(lines, columns=['data'])

    # Split into train (80%) and temp (20%)
    train_data, temp_data = train_test_split(df, train_size=0.8, random_state=42)

    # Further split temp_data into test (10%) and validation (10%)
    test_data, val_data = train_test_split(temp_data, test_size=0.5, random_state=42)

    # Write the datasets to separate files
    write_dataset(os.path.join(input_dir, "train.tsv"), train_data['data'].tolist())
    write_dataset(os.path.join(input_dir, "test.tsv"), test_data['data'].tolist())
    write_dataset(os.path.join(input_dir, "val.tsv"), val_data['data'].tolist())

    print(f"Processed files saved as: train.tsv, test.tsv, val.tsv in {input_dir}")

def write_dataset(file_path, dataset):
    with open(file_path, 'w', encoding='utf-8') as outfile:
        outfile.writelines(dataset)

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_tsv_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    if not os.path.isfile(input_file):
        print(f"Error: The file {input_file} does not exist.")
        sys.exit(1)

    process_tsv(input_file)

if __name__ == "__main__":
    main()
