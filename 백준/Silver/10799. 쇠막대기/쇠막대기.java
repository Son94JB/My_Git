import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String stickAndLaser = br.readLine();

        // 괄호의 연결된 쌍은 레이저를 뜻하고 모든 ‘( ) ’는 반드시 레이저를 표현한다.
        // 나머지는 쇠막대기를 뜻하는데 쇠막대기는 항상 '('로 시작하고 ')'로 끝난다.
        int totalSticks = 0;
        int currentSticks = 0;
        for (int i = 0; i < stickAndLaser.length(); i++) {
            char ch = stickAndLaser.charAt(i);

            if (ch == '(') { // 막대기의 시작
                currentSticks++; // 열린 막대기 수 증가
            } else { // ch == ')'
                currentSticks--; // 열린 막대기 수 감소
                // 만약 이전 문자가 '('라면 레이저를 의미
                if (stickAndLaser.charAt(i - 1) == '(') {
                    totalSticks += currentSticks; // 현재 열린 막대기 수 만큼 잘림
                } else {
                    totalSticks++; // 막대기의 끝을 의미
                }
            }
        }

        System.out.println(totalSticks); // 최종 잘린 막대기 수 출력

    }

}
