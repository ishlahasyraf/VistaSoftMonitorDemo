Feature: VistaSoft Monitor Profile - My User Account Page
    
    Scenario: Verify User data
        When I click on Profile button
        And I click on My User Account 
        Then My User Account page appears
        And First/Last name fields matches 
        And email field matches
