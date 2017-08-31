Feature: Test Admin PAge
  Scenario: Test Admin Login
    When I visit Admin Page
    And  I login as Google+ User
    Then I should be able to see new donation page button

  Scenario: Create New Donation PAge
    Given I am on donation page
    When I go to new donation page
    And I Fill all the values
    Then I should be able to create a new donation page
