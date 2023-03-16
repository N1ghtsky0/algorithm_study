import java.util.*;
import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder answer = new StringBuilder();
        String str = br.readLine();
        Stack<Character> stack = new Stack<>();
        for (int i = 0; i < str.length(); i++) {
            char now = str.charAt(i);
            switch (now) {
                case '+':
                case '-':
                case '*':
                case '/':
                    while (!stack.isEmpty() && priority(stack.peek()) >= priority(now)) answer.append(stack.pop());
                    stack.add(now);
                    break;
                case '(':
                    stack.add(now);
                    break;
                case ')':
                    while (!stack.isEmpty() && stack.peek() != '(') answer.append(stack.pop());
                    stack.pop();
                    break;
                default:
                    answer.append(now);
            }
        }

        while (!stack.isEmpty()) {
            answer.append(stack.pop());
        }
        System.out.println(answer);
    }

    // 연산자 별 우선순위 리턴
    public static int priority(char operator){
        if(operator=='(' || operator==')'){
            return 0;
        } else if (operator == '+' || operator == '-') {
            return 1;
        } else if (operator == '*' || operator == '/') {
            return 2;
        }
        return -1;
    }
}