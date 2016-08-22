import json, requests, ast, iso8601, datetime

"""
    This is my solution to code2040's Tech Assessment.

    - Paul Adedeji
"""

#This token will be used in every step of this technical assessment.
token = "e6e8fdd5b79f27ec527e9fbf0de28812"

""" Step I: Registration

    Connects my github to the registration endpoint and supplies code2040's API with my token.
"""

github = "https://github.com/padedeji/code2040-Tech-Assessment"
url = "http://challenge.code2040.org/api/register"
payload = {"token" : token, "github" : github}
r = requests.post(url, json=json.dumps(payload))

""" Step II: Reverse a String

    Reverses the string that the code2040 Tech Assessment supplies.
"""

#This block of code posts my token to the API and obtains the string to be reversed.
url = "http://challenge.code2040.org/api/reverse"
payload = {"token" : token}
r = requests.post(url, json=payload)
string = r.text

# This function takes a string and reverses it.
def reverse_string(text):
    return text[::-1]

reversed_string = reverse_string(string)

#This block of code posts my token and the new string to code2040's API.
url = "http://challenge.code2040.org/api/reverse/validate"
payload = {"token" : token, "string" : reversed_string}
r = requests.post(url, json=payload)
result = r.text
print result

""" Step III: Needle in a haystack

    Finds a unique string within a list of strings and returns the index of the unique string.
"""

#This block of code obtains the dictionary containing the needle and the haystack.
url = "http://challenge.code2040.org/api/haystack"
payload = {'token' : token}
r = requests.post(url, json=payload)

#This allows the string dictionary i.e. '{}' to be turned into an actual dictionary i.e. {}.
dictionary = ast.literal_eval(r.text)

needle = dictionary["needle"]
haystack = dictionary["haystack"]

#This function locates a unique string within a list of strings.
def needle_in_haystack(s, l):
    return l.index(s)

index = needle_in_haystack(needle, haystack)

#This block of code posts the index of the unique string to code2040's API.
url = "http://challenge.code2040.org/api/haystack/validate"
payload = {'token' : token, 'needle' : index}
r = requests.post(url, json=payload)
result = r.text
print result

""" Step IV: Prefix

    Returns an array of words from a supplied array of words that do NOT contain a certain prefix.
"""

#This block of code obtains the dictionary containing the prefix and array.
url = "http://challenge.code2040.org/api/prefix"
payload = {'token' : token}
r = requests.post(url, json=payload)

dictionary = ast.literal_eval(r.text)

prefix = dictionary["prefix"]
array = dictionary["array"]

#This function returns an array of any words that do not start with the indicated prefix.
def prefix_arr(s, l):
    arr = []
    for i in l:
        if i[0:len(s)] != s:
            arr.append(i)
    return arr

new_array = prefix_arr(prefix, array)

#This block of code posts the new array to code2040's API.
url = "http://challenge.code2040.org/api/prefix/validate"
payload = {'token' : token, 'array' : new_array}
r = requests.post(url, json=payload)
result = r.text
print result

""" Step V: Dating Game

    Adds an interval of time (seconds) to an ISO8601 formatted datestamp.
"""

#This block of code obtains the dictionary containing the datestamp and interval.
url = "http://challenge.code2040.org/api/dating"
payload = {'token' : token}
r = requests.post(url, json=payload)

dictionary = ast.literal_eval(r.text)

datestamp = dictionary["datestamp"]
interval = dictionary["interval"]

#This function adds seconds to an iso8601 datestamp and returns the new datestamp

def dating_game(ds, inter):
    new_date = iso8601.parse_date(ds) + datetime.timedelta(seconds=int(inter))
    #removes +00:00 from the new datestamp and adds Z(Zulu Time Zone)
    new_date = new_date.isoformat()[:-6] + 'Z'
    return new_date

new_datestamp = dating_game(datestamp, interval)

#This block of code posts the new datestamp to the API.
url = "http://challenge.code2040.org/api/dating/validate"
payload = {'token' : token, "datestamp" : new_datestamp}
r = requests.post(url, json=payload)
result = r.text
print result
