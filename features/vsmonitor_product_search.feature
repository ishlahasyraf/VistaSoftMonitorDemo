Feature: VistaSoft Monitor Product Search Page

    Scenario: Perform search using serial number (full)
        Given I have logged in to VistaSoft Monitor webpage
        And I click on Product Search button
        When I populate the search field with complete serial number
        And I proceed with the search
        Then I am able to see relevant products in the search results


    Scenario: Perform search using reference number (full)
        Given I have logged in to VistaSoft Monitor webpage
        And I click on Product Search button
        When I populate the search field with complete reference number
        And I proceed with the search
        Then I am able to see relevant products in the search results


    Scenario: Perform search using product name (full)
        Given I have logged in to VistaSoft Monitor webpage
        And I click on Product Search button
        When I populate the search field with complete reference number
        And I proceed with the search
        Then I am able to see relevant products in the search results


    Scenario: Perform search using serial number (partial)

    Scenario: Perform search using reference number (partial)

    Scenario: Perform search using product name (partial)


    Scenario: Perform search for non-existent product

