Feature: Victory Passport Donation Page

  Scenario: I can see victory passport footer on Victory Passport Donation Page
    When I have vp site open
    Then I can see footer Paid for by Stripe AAN

  Scenario: I can contribute on victory passport page
    Given I have vp site open
    When I fill all fields on vp page
    And I click on contribute button
    Then I can make contribution

  Scenario: I should not be able to enter invalid data in lastname
    Given I have vp site open
    And I fill all fields on vp page
    When I change the last name to @@@@@@
    Then I should not be able to make contribution