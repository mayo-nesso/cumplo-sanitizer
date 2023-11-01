import os

import pandas as pd


def get_most_recent_filename(dir: str, prefix: str, extension: str) -> str:
    """
    Get the most recent filename in a directory matching a specified prefix and extension.

    Parameters
    ----------
    dir : str
        The directory in which to search for files.
    prefix : str
        The desired prefix of the file name.
    extension : str
        The desired file extension (e.g., '.txt').

    Returns
    -------
    str
        The full path to the most recent file matching the criteria,
        or None if no matching files are found.

    Description
    -----------
    This function searches the specified directory for files with a
    given prefix and extension.
    It returns the full path to the most recent file that matches
    the criteria, allowing you to easily access or process the most
    recent file in a directory.

    If no matching files are found or if the directory does not exist,
    the function returns None.

    Examples
    --------
    >>> get_most_recent_filename("/path/to/directory", "data_", ".csv")
    '/path/to/directory/data_20231030.csv'
    >>> get_most_recent_filename("/nonexistent_directory", "file_", ".txt")
    'Directory not found: [/nonexistent_directory]'
    """
    # Check if dir exists?
    if not os.path.exists(dir):
        print(f"Directory not found: [{dir}]")
        return None

    file_names = []

    for root, _, files in os.walk(dir):
        for file in files:
            # Filter out files that not match our criteria
            if not file.startswith(prefix):
                continue
            if not file.endswith(extension):
                continue
            file_names.append(file)

    # Check if no core_names were added, which means no matching files were found
    if len(file_names) == 0:
        print(f"No files found in: [{dir}] with prefix [{prefix}] and extension [{extension}]")
        return None

    # Sort the core_names list in reverse order to get the most recent file first
    file_names.sort(reverse=True)
    most_recent = file_names[0]

    # Build the full path to the most recent file
    return os.path.join(root, f"{most_recent}")


def match_group_and_assign(
    df: pd.DataFrame,
    group_pattern: str,
    source_col: str,
    destination_col: str,
    preserve: bool = True,
) -> pd.DataFrame:
    """
    Match a regex group from a source column and assign it to a destination column in a DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame containing the data.
    group_pattern : str
        A regular expression pattern for data extraction. A regex group has to be selected.
    source_col : str
        The name of the source column from which data is extracted.
    destination_col : str
        The name of the destination column to which extracted data is assigned.
    preserve : bool, optional
        If True, preserves existing data in the destination column and only assigns
        values where the destination column is empty (default is True).

    Returns
    -------
    pd.DataFrame
        The DataFrame with the data assigned to the destination column.

    Description
    -----------
    This function extracts data from the specified source column using a regular expression pattern
    and assigns it to the destination column.
    The optional 'preserve' flag ensures that values are only assigned if
    the destination column is empty, which can be helpful to avoid overwriting existing data.
    If pattern not found, NA value will be assigned.

    Examples
    --------
    >>> df = pd.DataFrame({'data_column': ['ABC 123', 'XYZ 456', 'LMN 789']})
    >>> match_group_and_assign(df, r'(\w+) .*', 'data_column', 'result_column')
    >>> print(df)
       data_column result_column
    0     ABC 123           ABC
    1     XYZ 456           XYZ
    2     LMN 789           LMN
    """

    match_groups = df[source_col].str.strip().str.extract(group_pattern)

    # We select the first group!
    mask = match_groups[0].notna()
    if preserve & (destination_col in df.columns):
        mask &= df[destination_col].isna()

    df.loc[mask, destination_col] = match_groups[0]
    return df


def clean_spanish_characters(sp_str: str) -> str:
    """
    Clean and normalize a string containing some Spanish characters.

    Parameters
    ----------
    sp_str : str
        The input string to be cleaned and normalized.

    Returns
    -------
    str
        The cleaned and normalized version of the input string.

    Description
    -----------
    This function takes a string `sp_str` as input and returns a cleaned version of the string.
    It removes leading and trailing whitespace, converts the string to lowercase for consistency,
    and replaces accented characters with their non-accented equivalents commonly used
    in the Spanish language.

    Examples
    --------
    >>> clean_spanish_characters("Café con león")
    'cafe con leon'
    >>> clean_spanish_characters("Álvaro y María")
    'alvaro y maria'
    """
    # Convert `sp_str` to a string to ensure it's treated as a string even if it's not initially.
    sp_str = str(sp_str)

    # Remove leading and trailing white spaces from the string.
    sp_str = sp_str.strip()
    # Convert the entire string to lowercase to ensure consistency in character replacements.
    sp_str = sp_str.lower()
    # Replace accented characters with their non-accented equivalents.
    sp_str = sp_str.replace("á", "a")
    sp_str = sp_str.replace("é", "e")
    sp_str = sp_str.replace("í", "i")
    sp_str = sp_str.replace("ó", "o")
    sp_str = sp_str.replace("ú", "u")
    sp_str = sp_str.replace("ñ", "n")

    return sp_str
