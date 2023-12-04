#!/usr/bin/python3
def element_at(lists, idx):
    if idx < 0 or idx > len(lists):
        return None
    return lists[idx]

