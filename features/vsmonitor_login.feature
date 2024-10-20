Feature: VistaSoft Monitor Login Page

    @skip_before
    Scenario: Successful Login
        Given I launched chrome browser
        When open VistaSoft Monitor webpage
        And input Email in Email field
        And input Password in Password field
        And Click on Log-in button
        Then I am able to Login successfully


