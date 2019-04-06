##story1
* greet
   - utter_greet

##story2
* goodbye
  - utter_goodbye

##story3
* new_admission
   - utter_ask_stream

##story4
* greet
   - utter_greet

* new_admission{"stream":"mba"}
   - slot{"stream":"mba"}
   - admission_mcs

* goodbye
  - utter_goodbye

##story5
* greet
   - utter_greet

* new_admission{"stream":"msc computer science"}
   - slot{"stream":"msc computer science"}
   - admission_mcs

* goodbye
  - utter_goodbye

##story6
* greet
   - utter_greet

* new_admission{"stream":"bsc"}
   - slot{"stream":"bsc"}
   - admission_mcs

* goodbye
  - utter_goodbye

##story7
* greet
   - utter_greet

* new_admission{"stream":"msc comp sci"}
   - slot{"stream":"msc comp sci"}
   - admission_mcs

* goodbye
  - utter_goodbye

##story8
* new_admission{"stream":"bsc comp sci"}
   - slot{"stream":"bsc comp sci"}
   - admission_mcs

##story9
* intro
   - utter_intro

##story10
* new_admission{"stream":"bba"}
   - slot{"stream":"bba"}
   - admission_mcs

##story11
* greet
   - utter_greet

* new_admission{"stream":"mca"}
   - slot{"stream":"msa"}
   - admission_mcs

* goodbye
  - utter_goodbye

##story12
* greet
   - utter_greet

* inform_fees{"stream":"msc comp sci"}
   - slot{"stream":"msc comp sci"}
   - inform_fees

* goodbye
  - utter_goodbye

##story13
* greet
   - utter_greet

* inform_fees{"stream":"bsc"}
   - slot{"stream":"bsc"}
   - utter_inform_fees

* goodbye
  - utter_goodbye

##story14
* inform_placements{"stream":"bcom"}
   - slot{"stream":"bcom"}
   - utter_inform_placements

##story15
* inform_placements{"stream":"mba"}
   - slot{"stream":"mba"}
   - utter_inform_placements

##story16
* greet
   - utter_greet	

* inform_placements{"stream":"mcom"}
   - slot{"stream":"mcom"}
   - utter_inform_placements

##story17
* greet
   - utter_greet

* inform_placements{"stream":"bsc"}
   - slot{"stream":"bsc"}
   - utter_inform_placements

##story18
* greet
   - utter_greet

* entrance_exam{"stream":"mba"}
   - slot{"stream":"mba"}
   - utter_entrance_exam

##story19
* greet
   - utter_greet

* entrance_exam{"stream":"msc comp sci"}
   - slot{"stream":"msc comp sci"}
   - utter_entrance_exam


##story20
* greet
   - utter_greet

* entrance_exam{"stream":"mca"}
   - slot{"stream":"mca"}
   - utter_entrance_exam

##story21
* greet
   - utter_greet

* question_paper_entrance{"stream":"mba"}
   - slot{"stream":"mba"}
   - utter_question_paper_entrance

##story22
* greet
   - utter_greet

* question_paper_entrance{"stream":"msc comp sci"}
   - slot{"stream":"msc comp sci"}
   - utter_question_paper_entrance

##story23
* greet
   - utter_greet

* college_timings{"stream":"msc comp sci"}
   - slot{"stream":"msc comp sci"}
   - utter_college_timings

##story24

* greet
   - utter_greet

* college_timings{"stream":"bcs"}
   - slot{"stream":"bcs"}
   - utter_college_timings


