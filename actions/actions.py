    # This files contains your custom actions which can be used to run
    # custom Python code.
    
    # See this guide on how to implement these action:
    # https://rasa.com/docs/rasa/custom-actions


    # This is a simple example for a custom action which utters "Hello World!"


from typing import Any, Dict, List, Text
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from rasa_sdk.types import DomainDict

def SendEmail(toaddr, subject, message, dispatcher):
    fromaddr = "snikhil6295@gmail.com"  # Replace with your email address
    from_pass = "fjiv qngi caxe rhyx"   # Replace with your email password (consider using app passwords for security)

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr  # Use the provided email address as the recipient
    msg['Subject'] = subject
    body = message
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Create an SMTP session and send the email
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.login(fromaddr, from_pass)
        text = msg.as_string()
        session.sendmail(fromaddr, toaddr, text)
        session.quit()
        dispatcher.utter_message("Thanks for providing the details. We have sent the email.")
    except Exception as e:
        print(f"An Error Occurred while sending email: {str(e)}")

class ActionSubmit(Action):
    def name(self) -> Text:
        return "action_submit"
    
    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict
    ) -> List[Dict[Text, Any]]:
        toaddress = tracker.get_slot("toaddress")
        subject = tracker.get_slot("subject")
        message = tracker.get_slot("message")
        
        if toaddress and subject and message:
            SendEmail(toaddress, subject, message, dispatcher)
        else:
            dispatcher.utter_message("Please provide all required details before sending the email.")
        
        return []


class ActionHelloWorld(Action):
    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Hello World!")
        return []

class ActionAskToaddress(Action):
    def name(self) -> Text:
        return "action_ask_toaddress"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Please enter the email address of the recipient.")
        return []

class ActionAskSubject(Action):
    def name(self) -> Text:
        return "action_ask_subject"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Please enter the subject of the email.")
        return []

class ActionAskMessage(Action):
    def name(self) -> Text:
        return "action_ask_message"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Please enter the message you want to send in the email.")
        return []
