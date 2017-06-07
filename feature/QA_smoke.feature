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
    Then sleep "7" seconds
    Then verify user "NEW_USER" is Logged in

  #Scenario: QA: New user can add social media accounts - happy path
    Then input text "Brand 1" to text field with placeholder "Enter Brand name"
    Then Click span by text "Add"
    Then sleep "7" seconds
    Then Click button to add "Facebook" social media account
    Then sleep "3" seconds
    Then Switch to active window
    Then sleep "3" seconds
    Then input text "test.yuvzhik@gmail.com" to text field with ID "email"
    Then input text "go2017" to text field with ID "pass"
    Then sleep "10" seconds
    Then Click input button by name "login"
    Then Switch to active window
    Then sleep "5" seconds
    Then check "facebook" account
    Then sleep "5" seconds
    Then Click button with class "save-button active" by text "Save"
    Then sleep "3" seconds
    #Then Click button to add "Twitter" social media account
    #Then sleep "15" seconds
    #Then Switch to active window
    #Then sleep "15" seconds
    #Then Click label by text "Username or email"
    #Then sleep "30" seconds
    #Then input text "test.yuvzhik@gmail.com" to label with text "Username or email"
    #Then input text "test.yuvzhik@gmail.com" to text field with ID "username_or_email"
    #Then Click label by text "Password"
    #Then input text "abcabc123" to text field with ID "password"
    #Then input text "abcabc123" to text field with label for "Password"
    #Then send symbl "test.yuvzhik@gmail.com" to active element
    #Then sleep "3" seconds
    #Then Click input button by ID "allow"
    #Then Switch to active window
    #Then sleep "3" seconds
    #Then check "twitter" account
    #Then sleep "2" seconds
    #Then Click button with class "save-button active" by text "Save"
    #Then wait "10" second until expected condition of element by "//input[@name='username_or_email']" is visible
    #Then input text "test.yuvzhik@gmail.com" to text field with ID "username_or_email"
    Then Click button to add "Google Plus" social media account
    Then sleep "5" seconds
    Then Switch to active window
    Then input text "test.yuvzhik@gmail.com" to text field with ID "Email"
    Then Click input button by ID "next"
    Then sleep "2" seconds
    Then input text "go20172017" to text field with ID "Passwd"
    Then sleep "2" seconds
    Then Click input button by ID "signIn"
    Then sleep "2" seconds
    Then Switch to active window
    Then Click button by text "Allow"
    Then sleep "5" seconds
    Then Switch to active window
    Then check "googleplus" account
    Then sleep "5" seconds
    Then Click button with class "save-button active" by text "Save"
    Then sleep "2" seconds
    Then Click button to add "Linkedin" social media account
    Then sleep "2" seconds
    Then Switch to active window
    Then input text "test.yuvzhik@gmail.com" to text field with ID "session_key-login"
    Then sleep "2" seconds
    Then input text "abcabc123" to text field with ID "session_password-login"
    Then sleep "2" seconds
    Then Click input button by name "signin"
    Then sleep "2" seconds
    Then Switch to active window
    Then sleep "2" seconds
    Then check "linkedin" account
    Then Click button with class "save-button active" by text "Save"
    Then sleep "2" seconds
    Then Click button to add "Instagram" social media account
    Then sleep "2" seconds
    Then Switch to active window
    Then input text "test.yuvzhik" to text field with ID "id_username"
    Then input text "go2017" to text field with ID "id_password"
    Then Click input button by type "submit"
    Then sleep "2" seconds
    Then Switch to active window
    Then sleep "2" seconds
    Then check "instagram" account
    Then Click button with class "save-button active" by text "Save"
    Then sleep "10" seconds
    Then Click button in div with class "content-area" with class "save-button" by text "Close"
    Then sleep "2" seconds
    Then Click div with class "user-pic"
    Then sleep "2" seconds
    Then Click link by class "link logout"
  #Scenario: user can login with existing account
    #Then Go to "qa.eclincher"
    Then input text "generated_email" to text field with ID "l-txt-email-address"
    Then sleep "2" seconds
    Then input text "STANDARD_PSW" to text field with ID "l-txt-password"
    Then Click button by text "Login"











