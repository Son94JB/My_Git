    import java.io.*;

    public class Main {
        // 666이 들어가는 n번째 숫자를 출력

        public static void main(String[] args) throws IOException {
            
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            int N = Integer.parseInt(br.readLine());

            int i = 0;
            int number = 665;

            while (i < N) {
                number++;
                String strNumber = Integer.toString(number);
                if (strNumber.contains("666")) {
                    i++;
                }
            }

            System.out.println(number);
            
        }

    }