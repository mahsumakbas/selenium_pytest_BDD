from pytest_bdd import when, then, given, parsers
from wrappers.base_page import BasePage
import time

link_triangle_app = "//a[@id='triangleapp']"
btn_identify_type = "//button[@id='identify-triangle-action']"
input_side = "//input[@id='side{}']"
# input_side1 = "//input[@id='side1']"
# input_side2 = "//input[@id='side2']"
# input_side3 = "//input[@id='side3']"
text_result = "//p[@id='triangle-type']"

@given("open triangle application page")
def open_triangle_app_page(driver):
    BasePage(driver).click_element(link_triangle_app)
    BasePage(driver).wait_for_element_to_be_visible(btn_identify_type)

@when(parsers.parse("enter value '{side_value}' into side '{side_no}' field"))
def enter_value_into_sides(driver, side_value, side_no):
    input_path = input_side.format(side_no)
    BasePage(driver).type_element(input_path, side_value)

@when("click on identify button")
def click_identify_button(driver):
    BasePage(driver).click_element(btn_identify_type)

@then(parsers.parse("triangle type should be '{expected_result}'"))
def calculation_result_should_be(driver, expected_result):
    actual_result = BasePage(driver).get_element_text(text_result)
    assert expected_result == actual_result

