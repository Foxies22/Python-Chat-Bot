import random

def unknown():
    response = ['Could you please re-phrase thath?',
                 "......",
                 "Sounds about rightm",
                  "What does that mean?"][random.randrange(4)]
    return response