from typing import *
class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        max_duration = releaseTimes[0]
        max_key = keysPressed[0]
        for i in range(1, len(releaseTimes)):
            duration = releaseTimes[i] - releaseTimes[i-1]
            if duration > max_duration:
                max_duration = duration
                max_key = keysPressed[i]
            elif duration == max_duration:
                if keysPressed[i] > max_key:
                    max_key = keysPressed[i]
        return max_key