class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();

        for(String s : tokens){
            if(!s.equals("+") && !s.equals("-") && !s.equals("*") && !s.equals("/")){
                stack.push(Integer.parseInt(s));
            }
            else{
                // note first poped element would be b because if order is 3,6,- and we wrote first poped element as a and second one as b then order will be 6-3 but it should be 3-6
                int b = stack.pop();  
                int a = stack.pop();

                if(s.equals("+")){
                    stack.push(a+b);
                }
                else if(s.equals("-")){
                    stack.push(a-b);
                }
                else if(s.equals("/")){
                    stack.push(a/b);
                }
                else{
                    stack.push(a*b);
                }
            }
        }

        return stack.pop();
    }
}