from objexplore import explore as obj_explore
import os

EXPLORE_RESPONSES = os.environ.get("EXPLORE_RESPONSES", False)

def explore(obj):
    if EXPLORE_RESPONSES:
        obj_explore(obj)