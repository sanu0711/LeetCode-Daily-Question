class Solution:
    def countSeniors(self, details) -> int:
        seniors = 0
        for d in details:
            age = int(d[11:13])
            if age > 60:
                seniors  = seniors + 1
        return seniors