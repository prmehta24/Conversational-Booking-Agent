from playwright.sync_api import sync_playwright, Page, expect
from dotenv import load_dotenv
import os

load_dotenv()
CALENDLY_BOOKING_URL = os.getenv("CALENDLY_BOOKING_URL")

def book_meeting(name: str, email: str, date: str, time: str):
    response = None  
    try:
        p = sync_playwright().start()
        browser = p.chromium.launch(headless=True) # Set headless=False to debug
        page = browser.new_page()

        # Navigate to the booking page
        response = "The booking URL is unavailable. Please try again later." #TODO: Test how to get this response.
        booking_url = CALENDLY_BOOKING_URL
        # update url with date.
        month = date[:-3] # Extracting year and month.
        booking_url += f"?date={date}&month={month}"
        page.goto(booking_url)

        #select the time by finding button with specific time and clicking it.  
        response = "The booking time is unavailable. Please request a different time."
        p.selectors.set_test_id_attribute("data-start-time")
        time_button_selector = page.get_by_test_id(time)
        expect(time_button_selector).to_be_visible()
        time_button_selector.click()

        # Click the button with text "Next"
        response = None
        ariaLabelValue = f"Next {time}"
        print(ariaLabelValue)
        p.selectors.set_test_id_attribute("aria-label") # to select Next button.
        nextButtonLocator = page.get_by_test_id(ariaLabelValue)
        expect(nextButtonLocator).to_be_visible()
        print(nextButtonLocator)
        nextButtonLocator.click()

        # Fill in the form fields
        page.fill("#full_name_input", name)
        page.fill("#email_input", email)
        p.selectors.set_test_id_attribute("name") # to select textarea 'Please share anything that will help prepare for our meeting.
        extraInfoLocator = page.get_by_test_id('question_0')
        expect(extraInfoLocator).to_be_visible()
        extraInfoLocator.fill("This is a test booking for the take home assignment. Please ignore or delete this booking.")

        # Submit the form by clicking span with text "Schedule Event"
        page.click("span:has-text('Schedule Event')")

        # Wait for next page to load and confirm with text on page "You are scheduled"  
        expect(page.get_by_text('You are scheduled')).to_be_visible()
        response = "Meeting booked successfully for {} at {} on {}".format(name, time, date)
    except Exception as e:
        print(f"An error occurred: {e}")
        if response is None:
            response = "Failed to book meeting. Please try again."
    finally:
        if p:    
            p.stop()
        print("book_meeting fn result: ",response)
        return response

#book_meeting("John Doe", "jdoetakehometest@gmail.com","2025-06-18","9:30am") #Debugging

