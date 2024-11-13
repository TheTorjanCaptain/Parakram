# Parakram: A Powerful Directory Buster Tool for Security Testing

Parakram is an advanced directory buster designed to help penetration testers, security researchers, and developers discover hidden directories and files within web applications. It uses a customizable wordlist and supports recursive scanning to reveal potential vulnerabilities in the structure of web applications. Parakram is built with performance in mind, leveraging multithreading for faster scans and providing detailed results with customizable output formats (JSON, CSV, or plain text).

## Key Features:
- **Customizable Wordlist**: Easily load a wordlist and apply optional extensions.
- **Recursive Scanning**: Automatically follow subdirectories to uncover deeper paths.
- **Flexible Request Options**: Choose HTTP methods, set custom headers, or use proxies.
- **Rate Limiting**: Control the rate of requests to avoid overloading servers.
- **Verbose Mode**: View detailed logs for every request, including successful and failed attempts.
- **Output Formats**: Export results in JSON, CSV, or plain text formats.
- **Multi-Threading**: Speed up the scanning process using threads.

## Installation:
Clone the repository and install dependencies:
```bash
git clone https://github.com/your-username/parakram.git
cd parakram
pip install -r requirements.txt(Not required as of now)
