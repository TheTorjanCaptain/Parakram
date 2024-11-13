import requests
import argparse
import time
import threading
import json
import csv
from queue import Queue

# Function to load wordlist
def load_wordlist(wordlist_file):
    try:
        with open(wordlist_file, "r") as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        print(f"Error: The file '{wordlist_file}' was not found.")
        return []

# Directory busting function
def directory_buster(url, wordlist, method, timeout, user_agent, proxy, rate, recursive, output, status_filter, follow_redirects, headers, output_format):
    found_urls = []
    proxies = {"http": proxy, "https": proxy} if proxy else None
    headers = headers if headers else {"User-Agent": user_agent}
    
    def test_directory(directory):
        target_url = f"{url}/{directory}"
        try:
            # Adding verify=False to bypass SSL certificate verification
            response = requests.request(
                method, 
                target_url, 
                headers=headers, 
                timeout=timeout, 
                proxies=proxies, 
                allow_redirects=follow_redirects, 
                verify=False  # Disable SSL verification
            )
            status_message = f"{target_url} - Status Code: {response.status_code}"

            # Print all URLs and status codes if in verbose mode, or only matching status codes
            if args.verbose:
                print("Testing", status_message)
            if response.status_code in status_filter or response.status_code == 200:
                found_urls.append({"url": target_url, "status_code": response.status_code})
                print("Found:", status_message)

            # Recursive scanning for subdirectories if enabled and status code is 200
            if recursive and response.status_code == 200:
                for subdirectory in wordlist:
                    test_directory(f"{directory}/{subdirectory}")

            time.sleep(rate)
        except requests.RequestException as e:
            if args.verbose:
                print(f"Error accessing {target_url}: {e}")

    # Start busting directories
    for directory in wordlist:
        test_directory(directory)

    # Output results to file if specified
    if output:
        if output_format == 'json':
            with open(output, 'w') as f:
                json.dump(found_urls, f, indent=4)
        elif output_format == 'csv':
            with open(output, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["URL", "Status Code"])
                for entry in found_urls:
                    writer.writerow([entry["url"], entry["status_code"]])
        else:
            with open(output, 'w') as f:
                for entry in found_urls:
                    f.write(f"{entry['url']} - Status Code: {entry['status_code']}\n")

    # Summary of found URLs
    if found_urls:
        print(f"\n{len(found_urls)} URL(s) were found.")
    else:
        print("\nNo matching URLs were found.")

# Argument parsing
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advanced Directory Buster")
    parser.add_argument("-w", "--wordlist", required=True, help="Path to the wordlist file")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose mode to show all tested paths")
    parser.add_argument("-m", "--method", default="GET", help="HTTP method to use (default: GET)")
    parser.add_argument("-t", "--timeout", type=int, default=5, help="Request timeout in seconds (default: 5)")
    parser.add_argument("-a", "--user-agent", default="Mozilla/5.0", help="Custom User-Agent string")
    parser.add_argument("-p", "--proxy", help="HTTP/SOCKS proxy (e.g., http://127.0.0.1:8080)")
    parser.add_argument("-r", "--rate", type=float, default=0, help="Rate limit: delay in seconds between requests (default: 0)")
    parser.add_argument("-R", "--recursive", action="store_true", help="Enable recursive directory busting")
    parser.add_argument("-o", "--output", help="File to save the output results")
    parser.add_argument("-s", "--status", type=str, default="200,403", help="Comma-separated status codes to filter (default: 200,403)")
    parser.add_argument("--follow-redirects", action="store_true", help="Follow redirects for URLs")
    parser.add_argument("--header", action="append", help="Custom headers for requests (e.g., --header 'Authorization: Bearer <token>')")
    parser.add_argument("--json", action="store_const", const="json", dest="output_format", help="Output results in JSON format")
    parser.add_argument("--csv", action="store_const", const="csv", dest="output_format", help="Output results in CSV format")
    args = parser.parse_args()

    # Convert status code filter to a list of integers
    status_filter = list(map(int, args.status.split(',')))
    
    # Parse custom headers
    headers = {}
    if args.header:
        for header in args.header:
            key, value = header.split(": ", 1)
            headers[key] = value

    # Prompt for URL input
    url = input("Enter the URL (e.g., http://example.com): ").strip()
    
    # Load wordlist
    wordlist = load_wordlist(args.wordlist)
    if not wordlist:
        print("Wordlist is empty or could not be loaded.")
        exit(1)

    # Run directory buster with all options
    directory_buster(
        url=url,
        wordlist=wordlist,
        method=args.method,
        timeout=args.timeout,
        user_agent=args.user_agent,
        proxy=args.proxy,
        rate=args.rate,
        recursive=args.recursive,
        output=args.output,
        status_filter=status_filter,
        follow_redirects=args.follow_redirects,
        headers=headers,
        output_format=args.output_format
    )
