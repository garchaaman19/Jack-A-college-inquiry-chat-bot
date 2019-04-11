from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
class AdmissionMcs(Action):
	def name(self):
		return 'admission_mcs'
	def run(self,dispatcher,tracker,domain):
		streams=tracker.get_slot('stream')
		if 'streams' == 'msc comp sci' or 'mcs':
			response=""" The admission for MCS is given on basis of 50% marks of bcs and 50% marks of entrance"""
		dispatcher.utter_message(response)
		return [SlotSet('stream',streams)]

class AdmissionBcs(Action):
	def name(self):
		return 'admission_bcs'
	def run(self,dispatcher,tracker,domain):
		streams=tracker.get_slot('stream')
		if 'streams' == 'bcs' or 'bsc comp sci':
			response=""" The admission for BCS is given on basis of entrance exam conducted by college"""
		dispatcher.utter_message(response)
		return [SlotSet('stream',streams)]

class AdmissionBba(Action):
	def name(self):
		return 'admission_bba'
	def run(self,dispatcher,tracker,domain):
		streams=tracker.get_slot('stream')
		if 'streams' == 'bba':
			response=""" The admission for BAA is given through merit list on basis of 12th Marks """
		dispatcher.utter_message(response)
		return [SlotSet('stream',streams)]

class AdmissionMba(Action):
	def name(self):
		return 'admission_mba'
	def run(self,dispatcher,tracker,domain):
		streams=tracker.get_slot('stream')
		if 'streams' == 'mba':
			response=""" The admission for MBA is given through marks scored in CAT """
		dispatcher.utter_message(response)
		return [SlotSet('stream',streams)]


class AdmissionBcom(Action):
	def name(self):
		return 'admission_bcom'
	def run(self,dispatcher,tracker,domain):
		streams=tracker.get_slot('stream')
		if 'streams.lower ' == 'bcom':
			response=""" The admission for B.COM is given on basis of Merit List of 12th result"""
		dispatcher.utter_message(response)
		return [SlotSet('stream',streams)]

class AdmissionMcom(Action):
	def name(self):
		return 'admission_mcom'
	def run(self,dispatcher,tracker,domain):
		streams=tracker.get_slot('stream')
		if 'streams' == 'mcom':
			response=""" The admission for Mcom is given on basis of 50% marks of bcom and 50% marks of entrance"""
		dispatcher.utter_message(response)
		return [SlotSet('stream',streams)]

#classes for fees related quieries
class FeesInquiryMba(Action):
	def name(self):
		return 'fees_mba'
	def run(self,dispatcher,tracker,domain):
		streams=tracker.get_slot('stream')
		if 'streams' == 'mba':
			response=""" The fees for open category is 2.5 lakhs, For OBC category it is 1.5 lakhs and for SC category it is 25k"""
		dispatcher.utter_message(response)
		return [SlotSet('stream',streams)]

class FeesInquiryMcs(Action):
	def name(self):
		return 'fees_mcs'
	def run(self,dispatcher,tracker,domain):
		streams=tracker.get_slot('stream')
		if 'streams' == 'mcs':
			response=""" The fees for open category is 55k, For OBC category it is 35k and for SC category it is 10k"""
		dispatcher.utter_message(response)
		return [SlotSet('stream',streams)]

class FeesInquiryBcs(Action):
	def name(self):
		return 'fees_bcs'
	def run(self,dispatcher,tracker,domain):
		streams=tracker.get_slot('stream')
		if 'streams' == 'bcs':
			response=""" The fees for open category is 35k, For OBC category it is 20k and for SC category it is 5k"""
		dispatcher.utter_message(response)
		return [SlotSet('stream',streams)]

class FeesInquiryBcom(Action):
	def name(self):
		return 'fees_bcom'
	def run(self,dispatcher,tracker,domain):
		streams=tracker.get_slot('stream')
		if 'streams' == 'bcom':
			response=""" The fees for open category is 20k, For OBC category it is 10k and for SC category it is 5k"""
		dispatcher.utter_message(response)
		return [SlotSet('stream',streams)]

class FeesInquiryMcom(Action):
	def name(self):
		return 'fees_mcom'
	def run(self,dispatcher,tracker,domain):
		streams=tracker.get_slot('stream')
		if 'streams' == 'mcom':
			response=""" The fees for open category is 35k, For OBC category it is 20k and for SC category it is 5k"""
		dispatcher.utter_message(response)
		return [SlotSet('stream',streams)]

class FeesInquiryBba(Action):
	def name(self):
		return 'fees_bba'
	def run(self,dispatcher,tracker,domain):
		streams=tracker.get_slot('stream')
		if 'streams' == 'bba':
			response=""" The fees for open category is 40k, For OBC category it is 20k and for SC category it is 5k"""
		dispatcher.utter_message(response)
		return [SlotSet('stream',streams)]

