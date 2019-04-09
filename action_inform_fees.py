from rasa_core.sdk import Action
from rasa_core.sdk.events import Slotset
class InformFees(Action):
	def name(self):
		return 'inform_fees'
	def run(self,dispatcher,tracker,domain):
        streams=tracker.get_slot('stream')
            streams=streams.lower()
             if "streams" == "msc comp sci" or " mcs" or " msc computer science":
                reponse=dispatcher.utter_message(""" The fees for msc computer science is 55,0000 per year for open category"""")
        return [SlotSet("stream","streams")]

