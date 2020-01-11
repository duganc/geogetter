# geogetter

### Usage
* Download the repository or python file
* Run `pip3 install requests` in the terminal to install the requests library (ability for python to hit APIs)
* Get an API key from [OpenCageData](https://opencagedata.com/api#intro)
* Create an input csv where the columns are Street Address, City, State, Zip code and save it to your computer
* Run `python3 geogetter.py $YOUR_API_KEY $INPUT_FILE_LOCATION $OUTPUT_FILE_LOCATION` from your terminal

### Note
* OpenCageData has rate limiting.  Make sure you have enough requests that you don't get cut off during processing.
* This script is append only.  If you run it multiple times with the same output it will append, not replace that output.  Delete your previous output if you want to replace it.