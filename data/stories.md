##greetandbye
* greet
   - utter_greet
> check_greet

##asking health
* health
    - utter_health
> check_health

##utteringbye
> check_goodbye
* goodbye
  - utter_goodbye

##admissionmcom
> check_greet
* new_admission{"stream":"mcom"}
   - slot{"stream":"mcom"}
   - admission_mcom
> check_goodbye

##admissionbcom
> check_greet
* new_admission{"stream":"bcom"}
   - slot{"stream":"bcom"}
   - admission_bcom
> check_goodbye

##feesmcs
* inform_fees{"stream":"mcs"}
   - slot{"stream":"mcs"}
   - fees_mcs

##admissionmba
* greet
   - utter_greet

* new_admission{"stream":"mba"}
   - slot{"stream":"mba"}
   - admission_mba
* goodbye
  - utter_goodbye

##admissionmcs
* greet
   - utter_greet

* new_admission{"stream":"msc comp sci"}
   - slot{"stream":"msc comp sci"}
   - admission_mcs

* goodbye
  - utter_goodbye

##admissionbcs
* greet
   - utter_greet

* new_admission{"stream":"bcs"}
   - slot{"stream":"bcs"}
   - admission_bcs
* goodbye
  - utter_goodbye

##introduction
* intro
   - utter_intro

##admissionbba
> check_greet
* new_admission{"stream":"bba"}
   - slot{"stream":"bba"}
   - admission_bba
> check_goodbye

##collegetimingsmba
* greet
   - utter_greet

* college_timings{"stream":"mba"}
   - slot{"stream":"mba"}
   - timing_mba
* goodbye
  - utter_goodbye

##greetandbye
* greet
   - utter_greet

* goodbye
  - utter_goodbye

##entrancexammba
* greet
   - utter_greet

* entrance_exam{"stream":"mba"}
   - slot{"stream":"mba"}
   - utter_entrance_exam

##entranceexammcs
* greet
   - utter_greet

* entrance_exam{"stream":"msc comp sci"}
   - slot{"stream":"msc comp sci"}
   - utter_entrance_exam

##questionpaperentrancemba
> check_greet
> check_health
* question_paper_entrance{"stream":"mba"}
   - slot{"stream":"mba"}
   - utter_question_paper_entrance

##questionpapermcs
* greet
   - utter_greet

* question_paper_entrance{"stream":"msc comp sci"}
   - slot{"stream":"msc comp sci"}
   - utter_question_paper_entrance

##timingsmcs
> check_greet
* college_timings{"stream":"msc comp sci"}
   - slot{"stream":"msc comp sci"}
   - timing_bcs

##timingsbcs
> check_greet
> check_health 
* college_timings{"stream":"bcs"}
   - slot{"stream":"bcs"}
   - timing_bcs
* goodbye
   - utter_goodbye

##placementmba
> check_greet
> check_health
* inform_placements{"stream":"mba"}
   - slot{"stream":"mba"}
   - placement_mba
> check_goodbye

#placementbba
> check_greet
> check_health
* inform_placements{"stream":"bba"}
   - slot{"stream":"bba"}
   - placement_bba
> check_goodbye

#collegetimingmcom
> check_greet
* college_timings{"stream":"mcom"}
   - slot{"stream":"mcom"}
   - timing_mcom
> check_goodbye

#placementbcom
> check_greet
* inform_placements{"stream":"bcom"}
   - slot{"stream":"bcom"}
   - placement_bcom
> check_goodbye

#feesbcs
* greet
   - utter_greet
* inform_fees{"stream":"bcs"}
    - slot{"stream":"bcs"}
    - fees_bcs

#feesmcom
> check_greet
* inform_fees{"stream":"mcom"}
   - slot{"stream":"mcom"}
   - fees_mcom
> check_goodbye

#feesbba
> check_greet
* inform_fees{"stream":"bba"}
   - slot{"stream":"bba"}
   - fees_bba
> check_goodbye


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

## Generated Story -7434479349005267948
* greet
    - utter_greet
* inform_placements{"stream": "bba"}
    - slot{"stream": "bba"}
    - placement_bba
    - slot{"stream": "bba"}
* health
    - utter_health
* new_admission{"stream": "bcs"}
    - slot{"stream": "bcs"}
    - admission_bcs
    - slot{"stream": "bcs"}
* intro
    - utter_intro
* goodbye

## Generated Story 2935618311382803927
* greet
    - utter_greet
* inform_placements{"stream": "bcom"}
    - slot{"stream": "bcom"}
    - placement_bba
    - slot{"stream": "bcom"}
* affirm
    - utter_affirm
* goodbye
    - utter_goodbye

## Generated Story 9168335032264784714
* greet
    - utter_greet
