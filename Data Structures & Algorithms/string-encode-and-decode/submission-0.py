class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_list: list[str] = []

        for string in strs:
            encoded_list.append(f"{len(string)}!{string}")
        
        return "".join(encoded_list)

    def decode(self, s: str) -> List[str]:
        ans: list[str] = []
        cursor = 0

        while cursor < len(s):
            jump = ""

            while s[cursor] != '!':
                jump += s[cursor]
                cursor += 1
            
            jump = int(jump)
            cursor += 1
            ans.append(s[cursor : cursor + jump])
            cursor += jump
        
        return ans

