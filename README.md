# Extraction Of Data Using Regular Expressions

## Understanding the Project

This project aims to extract required data from hundreds of thousands of pages of string using regular expressions (Regex) in python. These are:
- Email addressses
- URLs
- Phone numbers
- Time in 12-hour or 24-hour format
- Currency amounts

I will use 're' a python's module to define and utilize regex patterns then extract information from sample data. These include


## Features used of the project

1. Email Extraction: The program finds and extracts valid email adddresses.
2. URL Extraction: The program finds and extracts valid HTTP and HTTPS URLs.
3. Phone Numbers Ectraction: Extracts valid phone numbers found in different formats.
4. Currency Extraction: Extracts currency values in only USD format ($) and excludes invalid values.
5. Time Extraction: Extracts time in 12-hour or 24-hour format and excludes all other invalid values.


## Regular Expressions used for the project

The following regex were used for different data typas:
- Email:
**r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"**
This regex matches only valid email addresses.

- URL:
**r"https?://[a-zA-Z0-9./_-]+"**
This regex catches only valid HTTP and HTTPS URLs.

- Phone numbers:
**r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"**
This regex matches all phone numbers that have different formatting choices.

- Currency:
**r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?"**
This regex  catches currency amounts that are in USD format and excludes any other ike 5866.

- Time:
**r"\b((?:1[0-2]|0?[1-9]):[0-5][0-9]\s?(?:AM|PM|am|pm)|(?:[01]?[0-9]|2[0-3]):[0-5][0-9])\b"**
This regex finds both 12-hour and 24-hour time formats and excludes any other like 21:65 PM.


## Sample data used for the project
Here is the sampke data that i used to test the regular expressions:


## Example Output
The program will output the following:

- Emails:
['user@example.com', 'firstname.lastname@company.co.uk', 's.ineza@alustudent.com']

- URLs:
['https://www.example.com', 'http://subdomain.example.org/page']

- Phone Numbers:
['(123) 456-7890', '123-456-7890', '123.456.7890']

- Times:
['14:30', '2:30 PM', '09:25']

- Currency:
['$19.99', '$1,234.56', '$23,000,000']

## How To Run The Program

1. Clone the repository on your machine:
git clone https://github.com/your-username/alu_regex-data-extraction.git and then enter the repo using **cd**

2. Run the python script:
Python regex_data_extraction.py


## Test Cases
The program involves test cases to make sure that the regex are working as they should. Every test case confirms that the correct number of valid matches are found for every data types.

### Test cases used
- Emails: 3 valid emails (excludes funny_email@domain)
- URLs: 2 valid URLs (excludes gktp://example.com)
- Phone numbers: 3 valid phone numbers (excludes +250 781 449)
- Currency: 4 valid currency amounts (excludes 5866)
- Times: 3 valid times (excludes 21:65 PM)

## Contribution
Feel free to fork this repository and make pull requests to contribute for more improvements or bug fixes.
