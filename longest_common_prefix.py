def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        def allHavePrefix(str_lst, l, h):
            common_subs = [x[l:h+1] for x in str_lst]
            return len(set(common_subs)) == 1

        if len(strs) == 0:
            return ""

        min_str = min(strs, key = len)
        min_str_len = len(min_str)
        # Binary search the length of the min string across all strings
        low = 0
        high = min_str_len
        prefix = ""
        x = 0
        while low <= high:

            # If all on the left side contain substring
            mid = low + (high - low)/2
            if allHavePrefix(strs, low, mid):
                # search right side only
                prefix+= min_str[low:(mid+1)]
                low = mid + 1
            else:
                # Else search left side
                high = mid - 1


        return prefix

print "-------", longestCommonPrefix(["abc", "abcdef", "abcd"])
