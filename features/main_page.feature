Feature: CBUK Main Page Testing


  Scenario Outline: Navbar Testing
    Given the user is on the cbuk main page
    When the navbar is visible
    And the Carpetbright logo should be present with the home page link
    And the phone number "<phone_number>" should be there on the page
    And the "<opening_hours>" should be present on the page
    Then it will close the browser

    Examples:
      | phone_number     |  opening_hours |
      | 020 3011 5590    |  Open 6 days 9am - 6pm |