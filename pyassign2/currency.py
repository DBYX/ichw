# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 17:26:18 2017

@author: 惠普
"""


"""module 1 : all the functions to be used"""


def before_space(x):
    """ Returns: Substring of x; up to, but not including, the first space

    Parameter x: the string to slice
    Precondition: x has at least one space in it """
    return x.split()[0]


def get_from(json):
    """ Returns: The FROM value in the response to a currency query.

    Given a JSON response to a currency query, this returns the string
    inside double quotes (") immediately following the keyword "from".
    For example, if the JSON is

      '{"from":"2 United States Dollars","to":"1.825936 Euros","success":true,
      "error":""}'

    then this function returns '2 United States Dollars'
    (not '"2 United States Dollars"').
    It returns the empty string if the JSON is the result of on invalid query.

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query """
    json = json.split('"')[3]
    return json


def get_to(json):
    """ Returns: The TO value in the response to a currency query.

    Given a JSON response to a currency query, this returns the string
    inside double quotes (") immediately following the keyword "to".
    For example, if the JSON is

      '{"from":"2 United States Dollars","to":"1.825936 Euros","success":true,
      "error":""}'

    then this function returns '1.825936 Euros' (not '"1.825936 Euros"').
    It returns the empty string if the JSON is the result of on invalid query.

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query """
    json = json.split('"')[7]
    return json


def has_error(JSON):
    """ Returns: The FROM value in the response to a currency query.

    Given a JSON response to a currency query, this returns the string inside
    double quotes (") immediately following the keyword "from".
    For example, if the JSON is

      '{"from":"2 United States Dollars","to":"1.825936 Euros","success":true,
      "error":""}'

    then this function returns '2 United States Dollars'
    (not '"2 United States Dollars"').
    It returns the empty string if the JSON is the result of on invalid query.

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query """
    JSON = JSON.split('"')[10]
    JSON = JSON.split()[1]
    return JSON == "false,"


def currency_response(currency_from, currency_to, amount_to):
    """Returns: a JSON string that is a response to a currency query.

    A currency query converts amount_from money in currency currency_from
    to the currency currency_to. The response should be a string of the form

        '{"from":"<old-amt>","to":"<new-amt>","success":true, "error":""}'

    where the values old-amount and new-amount contain the value and name
    for the original and new currencies. If the query is invalid, both
    old-amount and new-amount will be empty, while "success" will be followed
    by the value false.

    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string

    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string

    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""
    from urllib.request import urlopen
    doc = urlopen(
        'http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=%s&to=%s&amt=%f'
        % (currency_from, currency_to, amount_to))
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    return jstr


def exchange(currency_from, currency_to, amount_to):
    """Returns: amount of currency received in the given exchange.

    In this exchange, the user is changing amount_from money in
    currency currency_from to the currency currency_to. The value
    returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string for a valid currency code

    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string for a valid currency code

    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""
    x = currency_response(currency_from, currency_to, amount_to)
    x = get_to(x)
    x = before_space(x)
    return x


"""module 2 : test functions"""


def test_A():
    """To determine whether there is an invalid currency code or invalid
    currency number input"""
    s = currency_response(currency_from_, currency_to_, amount_to_)
    assert(get_to(s) != " ")
    assert(get_from(s) != " ")


def test_B():
    """to determine whether there is an error"""
    s = currency_response(currency_from_, currency_to_, amount_to_)
    assert(not has_error(s))


"""module 3 : testAll helps with a thorough test on the input contents
before operation"""


def testAll():
    """test all cases"""
    test_A()
    test_B()
    print("All tests passed")


""""the operation module"""

currency_from_ = input()
currency_to_ = input()
amount_to_ = float(input())

testAll()

if __name__ == "__main__":
    print(exchange(currency_from_, currency_to_, amount_to_))
