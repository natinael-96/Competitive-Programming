class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        teams = len(skill) // 2
        team_arr = [skill[i] + skill[~i] for i in range(teams)]
        chem = sum(skill[i] * skill[~i] for i in range(teams) if team_arr[i] == team_arr[0])
        return chem if all(team_arr[i] == team_arr[0] for i in range(1, teams)) else -1
