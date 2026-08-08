class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # this step i missed previously which to check if the length of the strings are equal
        if len(s)!=len(t):
            return False
        # this is the 1st approach which compares two hashmaps and the no of occurance of each character
        hashMapS={}
        hashMapT={}
        for i in range(len(s)):
            hashMapS[s[i]]=hashMapS.get(s[i],0)+1
            hashMapT[t[i]]=hashMapT.get(t[i],0)+1
        return hashMapS==hashMapT
# another approach better for this problem as it says only lower case a-z is allowed so we take a fixed 26 length of array
    def isAnagramArray(self, s: str, t: str) -> bool:
        hashTable=[0]*26
        for i in range(len(s)):
            hashTable[ord(s[i])-ord('a')]+=1
            hashTable[ord(t[i])-ord('a')]-=1
        for count in hashTable:
            if count!=0:
                return False
        return True

