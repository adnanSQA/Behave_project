Feature: CBUK Main Page Testing


  # Scenario Outline: Navbar Testing
  #   Given the user is on the cbuk main page
  #   When the navbar is visible
  #   And the Carpetbright logo should be present with the home page link
  #   And the phone number "<phone_number>" should be there on the page
  #   And the "<opening_hours>" should be present on the page 

  #   Examples:
  #     | phone_number     |  opening_hours |
  #     | 020 3011 5590    |  Open 6 days 9am - 6pm |
    
  Scenario: Verify Presence of the data
    Given the user is on the cbuk main page
    Then The banner text should be there 
    And The bullet points should be exact
    And Verify the banner button background color