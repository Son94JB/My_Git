    import java.io.*;

    public class Main {
        // 규칙을 유추해서 정수 N이 주어질 때 별을 찍어라
        static int N;

        public static void main(String[] args) throws IOException {

            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

            String n = br.readLine();
            N = Integer.parseInt(n);

            for (int i = 1; i <= N; i++) {
                for (int j = N; j > i; j--) {
                    System.out.print(" ");
                }
                for (int j = 1; j <= (2 * i - 1); j++) {
                    System.out.print("*");
                }
                System.out.println();
            }



            for (int i = N - 1; i >= 1; i--) {
                for (int j = N; j > i; j--) {
                    System.out.print(" ");
                }
                for (int j = 1; j <= (2 * i - 1); j++) {
                    System.out.print("*");
                }
                System.out.println();
            }
        }

    }