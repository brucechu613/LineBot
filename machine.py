from fsm import TocMachine

def create_machine():
    machine = TocMachine(
        states=["user", "fsm", "intro", "flirt", "greet", "reply_flirt","test"],
        transitions=[
            {
                "trigger": "advance",
                "source": "user",
                "dest": "test",
                "conditions": "is_going_to_test",
            },
            {
                "trigger": "advance",
                "source": "user",
                "dest": "fsm",
                "conditions": "is_going_to_fsm",
            },
            {
                "trigger": "advance",
                "source": "user",
                "dest": "intro",
                "conditions": "is_going_to_intro",
            },
            {
                "trigger": "advance",
                "source": "user",
                "dest": "greet",
                "conditions": "is_going_to_greet",
            },
            {
                "trigger": "advance",
                "source": "user",
                "dest": "flirt",
                "conditions": "is_going_to_flirt",
            },
            {
                "trigger": "advance",
                "source": "flirt",
                "dest": "reply_flirt",
                "conditions": "is_going_to_reply_flirt",
            },
            {"trigger": "go_back", "source": ["fsm", "intro", "greet", "reply_flirt","test"], "dest": "user"}
        ],
        initial="user",
        auto_transitions=False,
        show_conditions=True,
    )
    return machine

