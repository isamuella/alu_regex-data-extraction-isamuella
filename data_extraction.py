import re

# These are regular expressions for each form field chosen
email_regex = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
url_regex = r"https?://[a-zA-Z0-9./_-]+"
phone_regex = r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"
currency_regex = r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?"
time_regex = r"\b((?:1[0-2]|0?[1-9]):[0-5][0-9]\s?(?:AM|PM|am|pm)|(?:[01]?[0-9]|2[0-3]):[0-5][0-9])\b"

# This function checks if the given data has the right format
def test_regex(test_data):
    """
    This function checks the input `test_data` for valid emails, URLs, phone numbers, times, and cur    rencies.    
    It excludes invalid matches like:
    - funny_email@domain
    - gktp://example.com
    - +250 781 449
    - 21:65 PM
    - 76:00
    - 5866
    """

    # Then we check for all matches in the test data using our regex patterns
    emails = re.findall(email_regex, test_data)
    urls = re.findall(url_regex, test_data)
    phones = re.findall(phone_regex, test_data)
    currency = re.findall(currency_regex, test_data)
    times = re.findall(time_regex, test_data)

    # Here we check if the number of valid matches is what we expect
    assert len(emails) == 3, f"Expected 3 emails, but found {len(emails)}: {emails}"
    assert len(urls) == 2, f"Expected 2 URLs, but found {len(urls)}: {urls}"
    assert len(phones) == 3, f"Expected 3 phone numbers, but found {len(phones)}: {phones}"
    assert len(times) == 3, f"Expected 3 times, but found {len(times)}: {times}"
    assert len(currency) == 4, f"Expected 4 currencies, but found {len(currency)}: {currency}"

    # If no problem then print the succes message
    print("\nAll tests passed successfully!")

# Here is some sample data to test the function
test_data = """
Emails: user@example.com, firstname.lastname@company.co.uk, funny_email@domain, s.ineza@alustudent.com
URLs: https://www.example.com, http://subdomain.example.org/page, gktp://example.com
Phones: (123) 456-7890, 123-456-7890, 123.456.7890, +250 781 449
Times: 14:30, 2:30 PM, 09:25, 21:65 PM, 76:00
Currency: $19.99, $1,234.56, $4040, $23,000,000, 5866
"""

# Call the function with the sample text
test_regex(test_data)

