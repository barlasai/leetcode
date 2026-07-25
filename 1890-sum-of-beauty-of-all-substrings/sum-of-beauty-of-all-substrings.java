class Solution {    
        /*
        #########################################################################
        #                                                                       #
        #  =============================================                        #
        #                  SIDDARDHA CHILUVERU                                  #
        #  =============================================                        #
        #                                                                       #
        #  Author      : Siddardha Chiluveru                                    #
        #  Description : Solution / Code / Project                              #
        #  Date        : 2026-07-22                                             #
        #                                                                       #
        #########################################################################
        */
    public int beautySum(String s) {
        int ans = 0;
        int n = s.length();
        for (int i = 0; i < n; i++) {
            int[] freq = new int[26]; 
            for (int j = i; j < n; j++) {
                char c = s.charAt(j);
                freq[c - 'a'] += 1;
                int min = 500;
                int max = 0;
                for (int num : freq) 
                    if (num > 0) {
                        min = Math.min(min, num);
                        max = Math.max(max, num);
                    }
                ans += (max - min);
            }
        }
        return ans;
    }
}