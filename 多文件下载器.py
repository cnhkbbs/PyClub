import threading
import requests

def download_file(url, filename):
    """Download file from given URL
    Args:
        url (str): URL to file
        filename (str): Filename to save URL content
    """
    # open in binary mode
    with open(filename, "wb") as file:
        # get request
        response = requests.get(url)
        # write to file
        file.write(response.content)

def main(urls):
    """Download multiple files using threads
    Args:
        urls (list): List of file URLs
    """
    # create a list of threads
    threads = []
    # loop through all URLs
    for url in urls:
        # extract filename from URL
        filename = url.split("/")[-1]
        # create a thread
        thread = threading.Thread(target=download_file, args=(url, filename))
        # start thread
        thread.start()
        # add thread to thread list
        threads.append(thread)
    # loop through all threads
    for thread in threads:
        # wait for thread to complete
        thread.join()

if __name__ == "__main__":
    # list of files to download
    urls = [
        "https://www.example.com/file1.pdf",
        "https://www.example.com/file2.pdf",
        "https://www.example.com/file3.pdf",
    ]
    # call main
    main(urls)
