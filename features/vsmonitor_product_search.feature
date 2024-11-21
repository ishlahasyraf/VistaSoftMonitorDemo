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
        When I populate the search field with complete product name
        And I proceed with the search
        Then I am able to see relevant products in the search results

    # Scenario: Perform search using serial number (partial)
    #     Given I have logged in to VistaSoft Monitor webpage
    #     And I click on Product Search button
    #     When I populate the search field with partial serial number
    #     And I proceed with the search
    #     Then I am able to see relevant products in the search results

    Scenario: Perform search using reference number (partial)
        Given I have logged in to VistaSoft Monitor webpage
        And I click on Product Search button
        When I populate the search field with partial reference number
        And I proceed with the search
        Then I am able to see relevant products in the search results

    Scenario: Perform search using product name (partial)
        Given I have logged in to VistaSoft Monitor webpage
        And I click on Product Search button
        When I populate the search field with partial product name
        And I proceed with the search
        Then I am able to see relevant products in the search results


    Scenario: Perform search for non-existent product
        Given I have logged in to VistaSoft Monitor webpage
        And I click on Product Search button
        When I populate the search field with non-existent product
        And I proceed with the search
        Then I am not able to see any search results

