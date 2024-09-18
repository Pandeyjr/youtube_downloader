YouTube Downloader
This is a Python-based YouTube video downloader application that allows users to download videos from YouTube using the URL.

Features
Download videos from YouTube by providing the video URL.
Save the downloaded videos to a specific location.
Easy to use command-line interface.
Requirements
Python 3.6 or later
yt-dlp (for downloading videos)
Installation
Clone the repository to your local machine:

bash
Copy code
git clone https://github.com/Pandeyjr/youtube_downloader.git
Navigate into the project directory:

bash
Copy code
cd youtube_downloader
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Usage
Run the YouTube downloader script from the command line:

bash
Copy code
python youtube_downloader.py
Enter the YouTube video URL when prompted.

Enter the download path or press Enter to save the video in the current directory.

Example:

bash
Copy code
Enter the YouTube video URL: https://www.youtube.com/watch?v=xyz123
Enter the download path (default is current directory): videos/
The video will be downloaded and saved to the specified folder.

Packaging the Project
To package the project for distribution:

Ensure setuptools is installed:

bash
Copy code
pip install setuptools
Build the package:

bash
Copy code
python setup.py sdist bdist_wheel
Install the package locally:

bash
Copy code
pip install .
Known Issues
Make sure you are using the latest version of yt-dlp as YouTube frequently updates its site and this may cause downloading issues.
Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request if you have suggestions for improvements or bug fixes.

License
This project is licensed under the MIT License. See the LICENSE file for details.
