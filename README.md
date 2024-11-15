## **PARAKRAM: A Powerful Directory Buster Tool**
![PARAKRAM](https://github.com/user-attachments/assets/b6c295e9-d570-4499-8daf-e28a9187d06b)

Welcome to **PARAKRAM**, an advanced and efficient **Directory Buster** tool designed to streamline web URL directory busting. This tool is capable of detecting page extensions (such as `.html`, `.jsp`, `.php`) and automatically appending those extensions to each wordlist entry when the `--auto-extension` flag is enabled.

PARAKRAM’s aim is to make directory busting faster, smarter, and more user-friendly. If you're looking for a tool to perform web application security testing, **PARAKRAM** is here to assist you in uncovering hidden directories with ease.

## **Features**

- **Automatic Extension Detection**: Automatically detects page extensions like `.html`, `.jsp`, and `.php` and appends them to each wordlist entry during scans if the `--auto-extension` flag is enabled.
- **Efficiency**: Optimized for fast directory busting with flexible configuration.
- **User-Friendly**: Simple command-line interface (CLI) for easy setup and use.

## **Installation**

PARAKRAM is lightweight and easy to use, with no external dependencies required. To get started, follow these steps:

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/PARAKRAM.git
    cd PARAKRAM
    ```

2. Make sure the script has execution permissions:
    ```bash
    chmod +x parakram
    ```

3. You can now run **PARAKRAM** from your terminal.


## **Usage**

PARAKRAM is a command-line tool that allows you to perform directory busting with ease. Here’s how to use it:


### **Basic Command**

```bash
./parakram --url http://example.com --wordlist /path/to/wordlist.txt
```
This will start the directory busting scan using the provided wordlist against the target URL.


## Enabling Auto Extension Detection(WIP)
To make PARAKRAM automatically detect and append extensions, simply add the --auto-extension flag:

```bash
./parakram --url http://example.com --wordlist /path/to/wordlist.txt --auto-extension
```
This option will help the tool detect extensions like .html, .jsp, .php, and append them to each entry in the wordlist during the scan. It's useful when you’re unsure about the file extensions of hidden directories.

## Example Commands
Scan a website with a custom wordlist:
```bash
./parakram --url http://example.com --wordlist /path/to/wordlist.txt
```

Enable automatic extension detection:
```bash
./parakram --url http://example.com --wordlist /path/to/wordlist.txt --auto-extension
```

Scan a website with verbose output:
```bash
./parakram --url http://example.com --wordlist /path/to/wordlist.txt --verbose
```

## Available Options/Flags
**--url**: The target website URL.
**--wordlist**: Path to the wordlist file used for directory busting.
**--auto-extension**: Automatically detects and appends common file extensions to each wordlist entry.
**--verbose**: Enable detailed output for debugging purposes.
**--help**: Display help and available commands.

## Contribution
I’m happy to allow and encourage fruitful enhancements to this tool. If you have ideas for features or improvements, please feel free to fork the repository and submit a pull request.
I appreciate your contributions and look forward to improving **PARAKRAM** together!

## License
This project is licensed under the MIT License - see the LICENSE file for details.
