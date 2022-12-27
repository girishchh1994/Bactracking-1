T.C: 2**(n+k) (exponential)
S.C: 2**(n+k) (exponential)
class Solution:
    def helper(self,candidates,target,idx,path):
        #base
        if target == 0:
            self.result.append(path.copy())
            return
        if target <0:
            return
        #logic
        for i in range(idx,len(candidates)):
            #action
            path.append(candidates[i])
            self.helper(candidates,target-candidates[i],i,path)
            path.pop()
            
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        self.result = []
        self.helper(candidates,target,0,[])
        return self.result
        
