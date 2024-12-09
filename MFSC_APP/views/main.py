from typing import TypedDict
from .root import Root
from .home_view import HomeViews
from .rule_create_views import RuleCreateViews
from .clientxrule_view import ClientXRuleViews

class Frames(TypedDict):
    rule: RuleCreateViews
    home: HomeViews


class View:
    def __init__(self):
        self.root = Root()
        self.frames: Frames = {}  # type: ignore

        self._add_frame(RuleCreateViews, "Rule Create")
        self._add_frame(HomeViews, "Home Page")
        self._add_frame(ClientXRuleViews,"ClientxRule")
        

    def _add_frame(self, Frame, name: str) -> None:
        self.frames[name] = Frame(self.root)
        self.frames[name].grid(row=0, column=0, sticky="nsew")

    def switch(self, name: str) -> None:
        frame = self.frames[name]
        frame.tkraise()

    def start_mainloop(self) -> None:
        self.root.mainloop()