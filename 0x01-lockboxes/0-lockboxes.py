#!/usr/bin/python3
'''Lock Boxes Algorithm'''


def canUnlockAll(boxes):
    '''Implement of Lock box Algo.'''
    unlocked = [0]
    for b_id, bx in enumerate(boxes):
        if not bx:
            continue
        for key in bx:
            if key < len(boxes) and key not in unlocked and key != b_id:
                unlocked.append(key)
    if len(unlocked) == len(boxes):
            return True
    return False
