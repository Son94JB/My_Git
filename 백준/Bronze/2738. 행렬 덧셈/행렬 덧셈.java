    import java.io.*;
    import java.util.Arrays;

    public class Main {
        // 두 개의 행렬의 합을 구하는 프로그램
        // 행렬 크기 N, M 이 주어지고 아래로 행렬 두 개가 주어진다.

        public static void main(String[] args) throws IOException {

            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

            String firstLine = br.readLine();
            String[] firstLineParts = firstLine.split(" ");
            int N = Integer.parseInt(firstLineParts[0]); // 첫 번째 수
            int M = Integer.parseInt(firstLineParts[1]); // 두 번째 수

            int[][] matrix1 = new int[N][M];
            int[][] matrix2 = new int[N][M];


            // 첫 번째 행렬 입력
            for (int i = 0; i < N; i++) {
                String line = br.readLine();
                String[] parts = line.split(" ");
                for (int j = 0; j < M; j++) {
                    matrix1[i][j] = Integer.parseInt(parts[j]);
                }
            }

            // 두 번째 행렬 입력
            for (int i = 0; i < N; i++) {
                String line = br.readLine();
                String[] parts = line.split(" ");
                for (int j = 0; j < M; j++) {
                    matrix2[i][j] = Integer.parseInt(parts[j]);
                }
            }

            int[][] result = new int[N][M];

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    result[i][j] = matrix1[i][j] + matrix2[i][j];
                }
            }

            printMatrix(result);
        }

        private static void printMatrix(int[][] matrix) {
            for (int[] row : matrix) {
                for (int value : row) {
                    System.out.print(value + " ");
                }
                System.out.println(); // 각 행이 끝날 때 줄 바꿈
            }
        }
    }