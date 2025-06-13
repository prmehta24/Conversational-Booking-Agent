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
    t.sleep(1)

    #select the time by finding button with specific time and clicking it.  
    time_button_selector = f"button:has-text('{time}')"
    #if no time, then return error
    page.click(time_button_selector)  
    t.sleep(5)    
    # Wait for change then click the button with text "Next"
    nextButtonLocator = page.get_by_role("button", name="Next")
    expect(nextButtonLocator).to_be_visible(timeout=10000)
    nextButtonLocator.click()
    t.sleep(1)
    # Fill in the form fields
    page.fill("#full_name_input", name)
    t.sleep(1)
    page.fill("#email_input", email)
    t.sleep(1)
    # Submit the form by clicking span with text "Schedule Event"
    #page.click("span:has-text('Schedule Event')")

    # # Wait for next page to load and confirm with text on page "You are scheduled"  
    # expect(page.getByText('You are scheduled')).toBeVisible()

    # # Verify the confirmation message contains the expected text
    # confirmation_text = page.getByText('You are scheduled').text_content()
    # assert re.search(r"You are scheduled", confirmation_text) is not None, "Confirmation message not found"

p = sync_playwright().start()
browser = p.chromium.launch(headless=False)
page = browser.new_page()
book_meeting(page, "John Doe", "prmehta24@gmail.com","2025-08-06","9:30am")
