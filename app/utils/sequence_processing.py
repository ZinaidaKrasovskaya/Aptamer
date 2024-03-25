import pandas as pd
import re

INVALID_DATA = dict()


def create_table(input_table: pd.DataFrame, sequence_column: str) -> pd.DataFrame:
    aptamer_sequence_column = {sequence_column: []}
    valid_sequences = []
    invalid_sequences = []

    for index, row in input_table[sequence_column].items():
        if type(row) != str:
            continue

        remove_non_letter(row)

        if is_invalid_sequence(row):
            invalid_sequences.append(row)
        else:
            valid_sequences.append(row)

    INVALID_DATA[sequence_column] = invalid_sequences
    aptamer_sequence_column[sequence_column] = valid_sequences
    clean_table = pd.DataFrame.from_dict(aptamer_sequence_column)
    return clean_table


def remove_non_letter(sequence) -> str:
    return re.sub("[^a-zA-Z]", '', sequence)


def is_invalid_sequence(sequence: str) -> str:
    valid_nucleotides = ["A", "T", "G", "C", "U"]
    for nucleotide in sequence:
        if nucleotide not in valid_nucleotides:
            return True
