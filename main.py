def groupAnagrams(strs):
    if len(strs)<1:
        return[[""]]

    hashmap = {}

    for ele in strs:
        ascii_sum = 0
        for char in ele:
            ascii_sum += ord(char)
        if ascii_sum in hashmap:
            hashmap[ascii_sum].append(ele)
        else:
            hashmap[ascii_sum] = [ele]
    return hashmap.values()

groupAnagrams(["eat","tea","tan","ate","nat","bat"])