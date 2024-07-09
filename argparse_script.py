import argparse
import pandas as pd

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Process CSV files containing economic data.')
    parser.add_argument('file_paths', metavar='F', type=str, nargs='+',
                        help='paths to the CSV files')

    # Parse arguments
    args = parser.parse_args()
    
    # Process each CSV file
    for file_path in args.file_paths:
        try:
            # Read the CSV file
            data = pd.read_csv(file_path)
            
            # Print the first few rows of the dataframe
            print(f"Data from {file_path}:")
            print(data.head())
            print("\n")
            
        except Exception as e:
            print(f"Error processing file {file_path}: {e}")

if __name__ == '__main__':
    main()