#classes for placement inquiry of different streams
class PlacementBcom(Action):
	def name(self):
		return 'placement_bcom'
	def run(self,dispatcher,tracker,domain):
		streams=tracker.get_slot('stream')
		if 'streams' == 'bcom':
			response=""" We have a very good record of placing students from the Bcom field,Every year atleast 80% of students get placed"""
		dispatcher.utter_message(response)
		return [SlotSet('stream',streams)]

class PlacementMcom(Action):
	def name(self):
		return 'placement_mcom'
	def run(self,dispatcher,tracker,domain):
		streams=tracker.get_slot('stream')
		if 'streams' == 'mcom':
			response=""" We have a very good record of placing students from the Mcom field,Every year atleast 90% of students get placed in banking,financial,corporate sectors"""
		dispatcher.utter_message(response)
		return [SlotSet('stream',streams)]

class PlacementMba(Action):
	def name(self):
		return 'placement_mba'
	def run(self,dispatcher,tracker,domain):
		streams=tracker.get_slot('stream')
		if 'streams' == 'mba':
			response=""" Our recruiters are google,amazon,IBM,Apple,Infosys,Capgemini,Fizerv"""
		dispatcher.utter_message(response)
		return [SlotSet('stream',streams)]

class PlacementMcs(Action):
	def name(self):
		return 'placement_mcs'
	def run(self,dispatcher,tracker,domain):
		streams=tracker.get_slot('stream')
		if 'streams' == 'mcs' or 'msc comp sci':
			response="""We have Best Placement in IT sector field ,Last year 95% students got placed ,Our recruiters are Google,Amazon,IBM,Apple,Infosys,Capgemini,Fizerv and many famous start up companies as well"""
		dispatcher.utter_message(response)
		return [SlotSet('stream',streams)]

class PlacementBcs(Action):
	def name(self):
		return 'placement_bcs'
	def run(self,dispatcher,tracker,domain):
		streams=tracker.get_slot('stream')
		if 'streams' == 'bcs' or 'bsc comp sci':
			response=""" Last year 30 out of 55 students got placed in many big MNC's in our college"""
		dispatcher.utter_message(response)
		return [SlotSet('stream',streams)]

class PlacementBba(Action):
	def name(self):
		return 'placement_bba'
	def run(self,dispatcher,tracker,domain):
		streams=tracker.get_slot('stream')
		if 'streams' == 'bba':
			response=""" BBA placements have always been good in our college,Many Management Firms recurit our student every year"""
		dispatcher.utter_message(response)
		return [SlotSet('stream',streams)]


#classes for college timing enquiries

class CollegeTimingMba(Action):
	def name(self):
		return 'timing_mba'
	def run(self,dispatcher,tracker,domain):
		streams=tracker.get_slot('stream')
		if 'streams' == 'mba':
			response=""" The Timings for Mba are from 8AM To 12PM,External Admissions ARE NOT ALLOWED"""
		dispatcher.utter_message(response)
		return [SlotSet('stream',streams)]

class CollegeTimingBba(Action):
	def name(self):
		return 'timing_bba'
	def run(self,dispatcher,tracker,domain):
		streams=tracker.get_slot('stream')
		if 'streams' == 'bba':
			response=""" The Timings for BBA are from 10AM To 1PM """
		dispatcher.utter_message(response)
		return [SlotSet('stream',streams)]

class CollegeTimingMcom(Action):
	def name(self):
		return 'timing_mcom'
	def run(self,dispatcher,tracker,domain):
		streams=tracker.get_slot('stream')
		if 'streams' == 'mcom':
			response=""" The Timings for Mcom are from 9AM To 12PM,External Admissions are also allowed If you are doing JOB """
		dispatcher.utter_message(response)
		return [SlotSet('stream',streams)]

class CollegeTimingBcom(Action):
	def name(self):
		return 'timing_bcom'
	def run(self,dispatcher,tracker,domain):
		streams=tracker.get_slot('stream')
		if 'streams' == 'bcom':
			response=""" The Timings for Bcom are from 11 AM to 2 PM  """
		dispatcher.utter_message(response)
		return [SlotSet('stream',streams)]

class CollegeTimingMcs(Action):
	def name(self):
		return 'timing_mcs'
	def run(self,dispatcher,tracker,domain):
		streams=tracker.get_slot('stream')
		if 'streams' == 'mcs' or 'msc comp sci':
			response=""" The Timings for MCS are from 12PM TO 4PM, and practicals are conducted on every alternate day from 10AM to 12PM """
		dispatcher.utter_message(response)
		return [SlotSet('stream',streams)]

class CollegeTimingBcs(Action):
	def name(self):
		return 'timing_bcs'
	def run(self,dispatcher,tracker,domain):
		streams=tracker.get_slot('stream')
		if 'streams' == 'bcs' or 'bsc comp sci':
			response=""" The Timings for BCS are from 8AM To 12PM and practicals timings are 12.30 PM to 3.30PM """
		dispatcher.utter_message(response)
		return [SlotSet('stream',streams)]
