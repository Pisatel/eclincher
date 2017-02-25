# Created by Alex Yuvzhik at 2/13/2017
Feature: Smoke Tests
  # Enter feature description here

  Scenario: QA: New user registration - happy path
    Then Go to "qa.eclincher"
    Then Click link by text "Create New Account"
    Then sleep "5" seconds
    Then Click link by class "selectBox custom-select form-control selectBox-dropdown"
    Then Click link by text "Agency"
    Then input text "Alex" to text field with ID "s-txt-fname"
    Then input text "Yuvzhik" to text field with ID "s-txt-lname"
    Then input text "NEW_EMAIL" to text field with ID "s-txt-email"
    Then input text "STANDARD_PSW" to text field with ID "s-txt-password"
    Then input text "STANDARD_PSW" to text field with ID "s-txt-password-confirm"
    Then Click button by text "Create Account"
    Then sleep "15" seconds
    Then Click link by title "Click here to close"
    Then sleep "10" seconds
    Then verify user "NEW_USER" is Logged in
  Scenario: QA: New user can add social media accounts - happy path
    Then input text "Brand 1" to text field with placeholder "Enter Brand name"
    Then Click span by text "Add"
    Then sleep "10" seconds
    Then Click button to add "Facebook" social media account



