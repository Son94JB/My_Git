    import java.io.*;

    public class Main {
        // 9*9 행렬이 주어질 때, 해당 행렬의 최대값과 그 위치를 출력

        public static void main(String[] args) throws IOException {

            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

            int[][] matrix = new int[9][9];
            int maxValue = 0;
            int x = 0;
            int y = 0;

            // 첫 번째 행렬 입력
            for (int i = 0; i < 9; i++) {
                String line = br.readLine();
                String[] parts = line.split(" ");
                for (int j = 0; j < 9; j++) {
                    matrix[i][j] = Integer.parseInt(parts[j]);
                }
            }

            for (int i = 0; i < 9; i++) {
                for (int j = 0; j < 9; j++) {
                    if (maxValue <= matrix[i][j]) {
                        maxValue = matrix[i][j];
                        y = i;
                        x = j;
                    }
                }
            }
            System.out.println(maxValue);
            System.out.print(y + 1);
            System.out.print(" ");
            System.out.print(x + 1);

        }

    }