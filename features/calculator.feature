Feature: Four basic operations of calculator

  Background: common step to open calculator app page
    Given open calculator application page

  Scenario: calculate addition of positive integers
    When select 'plus' from operation dropdown list
    And enter '13' into number 1 field
    And enter '47' into number 2 field
    And click on calculate button
    Then calculation result should be '60'
 
   Scenario: calculate addition of negative integers
    When select 'plus' from operation dropdown list
    And enter '-13' into number 1 field
    And enter '-47' into number 2 field
    And click on calculate button
    Then calculation result should be '-60'

  Scenario: calculate multiplication of positive integers
    When select 'times' from operation dropdown list
    And enter '13' into number 1 field
    And enter '47' into number 2 field
    And click on calculate button
    Then calculation result should be '611'

  Scenario: calculate multiplication of negative integers
    When select 'times' from operation dropdown list
    And enter '-13' into number 1 field
    And enter '-47' into number 2 field
    And click on calculate button
    Then calculation result should be '611'

  Scenario: calculate subtraction of positive integers
    When select 'minus' from operation dropdown list
    And enter '47' into number 1 field
    And enter '13' into number 2 field
    And click on calculate button
    Then calculation result should be '34'

  Scenario: calculate subtraction of negative integers
    When select 'minus' from operation dropdown list
    And enter '-47' into number 1 field
    And enter '-13' into number 2 field
    And click on calculate button
    Then calculation result should be '-34'

  Scenario: calculate division of positive integers
    When select 'divide' from operation dropdown list
    And enter '42' into number 1 field
    And enter '6' into number 2 field
    And click on calculate button
    Then calculation result should be '7'

  Scenario: calculate division of negative integers
    When select 'divide' from operation dropdown list
    And enter '-42' into number 1 field
    And enter '-6' into number 2 field
    And click on calculate button
    Then calculation result should be '7'