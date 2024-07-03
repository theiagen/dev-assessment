#!/bin/bash

# {COMMENT}
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <fastq_file>"
    exit 1
fi

FASTQ_FILE=$1

# {COMMENT}
if [ ! -f "$FASTQ_FILE" ]; then
    echo "Error: File '$FASTQ_FILE' not found!"
    exit 1
fi

echo "Processing FASTQ file: $FASTQ_FILE"


# {COMMENT}
LINE_COUNT=$(wc -l < "$FASTQ_FILE")
# {COMMENT}
READ_COUNT=$((LINE_COUNT / 4))

echo "Number of reads in $FASTQ_FILE: $READ_COUNT"
