from rasa_core.actions.action import Action
from rasa_core.events import Slotset
class AdmissionMcs(Action):
	def name(self):
		return 'admission_mcs'
	def run(self,dispatcher,tracker,domain):
		stream=tracker.get_slot('stream')
		  
