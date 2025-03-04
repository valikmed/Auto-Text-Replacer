# Auto Text Replacer

A Python script that replaces typed words with their corresponding values from a text file.

## Features

* Replaces typed words with their corresponding values from a text file
* Supports multiple values for each word
* Ignores case when matching words
* Can be used with any text editor or application

## Requirements

* Python 3.11.9
* `keyboard` library
* `pyperclip` library

## Installation

1. Install the required libraries by running `pip install keyboard pyperclip`
2. Clone this repository or download the script
3. Create a text file named `data.txt` in the same directory as the script
4. Add your word-value pairs to the `data.txt` file, one pair per line, separated by an equals sign (=)

## Usage

1. Run the script by executing `python auto_text_replacer.py`
2. Type a word that you want to replace, followed by a space
3. The script will replace the word with its corresponding value from the `data.txt` file

## Example

Suppose you have the following word-value pairs in your `data.txt` file:

If you type `hello` followed by a space, the script will replace it with `Hi there!`.

## Troubleshooting

* Make sure you have the correct file path to the `data.txt` file
* Check that the word-value pairs are formatted correctly in the `data.txt` file
* If you encounter any issues, try running the script in debug mode by executing `python auto_text_replacer.py -d`

## Run It on Startup (Windows)

To run the script automatically on startup, follow these steps:

1. Press Win + R, type `shell:startup`, and hit Enter.
2. Copy the `clipboard_listener.py` file into this folder.
3. Now, every time you start your laptop, it will run automatically.
## Contributing

Contributions are welcome! If you have any ideas for new features or improvements, please submit a pull request or open an issue.

## License

This script is released under the MIT License.
