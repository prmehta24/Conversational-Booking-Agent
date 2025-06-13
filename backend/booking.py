import re
from playwright.sync_api import Page, expect

def book_meeting(page: Page, name: str, email: str, date: str, time: str):  
    # Navigate to the booking page
    booking_url = "https://calendly.com/aadhrik-myaifrontdesk/30min"
    # update url with date.
    page.goto(booking_url)

    #select the time by finding button with specific time and clicking it.  
    time_button_selector = f"button:has-text('{time}')"
    page.click(time_button_selector)        
    # Fill in the form fields
    page.fill("#name", name)
    page.fill("#email", email)
    # Submit the form by clicking span with text "Schedule Event"
    page.click("span:has-text('Schedule Event')")

    # Wait for next page to load and confirm with text on page "You are scheduled"  
    expect(page.getByText('You are scheduled')).toBeVisible()

    # Verify the confirmation message contains the expected text
    confirmation_text = page.getByText('You are scheduled').text_content()
    assert re.search(r"You are scheduled", confirmation_text) is not None, "Confirmation message not found"