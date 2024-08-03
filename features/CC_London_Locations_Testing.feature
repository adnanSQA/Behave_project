Feature: Carpet Cleaning Abbey Wood Page

  Scenario: Verify the page title and banner section
    When the user redirects to the page
    Then the browser title should be Carpet Cleaning Abbey Wood, SE2 | 20 000+ Reviews
    And the banner section heading should be Carpet Cleaning Abbey Wood
    And the banner input field should be present
    And there should be a button that takes the user to a new page on click
    And a banner reviews image should be present

  Scenario: Verify content section
    Then the content heading should be CARPET CLEANING ABBEY WOOD
    And a content image should be present on the page
    And the content image should have an alt attribute with the value Carpet Cleaning Abbey Wood SE2

  Scenario: Verify the We Guarantee section
    Then there should be a We Guarantee section
    And it should display 5 boxes on the page
    And the footer of this section should have the heading Call Our Local Carpet Cleaning Branch On 020 3519 8926

  Scenario: Verify the Need Your Carpet Clean? section
    Then there should be a Need Your Carpet Clean? section
    And it should have a title for the input field
    And there should be an input field
    And there should be a Get a Quote button

  Scenario: Verify the Additional Services section
    Then there should be an Additional Services heading
    And it should contain the text Call us for a Free Estimate
    And it should display the phone number
    And it should include the text Voted #1 carpet cleaner in London. Our customer service hours are 9.00am to 6.00pm 6 days a week.
