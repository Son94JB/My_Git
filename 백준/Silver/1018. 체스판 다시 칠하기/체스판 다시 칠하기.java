import java.io.*;

public class Main {
    // 보드를 8*8로 잘랐을 때, 검은색과 흰색이 번갈아 나오도록 하는 색칠 횟수의 최소값
    static char[][] board;
    static int minColor;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String NM = br.readLine();
        String[] NMSplit = NM.split(" ", 2);

        int N = Integer.parseInt(NMSplit[0]);
        int M = Integer.parseInt(NMSplit[1]);

        board = new char[N][M];

        // 보드 생성
        for (int i = 0; i < N; i++) {
            String line = br.readLine();
            board[i] = line.toCharArray(); // 입력받은 문자열을 char 배열로 변환
        }

        minColor = Integer.MAX_VALUE;

        // 8x8 서브 배열을 순회하며 DFS 탐색
        for (int i = 0; i <= N - 8; i++) {
            for (int j = 0; j <= M - 8; j++) {
                int changes = dfs(i, j);
                minColor = Math.min(minColor, changes);
            }
        }

        System.out.println(minColor);
    }

    static int dfs(int startX, int startY) {
        char[][] pattern1 = {
                {'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
                {'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
                {'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
                {'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
                {'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
                {'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
                {'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
                {'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
        };

        char[][] pattern2 = {
                {'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
                {'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
                {'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
                {'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
                {'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
                {'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
                {'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
                {'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
        };
        int changes1 = 0;
        int changes2 = 0;

        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                if (board[startX + i][startY + j] != pattern1[i][j]) {
                    changes1++;
                }
                if (board[startX + i][startY + j] != pattern2[i][j]) {
                    changes2++;
                }
            }
        }

        return Math.min(changes1, changes2);
    }
}
