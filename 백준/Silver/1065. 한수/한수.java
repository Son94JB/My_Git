import java.io.*;

public class Main {
    // 자연수 N(1 <= N <= 1000)이 주어진다. 1 ~ N 까지의 수 중 각 자리의 수가 등차수열을 이루는 수의 개수를 구하라.

    static int N;
    static int count;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        count = 0;

        // 어차피 100 미만의 자연수는 모두 한수이다.
        // 그 이후는 자리수를 비교해서 차가 같은 것을 카운트 해준다.
        for (int i = 1; i <= N; i++) {
            if (i <= 99) count++;
            else {
                int a = i/100;  // 100의 자리
                int b = (i-a*100)/10;  // 10의 자리
                int c = i-a*100-b*10;  // 1의 자리
                
                if ((a-b) == (b-c)) {
                    count++;
                }
            }
        }

        System.out.println(count);
    }

}
