#!/usr/bin/env python3

import argparse
from pathlib import Path
from markitdown import MarkItDown


# Extensions commonly supported by MarkItDown
SUPPORTED_EXTENSIONS = {
    ".pdf",
    ".docx",
    ".pptx",
    ".xlsx",
    ".xls",
    ".html",
    ".htm",
    ".csv",
    ".json",
    ".xml",
    ".txt",
    ".md",
}


def convert_files(input_folder: str, output_folder: str, output_format: str = "md"):
    input_path = Path(input_folder)
    output_path = Path(output_folder)

    if not input_path.exists():
        raise FileNotFoundError(f"Input folder does not exist: {input_folder}")

    output_path.mkdir(parents=True, exist_ok=True)

    # Get all supported files
    files = [
        f for f in input_path.iterdir()
        if f.is_file() and f.suffix.lower() in SUPPORTED_EXTENSIONS
    ]

    total_files = len(files)

    if total_files == 0:
        print("No supported files found.")
        return

    md = MarkItDown(enable_plugins=False)

    converted_count = 0
    failed_count = 0

    for index, file in enumerate(files, start=1):
        try:
            print(f"[{index}/{total_files}] Converting: {file.name}")

            result = md.convert(str(file))
            text_content = result.text_content

            output_file = output_path / f"{file.stem}.{output_format}"

            with open(output_file, "w", encoding="utf-8") as f:
                f.write(text_content)

            converted_count += 1

            print(f"Saved: {output_file.name}")

        except Exception as e:
            failed_count += 1
            print(f"Failed to convert {file.name}: {e}")

    # Count actual output files created
    output_files = list(output_path.glob(f"*.{output_format}"))
    output_count = len(output_files)

    print("\n========== Conversion Summary ==========")
    print(f"Input files found      : {total_files}")
    print(f"Successfully converted : {converted_count}")
    print(f"Output files created   : {output_count}")
    print(f"Failed conversions     : {failed_count}")
    print(f"Conversion rate        : {converted_count}/{total_files}")
    print("========================================")


def main():
    parser = argparse.ArgumentParser(
        description="Convert files in a folder to Markdown or TXT using MarkItDown."
    )

    parser.add_argument(
        "input_folder",
        nargs="?",
        help="Path to folder containing files"
    )

    parser.add_argument(
        "output_folder",
        nargs="?",
        help="Path to folder where converted files will be saved"
    )

    parser.add_argument(
        "--format",
        choices=["md", "txt"],
        default="md",
        help="Output format (default: md)"
    )

    args = parser.parse_args()

    input_folder = args.input_folder
    output_folder = args.output_folder

    # Ask interactively if not provided
    if not input_folder:
        input_folder = input("Enter Input folder path: ").strip()

    if not output_folder:
        output_folder = input("Enter Output folder path: ").strip()

    convert_files(
        input_folder,
        output_folder,
        args.format
    )


if __name__ == "__main__":
    main()