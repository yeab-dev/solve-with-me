from typing import List
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        match_map = {}
        no_losses = []
        lost_only_one = []
        for match in matches:
            winner_score = match_map.get(match[0], [0,0])
            winner_score[0] += 1
            match_map[match[0]] = winner_score

            looser_score = match_map.get(match[1], [0,0])
            looser_score[1] += 1
            match_map[match[1]] = looser_score
        for player, score in match_map.items():
            if score[1] == 0:
                no_losses.append(player)
            if score[1] == 1:
                lost_only_one.append(player)
        
        return [no_losses, lost_only_one]

