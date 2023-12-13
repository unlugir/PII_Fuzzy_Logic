input_lvs = {
    "Walk" : [
        {
            "X": (0, 10.1, 0.01),
            "name" : "Distance",
            "terms":{
                "quick" : ("trapmf", 0,0,0.4, 1),
                "short" : ("trapmf", 0.5,1,1,2),
                "medium" : ("trimf", 1.5, 3, 5),
                "long" : ("trapmf", 4,5,9,10),
            }
        },
        {
            "X": (0, 200.1, 0.1),
            "name": "Height Gain",
            "terms": {
                "none": ("trapmf", 0, 0, 10, 20),
                "some": ("trapmf", 15, 20, 40, 40),
                "hard": ("trimf", 30, 70, 100),
                "extreme": ("trapmf", 50, 100, 150, 200),
            }
        },
        {
            "X": (0, 10.1, 0.01),
            "name": "RoadQuality",
            "terms": {
                "very bad": ("trapmf", 0, 0, 0.5, 1),
                "bad": ("trapmf", 0.5, 2, 3, 5),
                "medium": ("trimf", 4, 5, 7,),
                "good": ("trapmf", 6, 7, 10, 10),
            }
        }
             ],
    "Ride" : [
        {
            "X": (0, 100.1, 0.01),
            "name" : "Distance",
            "terms":{
                "quick" : ("trapmf", 0,0,4, 10),
                "short" : ("trapmf", 5,10,10,20),
                "medium" : ("trimf", 15, 30, 50),
                "long" : ("trapmf", 40,50,90,100),
            }
        },
        {
            "X": (0, 2000.1, 0.1),
            "name": "Height Gain",
            "terms": {
                "none": ("trapmf", 0, 0, 100, 200),
                "some": ("trapmf", 105, 200, 400, 400),
                "hard": ("trimf", 300, 700, 1000),
                "extreme": ("trapmf", 500, 1000, 1500, 2000),
            }
        },
        {
            "X": (0, 10.1, 0.01),
            "name": "RoadQuality",
            "terms": {
                "very bad": ("trapmf", 0, 1, 2, 3),
                "bad": ("trapmf", 2, 4, 5, 7),
                "medium": ("trimf", 6, 7, 8,),
                "good": ("trapmf", 8, 9, 10, 10),
            }
        }
             ],

}

output_lv = {
    "Walk":{
        'X': (0, 10.1, 0.1),
        'name': 'Attractive level',
        'terms': {
            'none to very little': ('trapmf', 0, 0, 0.5, 1),
            'very low': ('trimf', 0, 2, 3),
            'low': ('trapmf', 2, 3, 4, 5),
            'medium': ('trimf', 4, 5, 6),
            'above medium': ('trimf', 5, 6, 7),
            'high': ('trapmf', 6, 7, 8, 9),
            'extremely high': ('trapmf', 7, 9, 10, 10),
        }
    },
"Ride":{
        'X': (0, 10.1, 0.1),
        'name': 'Attractive level',
        'terms': {
            'none to very little': ('trapmf', 0, 0, 0.5, 1),
            'very low': ('trimf', 0, 2, 3),
            'low': ('trapmf', 2, 3, 4, 5),
            'medium': ('trimf', 4, 5, 6),
            'above medium': ('trimf', 5, 6, 7),
            'high': ('trapmf', 6, 7, 8, 9),
            'extremely high': ('trapmf', 7, 9, 10, 10),
        }
    }
}

rule_base = [
(('quick', 'none', 'very bad'), 'high') ,
(('quick', 'none', 'bad'), 'high') ,
(('quick', 'none', 'medium'), 'high') ,
(('quick', 'none', 'good'), 'extremely high') ,
(('quick', 'some', 'very bad'), 'above medium') ,
(('quick', 'some', 'bad'), 'high') ,
(('quick', 'some', 'medium'), 'high') ,
(('quick', 'some', 'good'), 'extremely high') ,
(('quick', 'hard', 'very bad'), 'above medium') ,
(('quick', 'hard', 'bad'), 'above medium') ,
(('quick', 'hard', 'medium'), 'above medium') ,
(('quick', 'hard', 'good'), 'high') ,
(('quick', 'extreme', 'very bad'), 'low') ,
(('quick', 'extreme', 'bad'), 'medium') ,
(('quick', 'extreme', 'medium'), 'medium') ,
(('quick', 'extreme', 'good'), 'above medium') ,
(('short', 'none', 'very bad'), 'above medium') ,
(('short', 'none', 'bad'), 'high') ,
(('short', 'none', 'medium'), 'high') ,
(('short', 'none', 'good'), 'extremely high') ,
(('short', 'some', 'very bad'), 'above medium') ,
(('short', 'some', 'bad'), 'above medium') ,
(('short', 'some', 'medium'), 'high') ,
(('short', 'some', 'good'), 'high') ,
(('short', 'hard', 'very bad'), 'above medium') ,
(('short', 'hard', 'bad'), 'above medium') ,
(('short', 'hard', 'medium'), 'above medium') ,
(('short', 'hard', 'good'), 'high') ,
(('short', 'extreme', 'very bad'), 'low') ,
(('short', 'extreme', 'bad'), 'low') ,
(('short', 'extreme', 'medium'), 'medium') ,
(('short', 'extreme', 'good'), 'above medium') ,
(('medium', 'none', 'very bad'), 'above medium') ,
(('medium', 'none', 'bad'), 'above medium') ,
(('medium', 'none', 'medium'), 'above medium') ,
(('medium', 'none', 'good'), 'high') ,
(('medium', 'some', 'very bad'), 'medium') ,
(('medium', 'some', 'bad'), 'above medium') ,
(('medium', 'some', 'medium'), 'above medium') ,
(('medium', 'some', 'good'), 'high') ,
(('medium', 'hard', 'very bad'), 'medium') ,
(('medium', 'hard', 'bad'), 'medium') ,
(('medium', 'hard', 'medium'), 'medium') ,
(('medium', 'hard', 'good'), 'above medium') ,
(('medium', 'extreme', 'very bad'), 'low') ,
(('medium', 'extreme', 'bad'), 'low') ,
(('medium', 'extreme', 'medium'), 'low') ,
(('medium', 'extreme', 'good'), 'medium') ,
(('long', 'none', 'very bad'), 'low') ,
(('long', 'none', 'bad'), 'low') ,
(('long', 'none', 'medium'), 'medium') ,
(('long', 'none', 'good'), 'above medium') ,
(('long', 'some', 'very bad'), 'low') ,
(('long', 'some', 'bad'), 'low') ,
(('long', 'some', 'medium'), 'low') ,
(('long', 'some', 'good'), 'medium') ,
(('long', 'hard', 'very bad'), 'very low') ,
(('long', 'hard', 'bad'), 'low') ,
(('long', 'hard', 'medium'), 'low') ,
(('long', 'hard', 'good'), 'medium') ,
(('long', 'extreme', 'very bad'), 'none to very little') ,
(('long', 'extreme', 'bad'), 'none to very little') ,
(('long', 'extreme', 'medium'), 'very low') ,
(('long', 'extreme', 'good'), 'very low') ,
]