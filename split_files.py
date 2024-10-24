import sys
import os
import pandas as pd
from sklearn.model_selection import train_test_split

def process_tsv(input_file):
    # Determine the output directory based on the input file's path
    input_dir = os.path.dirname(input_file)
    wavs_dir = os.path.join(input_dir, "wavs")
    output_file = input_file.replace('.tsv', '_processed.tsv')

    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            # Strip any whitespace and split the line into parts
            parts = line.strip().split('\t')
            if len(parts) == 2:
                file_id = parts[0]
                text = parts[1]
                # Create the new formatted line
                new_line = f"{os.path.join(wavs_dir, f'{file_id}.wav')}|{text}\n"
                outfile.write(new_line)

    print(f"Processed file saved as: {output_file}")

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