class Solution {
public:
    bool isValid(string s) {

        stack<int> braces;
        for (int i = 0; i<s.size();i++){
            if (s[i] == '(' || s[i] == '{' || s[i] == '[' ){
                braces.push(s[i]);}

            else{
               if (braces.size() == 0){
                    return false;}
               if( (braces.top() == '(' && s[i] == ')') ||
                    (braces.top() == '{' && s[i] == '}') ||
                    (braces.top() == '[' && s[i] == ']')){
                        braces.pop();}
                else {
                    return false;}
            }
        }
        return braces.size() == 0;
        
    }
};
