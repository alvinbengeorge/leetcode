class Solution:
    def simplifyPath1(self, path: str) -> str: # base
        path = [i for i in path.split("/") if i]
        index = 0
        while index < len(path):
            if path[index] == ".." and index != 0:
                del path[index-1:index+1]
                index -= 2
            elif path[index] in ['.', '..']:
                del path[index]
                index -= min(1, len(path))
            index += 1
        return "/"+"/".join(path)
    
    def simplifyPath(self, path: str) -> str: # fast
        path = [i for i in path.split("/") if i][::-1]
        skip = 0
        true_path = []
        for element in path:
            if element in [".", ".."]:
                if element == "..":
                    skip += 1
                continue
            if skip:
                if element != ".": 
                    skip -= 1
                continue
            true_path.append(element)       
        return "/"+"/".join(true_path[::-1])
        
