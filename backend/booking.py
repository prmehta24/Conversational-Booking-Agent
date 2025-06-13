import re
from playwright.sync_api import sync_playwright, Page, expect
import time as t

def book_meeting(page: Page, name: str, email: str, date: str, time: str):  
    # Navigate to the booking page
    booking_url = "https://calendly.com/aadhrik-myaifrontdesk/30min"
    # update url with date.
    month = date[:-3] # Extracting year and month.
    booking_url += f"?date={date}&month={month}"
    page.goto(booking_url)
    #select the time by finding button with specific time and clicking it.  
    time_button_selector = f"button:has-text('{time}')"
    #if no time, then return error
    page.click(time_button_selector)     
    # Wait for change then click the button with text "Next"
    ariaLabelValue = f"Next {time}"
    print(ariaLabelValue)
    nextButtonLocator = page.get_by_test_id(ariaLabelValue)
    expect(nextButtonLocator).to_be_visible()
    print(nextButtonLocator)
    nextButtonLocator.click()
    # Fill in the form fields
    page.fill("#full_name_input", name)
    page.fill("#email_input", email)

    # Submit the form by clicking span with text "Schedule Event"
    #page.click("span:has-text('Schedule Event')")

    # # Wait for next page to load and confirm with text on page "You are scheduled"  
    
    expect(page.get_by_text('You are scheduled')).to_be_visible()

    # # Verify the confirmation message contains the expected text
    # confirmation_text = page.getByText('You are scheduled').text_content()
    # assert re.search(r"You are scheduled", confirmation_text) is not None, "Confirmation message not found"

p = sync_playwright().start()
p.selectors.set_test_id_attribute("aria-label")
browser = p.chromium.launch(headless=False)
page = browser.new_page()
book_meeting(page, "John Doe", "jdoe@gmail.com","2025-08-06","9:30am")
