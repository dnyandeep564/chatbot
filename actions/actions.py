# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


 #This is a simple example for a custom action which utters "Hello World!"
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker,FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
import webbrowser
#from rasa_sdk.forms import FormAction



# class ValidateReservationForm(FormValidationAction):
#     def name(self) -> Text:
#         return "validate_reservation_form"

#     @staticmethod
#     # def cuisine_db() -> List[Text]:
#     #     """Database of supported cuisines"""

#     #     return ["caribbean", "chinese", "french"]

#     def validate_time(
#         self,
#         slot_value: Any,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict,
#     ) -> Dict[Text, Any]:
#         """Validate time value."""

#         print(slot_value," *****************************************************************************************")

#         hrs = slot_value[11:13]
#         mins = slot_value[14:16]

#         print(hrs,"  ",mins," *****************************************************************************************")

#         if(type(hrs) == str):
#             hrs2 = int(hrs)
#             mins2 = int(mins)
#             print(hrs,"  ",mins," *****************************************************************************************")

#         else :
#             hrs2 = hrs
#             mins2 = mins
#             print(hrs,"  ",mins," 123*****************************************************************************************")


#         if(hrs2 <22 and hrs2>=19):
#             if(mins<30):
#                 return {"time": str(hrs2) + ":00pm"}
#             else:
#                 return {"time": str(hrs2) + ":30pm"}
#         else:
#             return {"time": None}
       
# class ReservationForm(FormAction):
#     def name(self):
#         return "reservation_form"
    
#     @staticmethod
#     def required_slots(tracker):
#         return ["seats", "section"]

# class ValidateReservationForm(Action):
#     def name(self) -> Text:
#         return "reservation_form"

#     def run(
#         self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
#     ) -> List[Dict[Text, Any]]:
#         required_slots = ["seats", "section", "time"]

#         for slot_name in required_slots:
#             if tracker.slots.get(slot_name) is None:
#                 # The slot is not filled yet. Request the user to fill this slot next.
#                 return [SlotSet("requested_slot", slot_name)]
#             # else:
#             #     k = tracker.slots.get(slot_name)
#             #     print(k," errorr***************************************************************************************")
#             #     if(k == 8 or k == "8"):
#             #         print(k," errorr***************************************************************************************")
#             #         return [SlotSet("requested_slot", slot_name)]

#         # All slots are filled.
#         return [SlotSet("requested_slot", None)]

    # def validate_seats(
    #     self,
    #     value: Text,
    #     dispatcher: CollectingDispatcher,
    #     tracker: Tracker,
    #     domain: Dict
    # ) -> Dict[Text,Any]:

    #     if (value == '8'):
    #         return {"seats": value}
    #     else:
    #         print("error!")
    #         return {"seats": None}

class ActionSubmit(Action):
    def name(self) -> Text:
        return "action_submit"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_show_selection",
                                 Seats=tracker.get_slot("seats"),
                                 Section=tracker.get_slot("section"),
                                 Time=tracker.get_slot("time"),)

#class Actionntables(Action):
#
#     def name(self) -> Text:
#         return "action_ntables"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class Actionntables(Action):

     def name(self) -> Text:
         return "action_ntables"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message(text="Hello World!")

         return []

