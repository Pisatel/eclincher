from datetime import *
from lettuce import *
#from selenium.webdriver.support import expected_conditions
from lettuce import world
from steps_config import *
import time
from selenium.webdriver.support.ui import WebDriverWait




@step('Go to "([^"]*)"')
def go_to_url(step, url):
    urls = {"qa.eclincher": "https://qa.eclincher.com/login/",
            "app.eclincher": "https://app.eclincher.com/login/",
            "arun.eclincher": "https://arun.eclincher.com/login/"}
    if url in urls:
        url = urls[url]

    get_driver().get(url)


@step('Click link by text "([^"]*)"')
def click_link_txt(step, link_txt):
    links = get_driver().find_elements_by_xpath("//a[text()='%s']" % link_txt)
    if links:
        links[0].click()
    else:
        raise ValueError('Link with txt %s not found' % link_txt)


@step('Click link by class "([^"]*)"')
def click_link_class(step, link_class):
    links = get_driver().find_elements_by_xpath("//a[@class='%s']" % link_class)
    if links:
        links[0].click()
    else:
        raise ValueError('Link with class %s not found' % link_class)


@step('sleep "([^"]*)" seconds')
def sleep_sec(step, seconds):
    time.sleep(float(seconds))


@step('input text "([^"]*)" to text field with ID "([^"]*)"')
def input_with_id(step, txt, ID):
    global new_email
    links = get_driver().find_elements_by_xpath("//input[@id='%s']" % ID)
    if links:
        links[0].click()
    else:
        raise ValueError('Link with ID %s not found' % ID)
    if not "generated_email" in txt:
        timestamp = datetime.now().strftime('%m_%d_%Y.%H_%M')
        new_email = "automation.%s@yopmail.com" % timestamp
        txts = {"NEW_EMAIL": new_email,
                "STANDARD_PSW": "go2017",
                "NEW_USER": new_email,
                }
        if txt in txts.keys():
            txt = txts[txt]
    else:
        txt = new_email
    links[0].send_keys(str(txt))





@step('Click button by text "([^"]*)"')
def click_by_txt(step, button_txt):
    buttons = get_driver().find_elements_by_xpath("//button[text()='%s']" % button_txt)
    if buttons:
        buttons[0].click()
    else:
        raise ValueError('Button with text %s not found' % button_txt)


@step('Click link by title "([^"]*)"')
def click_link_title(step, title):
    links = get_driver().find_elements_by_xpath("//a[@title='%s']" % title)
    if links:
        links[0].click()
    else:
        raise ValueError('Link with title %s not found' % title)


@step('verify user "([^"]*)" is Logged in')
def verif_loggin(step, user_name):
    user_names = {"NEW_USER": new_email}
    if user_name in user_names:
        user_name = user_names[user_name]
    link = get_driver().find_element_by_xpath("//div[@class='user-name'][@data-full-username='%s']" % user_name)
    assert (link, "No link with %s found" % user_name)


@step('input text "([^"]*)" to text field with placeholder "([^"]*)"')
def txt_to_placeholder(step, txt, placeholder):
    links = get_driver().find_elements_by_xpath("//input[@placeholder='%s']" % placeholder)
    if links:
        links[0].send_keys(str(txt))
    else:
        raise ValueError('Field with %s placeholder not found' % placeholder)


@step('Click button to add "([^"]*)" social media account')
def click_sm_button(step, name):
    buttons = get_driver().find_elements_by_xpath("//div[@id='accounts-manager']//div[@data-track='%s']" % name)
    if buttons:
        buttons[0].click()
    else:
        raise ValueError('Button %s social media is not found')


@step('Click span by text "([^"]*)"')
def click_span(step, span_txt):
    buttons = get_driver().find_elements_by_xpath("//span[text()='%s']" % span_txt)
    if buttons:
        buttons[0].click()
    else:
        raise ValueError('Span with text %s not found' % span_txt)


