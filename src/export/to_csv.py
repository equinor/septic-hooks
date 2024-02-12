import os
import sys
from pathlib import Path

import openpyxl as xl
import pandas as pd


def export_excel_sheets_to_csv(input_path: Path, output_path: Path, sheets):
    if not output_path.exists():
        os.makedirs(output_path.resolve())
    wb = xl.load_workbook(input_path)
    sheets = wb.sheetnames
    for sheet in sheets:
        output_file = output_path / f"{sheet}.csv"
        pd.read_excel(input_path, sheet_name=sheet).to_csv(
            output_file, sep=";", header=True, index=False
        )


def main():
    file = sys.argv[1]
    input_path = Path(__file__).parent.parent / file
    output_path = Path(__file__).parent.parent / "scg_data"
    try:
        export_excel_sheets_to_csv(input_path, output_path)
    except:
        exit(1)
    exit(0)


if __name__ == "__main__":
    main()
