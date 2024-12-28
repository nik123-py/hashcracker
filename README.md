

This Python-based Hash Cracker tool is designed for ethical hacking and penetration testing. It attempts to crack hashed passwords by comparing them against a list of potential plaintext passwords.

## Features
- Supports **MD5**, **SHA1**, and **SHA256** hashing algorithms.
- Loads custom wordlists from a file.
- Provides progress updates during cracking.
- Reports execution time and attempt counts.
- Handles common errors gracefully.

## Prerequisites
- Python 3.x installed on your system.
- A wordlist file for testing (e.g., `wordlist_file.txt`).

## Installation
1. Clone or download this repository.
2. Ensure Python 3.x is installed by running:
   ```bash
   python --version
   ```
3. (Optional) Install any required dependencies, though the script uses Python's built-in libraries.

## Usage
1. Run the script:
   ```bash
   python hash_cracker.py
   ```

2. Provide the following inputs when prompted:
   - **Hash to crack**: The hash you want to crack.
   - **Hash type**: Choose one of the supported algorithms (`md5`, `sha1`, or `sha256`).
   - **Wordlist file**: Path to your wordlist file. Press Enter to use the default built-in wordlist.

3. The script will attempt to crack the hash by iterating through the wordlist.

## Example
### Input:
```plaintext
Enter the hash to crack: 5f4dcc3b5aa765d61d8327deb882cf99
Enter the hash type (md5, sha1, sha256): md5
Enter the path to the wordlist file (or press Enter to use default):
```

### Output:
```plaintext
[INFO] Starting hash cracking for 5f4dcc3b5aa765d61d8327deb882cf99 using md5...
[SUCCESS] Password found: 'password' in 0.01 seconds after 1 attempts.
```

## Wordlist
The script can use a custom wordlist file or a default list of common passwords for testing.

### Custom Wordlist
To use a custom wordlist, provide the file path when prompted. The wordlist should be a plain text file with one password per line.

### Built-in Wordlist
The script includes a small default wordlist with commonly used passwords like:
- `password`
- `123456`
- `qwerty`
- `abc123`

## Limitations
- This tool is for educational and ethical purposes only. Ensure you have explicit permission before testing any system.
- Cracking efficiency depends on the size of the wordlist and the complexity of the hash.

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests to improve the tool.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Disclaimer
This tool is intended for ethical use only. Unauthorized use is strictly prohibited and may violate laws or regulations.
