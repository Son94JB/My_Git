import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Main {
    // 주어진 왼쪽 아래 점, 오른쪽 위 점을 기준으로 사각형을 보드 내에 만든다.
    // 만들어진 사각형들로 나뉜 보드의 구역 개수와 그 크기를 오름차순으로 반환
    static int[][] board;
    static boolean[][] visited;
    static int M, N;
    static int areaCount;
    static List<Integer> areas;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String MNK = br.readLine();
        String[] MNKSplit = MNK.split(" ");

        M = Integer.parseInt(MNKSplit[0]);
        N = Integer.parseInt(MNKSplit[1]);
        int K = Integer.parseInt(MNKSplit[2]);

        board = new int[M][N];
        visited = new boolean[M][N];
        areas = new ArrayList<>();


        for (int i = 0; i < K; i++) {
            String points = br.readLine();
            String[] pointSplit = points.split(" ");
            int x1 = Integer.parseInt(pointSplit[0]);
            int y1 = M - Integer.parseInt(pointSplit[1]);
            int x2 = Integer.parseInt(pointSplit[2]);
            int y2 = M - Integer.parseInt(pointSplit[3]);

            for (int x = x1; x < x2; x++) {
                for (int y = Math.max(y2, 0); y < y1; y++) {
                    board[y][x] = 1; // 사각형은 1로 표시
                }
            }
        }

        areaCount = 0;
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (board[i][j] == 0 && !visited[i][j]) {
                    areas.add(dfs(i, j));
                    areaCount++;
                }
            }
        }

        Collections.sort(areas);
        System.out.println(areaCount);
        for (int area : areas) {
            System.out.print(area + " ");
        }
    }

    static int dfs(int x, int y) {
        if (x < 0 || x >= M || y < 0 || y >= N || board[x][y] == 1 || visited[x][y]) {
            return 0;
        }

        visited[x][y] = true;
        int size = 1;

        size += dfs(x+1, y);
        size += dfs(x, y+1);
        size += dfs(x-1, y);
        size += dfs(x, y-1);

        return size;
    }

}
