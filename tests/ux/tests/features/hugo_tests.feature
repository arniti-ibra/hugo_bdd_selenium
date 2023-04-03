Feature: Hugo Site Testing
    Scenario: Test index page
        Given you launch Chrome Browser and you have your site running
        When you open the page
        Then verify your chrome browser is at the correct url and the title of the page is Hugo Site
        And take a screenshot of the index page
    
    Scenario: Test first page
        Given you move to testing the first page
        When you verify you are at the correct page url and the title is Baqir | Hugo Site
        Then check the text of the page on baqir is the same as your assertion
        And verify the images on your page exist, testing 
        And take a screenshot of the first page
    
    Scenario: Test second page
        Given you move to testing the second page
        When you verify you are at the correct page url and the title is iphone | Hugo Site
        Then check the text of the page is the same as the poem on the page
        And verify there are no images this page
        And take a screenshot of the second page
