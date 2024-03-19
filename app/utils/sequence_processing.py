import re
import pandas as pd


def clean_symbols(sequence: str) -> str:
    """
    Функция для очистки последовательности от сторонних символов
    :param: sequence: аминокислотная последовательность

    :return: последовательность, содержащая лишь алфавитные символы
    """
    return re.sub(r'[^a-zA-Z]', '', sequence)


def validate_nucleotides(sequence: str) -> bool:
    """
    Функция для валидации последовательности
    :param: sequence: аминокислотная последовательность

    :return: результат сравнения набора нуклеотидов в последовательности
        с набором A, T, G, C, U
    """
    return set(sequence) == set('AUTGC')


def validate_sequence(df: pd.DataFrame, seq_column: str) -> pd.DataFrame:
    """
    Функция для обработки последовательностей в таблице с данными
    :param: df: таблица с данными
    :param: seq_column: название колонки последовательности в таблице

    :return: таблица с очищенной колонкой последовательности
    """
    df[seq_column] = df[seq_column].apply(clean_symbols)
    df['incorrect_sequence'] = df[seq_column].apply(validate_nucleotides)
    return df
