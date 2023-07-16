class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n = len(req_skills)
        m = len(people)
        dp = {0: []}
        for i, p in enumerate(people):
            his_skills = 0
            for skill in p:
                his_skills |= 1 << req_skills.index(skill)
            for skill_set, need in list(dp.items()):
                with_him = skill_set | his_skills
                if with_him == skill_set:
                    continue
                if with_him not in dp or len(dp[with_him]) > len(need) + 1:
                    dp[with_him] = need + [i]
        return dp[(1 << n) - 1]