mock_places = [
    {"id": 0, "name": "haven"},
    {"id": 1, "name": "buxtehude"},
    {"id": 2, "name": "pirmasens"},
]

mock_classes = [{"id": 0, "name": "berserk"}, {"id": 1, "name": "omen"}]

mock_factions = [{"id": 0, "name": "raven"}, {"id": 1, "name": "daemons"}]

mock_vehicles = [
    {"id": 0, "name": "rover"},
    {"id": 1, "name": "helicopter"},
    {"id": 2, "name": "horse"},
]

mock_monsters = [{"id": 0, "name": "crawler"}]

mock_events = [{"id": 0, "name": "cosmic intervention"}]

mock_weapons = [{"id": 0, "name": "harkon-a12"}, {"id": 1, "name": "fork"}]


mock_categories = [
    {"id": 0, "name": "place", "data": mock_places},
    {"id": 1, "name": "class", "data": mock_classes},
    {"id": 2, "name": "faction", "data": mock_factions},
    {"id": 3, "name": "vehicle", "data": mock_vehicles},
    {"id": 4, "name": "monster", "data": mock_monsters},
    {"id": 5, "name": "event", "data": mock_events},
    {"id": 6, "name": "weapon", "data": mock_weapons},
]

# will be in MongoDB later on
mock_posts = [
    {
        "id": 0,
        "title": "Hurehafe",
        "category": "place",
        "content": {
            "Introduction": [
                {
                    "visible": "true",
                    "text": "Lorem ipsum dolor, sit amet consectetur adipisicing elit.",
                },
                {
                    "visible": "false",
                    "text": "Lorem ipsum dolores, sit amet consectetur adispiercing elitepartner.",
                },
            ],
            "History": [
                {
                    "visible": "true",
                    "text": "apwoidmpwaoidmwapiapdmipwaodmpowaidmpoamipowamidpawipdmaowd",
                },
                {
                    "visible": "false",
                    "text": "adwpidpmwiaidpwadmwpoaidmpowdpoadaiwdomwadpimpodwaidmpoawidpowaimdpowamdpowmowaimdwpamdap",
                },
            ],
        },
    }
]
