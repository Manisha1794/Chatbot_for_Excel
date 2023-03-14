import pandas as pd
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset, SlotSet, Restarted, UserUtteranceReverted


class CustomActionGetTotalAmount(Action):
    def name(self) -> Text:
        return "custom_action_get_total_amount"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Load the data from the Excel file
        df = pd.read_excel('D:\\Chatbot_for_Excel-master\\test_file.xlsx')

        # Get the slot values from the tracker
        quarter = tracker.get_slot('quarter')
        week_number = tracker.get_slot('week_number')
        date = tracker.get_slot('date')
        amount_debit = tracker.get_slot('amount_debit')
        amount_credit = tracker.get_slot('amount_credit')
        category = tracker.get_slot('category')
        comments = tracker.get_slot('comments')

        # Filter the data by the specified category
        filtered_df = df[df['Category'] == category]

        # Calculate the total amount for the specified category
        total_amount = filtered_df['Amount Debit'].sum() - filtered_df['Amount Credit'].sum()

        dispatcher.utter_message(text=f"The result is {total_amount}")
        return [SlotSet("amount_debit", filtered_df['Amount Debit'].sum()),
        SlotSet("amount_credit", filtered_df['Amount Credit'].sum())]
        print("I was called...")


class ActionDefaultFallback(Action):
    """Default fallback action to be triggered
       if Rasa Core is unsure what to do next"""

    def name(self):
        return "action_default_fallback"

    def run(self, dispatcher, tracker, domain):
        # Retrieve the last user message
        last_message = tracker.latest_message.get('text', '')

        # Check if the last message was a fallback message
        last_intent = tracker.latest_message.get('intent', {}).get('name', '')
        if last_intent == 'nlu_fallback':
            dispatcher.utter_message(template="utter_default_fallback")
            return [UserUtteranceReverted()]

        # If the last message was not a fallback message,
        # set the fallback count slot to 1 and ask the user to repeat
        fallback_count = tracker.get_slot('fallback_count')
        if fallback_count is None:
            fallback_count = 0
        fallback_count += 1
        dispatcher.utter_message(template="utter_ask_repeat")
        return [SlotSet('fallback_count', fallback_count)]