* question_paper_entrance{"stream": "mcs"}
    - slot{"stream": "mcs"}
    - utter_question_paper_entrance
* goodbye
    - utter_goodbye

## Generated Story -6490790533404118598
* greet
    - utter_greet
* inform_placements{"stream": "mcs"}
    - slot{"stream": "mcs"}
    - placement_mcs
    - slot{"stream": "mcs"}
* goodbye
    - utter_goodbye

## Generated Story -8723046171941698091
* greet
    - utter_greet
* new_admission
    - utter_ask_stream
* new_admission{"stream": "mcs"}
    - slot{"stream": "mcs"}
    - admission_mcs
    - slot{"stream": "mcs"}
## Generated Story -8836141679213534233
* question_paper_entrance{"stream": "bcom"}
    - slot{"stream": "bcom"}
    - utter_question_paper_entrance
* goodbye
    - utter_goodbye

## Generated Story 6270859938020352127
* greet
    - utter_greet
* abusive
    - utter_abusive

## Generated Story 2243100202878868943
* greet
    - utter_greet
* inform_fees
    - utter_ask_stream
* inform_fees{"stream": "bba"}
    - slot{"stream": "bba"}
    - fees_bba
    - slot{"stream": "bba"}
* affirm
    - utter_affirm
* goodbye
    - utter_goodbye

## Generated Story -9172724314684723113
* affirm
    - utter_affirm
* affirm
    - utter_affirm

## Generated Story 5964143712098706641
* greet
    - utter_greet
* inform_fees{"stream": "mcom"}
    - slot{"stream": "mcom"}
    - fees_mcom
    - slot{"stream": "mcom"}
* goodbye

## Generated Story 8264954215667197787
* greet
    - utter_greet
* college_timings{"stream": "bcom"}
    - slot{"stream": "bcom"}
    - timing_bcom
    - slot{"stream": "bcom"}
* affirm
    - utter_affirm

## Generated Story -4332156959491531144
* out_of_scope
    - action_default_fallback
    - rewind
* goodbye
    - utter_goodbye

## Generated Story -3281951239169809501
* college_timings{"stream": "mcom"}
    - slot{"stream": "mcom"}
    - timing_mcom
    - slot{"stream": "mcom"}

## Generated Story 5413319973058468329
* greet
    - utter_greet
* new_admission{"stream": "mcs"}
    - slot{"stream": "mcs"}
    - admission_mcs
    - slot{"stream": "mcs"}
* goodbye
    - utter_goodbye

## Generated Story -3995859190212287983
* college_timings{"stream": "bcs"}
    - slot{"stream": "bcs"}
    - timing_bcs
    - slot{"stream": "bcs"}

## Generated Story -607499203877491832
* greet
    - utter_greet
* inform_placements{"stream": "mcs"}
    - slot{"stream": "mcs"}
    - placement_mcs
    - slot{"stream": "mcs"}
* goodbye
    - utter_goodbye

## Generated Story -628896083333757503
* inform_fees{"stream": "mcs"}
    - slot{"stream": "mcs"}
    - fees_mcs
    - slot{"stream": "mcs"}
* goodbye
    - utter_goodbye

## Generated Story -66006225975635926
* college_timings{"stream": "mcs"}
    - slot{"stream": "mcs"}
    - timing_mcs
    - slot{"stream": "mcs"}

## Generated Story 1746085200011047409
* events
    - utter_events
* affirm
    - utter_affirm

## Generated Story -5678286936604690379
* out_of_scope
    - action_default_fallback
    - rewind

## Generated Story -8216542703604331321
* events
    - utter_events
* goodbye
    - utter_goodbye

## Generated Story -1396273576188668801
* greet
    - utter_greet
* health
    - utter_health
* new_admission{"stream": "bba"}
    - slot{"stream": "bba"}
    - admission_bba
    - slot{"stream": "bba"}
    - reset_slot
    - slot{"stream": null}
* new_admission{"stream": "bcom"}
    - slot{"stream": "bcom"}
    - admission_bcom
    - slot{"stream": "bcom"}
* inform_placements{"stream": "bcom"}
    - slot{"stream": "bcom"}
    - placement_bcom
    - slot{"stream": "bcom"}
    - reset_slot
    - slot{"stream": null}
* inform_placements{"stream": "mcom"}
    - slot{"stream": "mcom"}
    - placement_mcom
    - slot{"stream": "mcom"}
    - reset_slot
    - slot{"stream": null}
* inform_fees{"stream": "mcs"}
    - slot{"stream": "mcs"}
    - fees_mcs
    - slot{"stream": "mcs"}
    - reset_slot
    - slot{"stream": null}
* goodbye
    - utter_goodbye

