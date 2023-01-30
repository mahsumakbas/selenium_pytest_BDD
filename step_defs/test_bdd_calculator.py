from pytest_bdd import when, then, given, parsers
from wrappers.base_page import BasePage

link_calc_app = "//a[@id='calculatetest']"
btn_calculate = "//input[@id='calculate']"
input_num1 = "//input[@id='number1']"
input_num2 = "//input[@id='number2']"
select_calc_op = "//select[@id='function']"
text_answer = "//span[@id='answer']"


@given("open calculator application page")
def open_calculator_app_page(driver):
    BasePage(driver).click_element(link_calc_app)
    BasePage(driver).wait_for_element_to_be_visible(btn_calculate)

@when(parsers.parse("select '{op_name}' from operation dropdown list"))
def select_operation_from_select_list(driver, op_name):
    BasePage(driver).select_dropbox_by_text(select_calc_op, op_name)

@when(parsers.parse("enter '{value}' into number 1 field"))
def enter_number_into_field1(driver, value):
    BasePage(driver).type_element(input_num1, value)

@when(parsers.parse("enter '{value}' into number 2 field"))
def enter_number_into_field2(driver, value):
    BasePage(driver).type_element(input_num2, value)

@when("click on calculate button")
def click_on_calculate_button(driver):
    BasePage(driver).click_element(btn_calculate)

@then(parsers.parse("calculation result should be '{expected_result}'"))
def calculation_result_should_be(driver, expected_result):
    actual_result = BasePage(driver).get_element_text(text_answer)
    assert expected_result == actual_result
