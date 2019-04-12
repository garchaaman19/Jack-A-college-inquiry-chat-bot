##story1
* greet
   - utter_greet
* health
    - utter_health

* goodbye
  - utter_goodbye

##story1
* greet
   - utter_greet
* health
    - utter_health

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
   - admission_mba

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

* new_admission{"stream":"bcs"}
   - slot{"stream":"bcs"}
   - admission_bcs

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
   - admission_bcs

##story9
* intro
   - utter_intro

##story10
* new_admission{"stream":"bba"}
   - slot{"stream":"bba"}
   - admission_bba

##story11
* greet
   - utter_greet

* college_timings{"stream":"mba"}
   - slot{"stream":"mba"}
   - timing_mba

* goodbye
  - utter_goodbye

##story12
* greet
   - utter_greet

* goodbye
  - utter_goodbye

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

* question_paper_entrance{"stream":"mba"}
   - slot{"stream":"mba"}
   - utter_question_paper_entrance

##story21
* greet
   - utter_greet

* question_paper_entrance{"stream":"msc comp sci"}
   - slot{"stream":"msc comp sci"}
   - utter_question_paper_entrance

##story22
* greet
   - utter_greet

* college_timings{"stream":"msc comp sci"}
   - slot{"stream":"msc comp sci"}
   - timing_bcs

##story23

* greet
   - utter_greet

* college_timings{"stream":"bcs"}
   - slot{"stream":"bcs"}
   - timing_bcs



## Generated Story -1760820799534768914
* greet
    - utter_greet
* health
    - utter_health
* new_admission{"stream": "bcom"}
    - slot{"stream": "bcom"}
    - admission_bcom
    - slot{"stream": "bcom"}
* goodbye
    - utter_goodbye

## Generated Story -6198081784127456134
* greet
    - utter_greet
* intro
    - utter_intro
* inform_fees{"stream": "bba"}
    - slot{"stream": "bba"}
    - fees_bba
    - slot{"stream": "bba"}
* affirm
    - utter_affirm
* goodbye
    - utter_goodbye

## Generated Story -7438921667049325324
* inform_fees{"stream": "bsc comp sci"}
    - slot{"stream": "bsc comp sci"}
    - fees_bcs
    - slot{"stream": "bsc comp sci"}
* affirm
    - utter_affirm
* abusive
    - utter_abusive

## Generated Story 841655493324089128
* inform_placements{"stream": "mcom"}
    - slot{"stream": "mcom"}
    - placement_mcom
    - slot{"stream": "mcom"}
* inform_placements{"stream": "bcom"}
    - slot{"stream": "bcom"}
    - placement_bcom
    - slot{"stream": "bcom"}
* affirm
    - utter_affirm
* goodbye
    - utter_goodbye

## Generated Story -6333017207833193266
* greet
    - utter_greet
* college_timings{"stream": "mcom"}
    - slot{"stream": "mcom"}
    - timing_mcom
    - slot{"stream": "mcom"}
* new_admission{"stream": "mcom"}
    - slot{"stream": "mcom"}
    - admission_mcom
    - slot{"stream": "mcom"}
* goodbye
    - utter_goodbye

## Generated Story 3980219643693371352
* inform_placements{"stream": "mcs"}
    - slot{"stream": "mcs"}
    - placement_mcs
    - slot{"stream": "mcs"}
* inform_placements{"stream": "bcs"}
    - slot{"stream": "bcs"}
    - placement_bcs
    - slot{"stream": "bcs"}
* affirm
    - utter_affirm
* goodbye
    - utter_goodbye

