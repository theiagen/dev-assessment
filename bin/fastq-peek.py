import sys
import os

def main():
    # {COMMENT}
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <fastq_file>")
        sys.exit(1)

    fastq_file = sys.argv[1]

    # {COMMENT}
    if not os.path.isfile(fastq_file):
        print(f"Error: File '{fastq_file}' not found!")
        sys.exit(1)

    print(f"Processing FASTQ file: {fastq_file}")

    # {COMMENT}
    try:
        with open(fastq_file, 'r') as file:
            line_count = sum(1 for line in file)
    except Exception as e:
        print(f"Error reading file '{fastq_file}': {e}")
        sys.exit(1)
        
    # {COMMENT}
    read_count = line_count // 4

    print(f"Number of reads in {fastq_file}: {read_count}")

if __name__ == "__main__":
    main()
