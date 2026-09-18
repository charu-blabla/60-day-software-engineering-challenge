class Solution {
public:
    int evalRPN(vector<string>& tokens) {

        stack<int> operands;
        for (string i : tokens){
            if (i == "+" || i == "-" || i == "*" || i == "/"){
                int a = operands.top();
                operands.pop();
                int b = operands.top();
                operands.pop();
                if (i == "+")
                    operands.push(a+b);
                else if (i == "-")
                    operands.push(b-a);
                else if (i == "*")
                    operands.push(a*b);
                else
                    operands.push(b/a);

            }
            else{
                operands.push(stoi(i));
            }
        }
        return operands.top();
        
    }
};
