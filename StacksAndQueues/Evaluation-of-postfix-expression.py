class Solution
{
    public static int performOp(char ch,int a,int b){
        int ans=0;
        switch(ch){
            case '*':
                ans=a*b;
                break;
            case '+':
                ans=a+b;
                break;
            case '-':
                ans=b-a;
                break;
            case '/':
                ans=b/a;
                break;
        }
        return ans;
    }
    //Function to evaluate a postfix expression.
    public static int evaluatePostFix(String S)
    {
        // Your code here
        Stack<Integer> stack=new Stack<>();
        for(char ch:S.toCharArray()){
            if(ch=='*' || ch=='+' || ch=='-' || ch=='/'){
                int last=stack.pop();
                int prevlast=stack.pop();
                int ans=performOp(ch,last,prevlast);
                stack.push(ans);
            }
            else{
                stack.push(Character.getNumericValue(ch));
            }
        }
        return stack.pop();
    }
}