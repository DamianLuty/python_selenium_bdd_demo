Feature: Verifying Python.org main page

  Scenario: Main page have correct url
     Given User enters to a "python.org" main page
     Then the main page should be displayed


  Scenario: Searching on python.org main page
    Given User enters to a "python.org" main page
    When User enter a "Python 3.10.0a1" text in search field
    Then The search results should be displayed