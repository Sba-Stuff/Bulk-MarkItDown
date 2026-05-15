# Bulk MarkItDown Converter

A simple Python script designed to convert documents (including Markdown) into plain text or Markdown format using the powerful [Markitdown](https://github.com/microsoft/markitdown) library from Microsoft.

## 🚀 Features
- **Universal Input/Output**: Supports `.pdf`, `.docx`, `.pptx`, `.xlsx`, `.xls`, `.html`, `.htm`, `.csv`, `.json`, `.xml`, and standard file types.
- **Flexible Output Formats**: Converts input to either `Markdown` (`.md`) or plain `Text` (`txt`).
- **Interactive Input**: Automatically detects the most useful format for your current project.
- **Detailed Logging**: Real-time status updates during conversion, including file names, sizes, and error messages.

## Screenshot
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/204f0ee3-11c6-4d8a-b05a-d2a3e819303c" />


## 🛠️ Technology Stack
- Python 3.x (tested on python 3.11 and 3.12)
- MarkItDown library (Python)
- Standard libraries (`argparse`, `pathlib`)
- UTF-8 encoding support for rich text handling.

## ⚙️ Installation

Best Way To Run It.
1. Create an environment using python. Either use my Python [Environment Manager](https://github.com/Sba-Stuff/Powershell-Python-GUI-Environment-Creator) to create and run environments quickly and easily on windows.
2. Download mark it down library. Download mark it down library using:
```
pip install markitdown[all]
```
As we need all types of file conversions, that is why we need all in your environment.

3. Place all files that you need to convert in input folder. Sample files are added as an example.
4. Run python code.
5. Markdown text converted files will be added in output folder the output created by library is also present as an example.
6. Please use project wisely.

## License:
MIT. I don't know what MIT is, If Microsoft have not any problems using their library, i don't have too.
