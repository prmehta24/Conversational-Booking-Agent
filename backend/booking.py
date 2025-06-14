import re
from playwright.sync_api import sync_playwright, Page, expect
import time as t



def book_meeting(name: str, email: str, date: str, time: str):
    response = None  
    try:
        p = sync_playwright().start()
        browser = p.chromium.launch(headless=True) # Set headless=False to debug
        page = browser.new_page()

        # Navigate to the booking page
        response = "The booking URL is unavailable. Please try again later."
        booking_url = "https://calendly.com/aadhrik-myaifrontdesk/30min"
        # update url with date.
        month = date[:-3] # Extracting year and month.
        booking_url += f"?date={date}&month={month}"
        page.goto(booking_url)

        #select the time by finding button with specific time and clicking it.  
        response = "The booking time is unavailable. Please request a different time."
        time_button_selector = f"button:has-text('{time}')"
        expect(time_button_selector).to_be_visible()
        page.click(time_button_selector)

        # Click the button with text "Next"
        response = "The Next button was unavailable. Please try again later."
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

        # # Wait for next page to load and confirm with text on page "You are scheduled"  
        
        expect(page.get_by_text('You are scheduled')).to_be_visible()
        response = "Meeting booked successfully for {} at {} on {}".format(name, time, date)
    except Exception as e:
        print(f"An error occurred: {e}")
        response = "Failed to book meeting. Please check the details and try again."
    finally:
        if p:    
            p.stop()
        print("book_meeting fn result: ",response)
        return response

#book_meeting("John Doe", "jdoetakehometest@gmail.com","2025-06-18","9:30am") #Debugging

