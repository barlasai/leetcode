class Solution {
    public void backtrack(List<String> ans, int n, int k, StringBuilder sb, int len, boolean a, boolean b, boolean c) {
        if (ans.size() >= k) return;
        if (len >= n) {
            ans.add(sb.toString());
            return;
        }
        if (!a) {
            sb.append('a');
            backtrack(ans, n, k, sb, len + 1, true, false, false);
            sb.deleteCharAt(sb.length() - 1);
        }
        if (!b) {
            sb.append('b');
            backtrack(ans, n, k, sb, len + 1, false, true, false);
            sb.deleteCharAt(sb.length() - 1);
        }
        if (!c) {
            sb.append('c');
            backtrack(ans, n, k, sb, len + 1, false, false, true);
            sb.deleteCharAt(sb.length() - 1);
        }
    }

    public String getHappyString(int n, int k) {
        List<String> ans = new ArrayList<>();
        backtrack(ans, n, k, new StringBuilder(), 0, false, false, false);
        return ans.size() >= k ? ans.get(k - 1) : "";
    }
}