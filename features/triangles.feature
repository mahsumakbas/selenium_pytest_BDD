Feature: Produce Triangle by value of its sides

    Background: common step to open triangle app page
        Given open triangle application page

    Scenario Outline: produce triangle
        When enter value '<side_1_value>' into side '1' field
        And enter value '<side_2_value>' into side '2' field  
        And enter value '<side_3_value>' into side '3' field
        And click on identify button
        Then triangle type should be '<result>'
        
        Examples:
            | side_1_value | side_2_value | side_3_value | result |
            | 5            | 6            | 7            | Scalene |
            | 6            | 6            | 7            | Isosceles |
            | 6            | 6            | 6            | Equilateral |
            | 5            | 6            | 11           | Error: Not a Triangle | 

