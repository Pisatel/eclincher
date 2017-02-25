from datetime import *
from lettuce import *
from steps_config import *
import time


@step('Go to "([^"]*)"')
def go_to_url(step, url):
    urls = {"qa.eclincher":"https://qa.eclincher.com/login/",
            "app.eclincher":"https://app.eclincher.com/login/",
            "arun.eclincher":"https://arun.eclincher.com/login/"}
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
def click_link_class (step, link_class):
    links = get_driver().find_elements_by_xpath("//a[@class='%s']" % link_class)
    if links:
        links[0].click()
    else:
        raise ValueError('Link with class %s not found' % link_class)


@step('sleep "([^"]*)" seconds')
def sleep_sec (step, seconds):
    time.sleep(float(seconds))


@step('input text "([^"]*)" to text field with ID "([^"]*)"')
def step_impl(step, txt, ID):
    global new_email
    links = get_driver().find_elements_by_xpath("//input[@id='%s']" % ID)
    if links:
        links[0].click()
    else:
        raise ValueError('Link with ID %s not found' % ID)
    timestamp = datetime.now().strftime('%m_%d_%Y.%H_%M')
    new_email = "automation.%s@yopmail.com" % timestamp
    txts = {"NEW_EMAIL":new_email,
            "STANDARD_PSW":"go2017"}
    if txt in txts:
        txt = txts[txt]
    links[0].send_keys(str(txt))


@step('Click button by text "([^"]*)"')
def step_impl(step, button_txt):
    buttons = get_driver().find_elements_by_xpath("//button[text()='%s']" % button_txt)
    if buttons:
        buttons[0].click()
    else:
        raise ValueError('Button with text %s not found' % button_txt)


@step('Click link by title "([^"]*)"')
def click_link_title (step, title):
    links = get_driver().find_elements_by_xpath("//a[@title='%s']" % title)
    if links:
        links[0].click()
    else:
        raise ValueError ('Link with title %s not found' % title)


@step('verify user "([^"]*)" is Logged in')
def step_impl(step, user_name):
    user_names = {"NEW_USER":new_email}
    if user_name in user_names:
       user_name = user_names[user_name]
    link = get_driver().find_element_by_xpath("//div[@class='user-name'][@data-full-username='%s']" % user_name)
    assert (link, "No link with %s found" % user_name)


@step('input text "([^"]*)" to text field with placeholder "([^"]*)"')
def step_impl(step, txt, placeholder):
    links = get_driver().find_elements_by_xpath("//input[@placeholder='%s']" % placeholder)
    if links:
        links[0].send_keys(str(txt))
    else:
        raise ValueError ('Field with %s placeholder not found' % placeholder)


@step('Click button to add "([^"]*)" social media account')
def step_impl(step, name):
    buttons = get_driver().find_elements_by_xpath("//div[@id='accounts-manager']//div[@data-track='%s']" % name)
    if buttons:
        buttons[0].click()
    else:
        raise ValueError ('Button %s social media is not found')


@step('Click span by text "([^"]*)"')
def step_impl(step, span_txt):
    buttons = get_driver().find_elements_by_xpath("//span[text()='%s']" % span_txt)
    if buttons:
        buttons[0].click()
    else:
        raise ValueError('Span with text %s not found' % span_txt)