
# Text Encryption and Decryption Tool

This Python tool provides a simple way to encrypt and decrypt text using a randomized substitution cipher. 
It features a user-friendly interface with colorful prompts powered by `Colorama`.

## Features

- Encrypt text with a randomized substitution cipher.
- Decrypt encrypted text back to its original form.
- Easy-to-use interface with colorful outputs for better user experience.
- Includes error handling for unsupported characters.

## Requirements

- Python 3.6 or higher
- `colorama` library (for colorful console outputs)

## Installation

1. Clone this repository or download the script.
2. Install the required library:
   ```bash
   pip install colorama
   ```

## Usage

1. Run the script:
   ```bash
   python script_name.py
   ```
2. Follow the prompts to:
   - Encrypt text.
   - Decrypt encrypted text.
   - Exit the program.

## Example

### Encryption
Input:
```
Hello, World!
```
Output:
```
%1@lz:xH!@#b+
```

### Decryption
Input:
```
%1@lz:xH!@#b+
```
Output:
```
Hello, World!
```

## Notes

- The encryption process uses a shuffled mapping of characters, ensuring unique results.
- Characters not supported by the script are left unchanged during encryption or decryption.

## License

This project is licensed under the MIT License.