@step("Switch to active window")
def switch(step):
    get_driver().switch_to.window(get_driver().window_handles[-1])


@step('Click input button by name "([^"]*)"')
def click_name(step, name_button):
    buttons = get_driver().find_elements_by_xpath("//input[@name='%s']" % name_button)
    if buttons:
        buttons[0].click()
    else:
        raise ValueError('Input button with name %s not found' % name_button)


@step('check "([^"]*)" account')
def check_box_click(step, acc_name):
    boxes = get_driver().find_elements_by_xpath("//div[@class ='ec-account %s']//input[@type = 'checkbox'][@class = "
                                                   "'checkbox']" % acc_name)
    if boxes:
        for box in boxes:
            if box.is_displayed():
                box.click()
    else:
        raise ValueError('%s accounts not displayed' % acc_name)


@step('Click input button by ID "([^"]*)"')
def click_name(step, id_button):
    buttons = get_driver().find_elements_by_xpath("//input[@id='%s']" % id_button)
    if buttons:
        buttons[0].click()
    else:
        raise ValueError('Input button with name %s not found' % id_button)


@step('Click button with class "([^"]*)" by text "([^"]*)"')
def click_class(step, class_name, button_txt):
    buttons = get_driver().find_elements_by_xpath("//button[@class='%s'][text()='%s']" % (class_name, button_txt))
    if buttons:
        buttons[0].click()
    else:
        raise ValueError('Button with text %s, or class %s not found' % (button_txt, class_name))


@step('input text "([^"]*)" to text field with label for "([^"]*)"')
def input_label(step, txt, label_for):
    links = get_driver().find_elements_by_xpath("//label[@for='%s']" % label_for)
    if links:
        links[0].send_keys(str(txt))
    else:
        raise ValueError('Field with label for %s not found' % label_for)


@step('Click label by text "([^"]*)"')
def click_label_by_txt(step, txt):
    labels = get_driver().find_elements_by_xpath("//label[text()='%s']" % txt)
    if labels:
        labels[0].click()
    else:
        raise ValueError('Label with text %s not found' % txt)


@step('input text "([^"]*)" to label with text "([^"]*)"')
def input_txt_label(step, txt, label_txt):
    labels = get_driver().find_elements_by_xpath("//label[text()='%s']" % label_txt)
    if labels:
        labels[0].send_keys(str(txt))
    else:
        raise ValueError('Label with %s text not found' % label_txt)


@step('send symbl "([^"]*)" to active element')
def send_symbl(step, txt):
    ActionChains.send_keys(str(txt))
    ActionChains.perform()


@step('wait "([^"]*)" second until expected condition of element by "([^"]*)" is visible')
def wait_visible(step, seconds, xpath):
    WebDriverWait(get_driver, float(seconds)).until(expected_conditions.element_to_be_clickable("[%s] %xpath"))


@step('Click input button by type "([^"]*)"')
def click_type(step, type_button):
    buttons = get_driver().find_elements_by_xpath("//input[@type='%s']" % type_button)
    if buttons:
        buttons[0].click()
    else:
        raise ValueError('Input button with type %s not found' % type_button)


@step('Click button in div with class "([^"]*)" with class "([^"]*)" by text "([^"]*)"')
def click_class_in_div(step, div_class, class_name, button_txt):
    buttons = get_driver().find_elements_by_xpath("//div[@class='%s']//button[@class='%s'][text()='%s']" %
                                                  (div_class, class_name, button_txt))
    if buttons:
        buttons[0].click()
    else:
        raise ValueError('Button with text %s, or class %s, or div class %s not found' %
                         (button_txt, class_name, div_class))


@step('Click div with class "([^"]*)"')
def click_div_by_class(step, clss):
    buttons = get_driver().find_elements_by_xpath("//div[@class='%s']" % clss)
    if buttons:
        buttons[0].click()
    else:
        raise ValueError('Div button with class %s not found' % clss)

