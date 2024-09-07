import java.io.*;
import java.util.*;

public class Main {
    // N X M 의 그래프가 주어진다. 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 곳이다.
    // 바이러스가 퍼지지 않도록 벽을 3개 세울 때, 생기는 빈 칸(안전구역)의 크기를 구하라.
    // 벽은 3개 모두 사용해야하고 바이러스는 인접한 상하좌우 칸으로 퍼진다.
    static int N, M;
    static int MAX_WALL = 3;
    static int[][] lab;
    static int maxSafeArea;
    static List<int[]> emptySpaces = new ArrayList<>();
    static List<int[]> virusPositions = new ArrayList<>();
    static final int[] dx = {0, 0, 1, -1};
    static final int[] dy = {1, -1, 0, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String NM = br.readLine();

        N = Integer.parseInt(NM.split(" ")[0]);
        M = Integer.parseInt(NM.split(" ")[1]);

        lab = new int[N][M];

        // 연구실 입력받기
        for (int i = 0; i < N; i++) {
            String[] input = br.readLine().split(" ");
            for (int j = 0; j < M; j++) {
                lab[i][j] = Integer.parseInt(input[j]);
                if (lab[i][j] == 0) {
                    emptySpaces.add(new int[]{i, j});
                } else if (lab[i][j] == 2) {
                    virusPositions.add(new int[]{i, j});
                }
            }
        }

        // 벽을 설치하고 안전구역 계산
        placeWalls(0, 0);
        System.out.println(maxSafeArea);
    }

    static void placeWalls(int count, int start) {
        if (count == MAX_WALL) {
            // 벽 설치 후 안전구역 크기 계산
            int safeArea = calculateSafeArea();
            maxSafeArea = Math.max(maxSafeArea, safeArea);
            return;
        }

        for (int i = start; i < emptySpaces.size(); i++) {
            int[] wallPosition = emptySpaces.get(i);
            int y = wallPosition[0];
            int x = wallPosition[1];
            lab[y][x] = 1; // 벽 세우기
            placeWalls(count + 1, i + 1);
            lab[y][x] = 0; // 벽 제거
        }
    }

    static int calculateSafeArea() {
        // 바이러스가 퍼진 연구소 상태를 복사
        int[][] tempLab = new int[N][M];
        for (int i = 0; i < N; i++) {
            tempLab[i] = lab[i].clone();
        }

        // 바이러스 퍼지기
        for (int[] virus : virusPositions) {
            spreadVirus(tempLab, virus[0], virus[1]);
        }

        int safeAreaCount = 0;

        // 안전구역의 개수 세기
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (tempLab[i][j] == 0) {
                    safeAreaCount++;
                }
            }
        }
        return safeAreaCount;
    }

    static void spreadVirus(int[][] lab, int y, int x) {
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{y, x});

        while (!queue.isEmpty()) {
            int[] pos = queue.poll();
            int currY = pos[0];
            int currX = pos[1];

            for (int d = 0; d < 4; d++) {
                int newY = currY + dy[d];
                int newX = currX + dx[d];

                if (newY >= 0 && newY < N && newX >= 0 && newX < M && lab[newY][newX] == 0) {
                    lab[newY][newX] = 2; // 바이러스를 퍼뜨림
                    queue.offer(new int[]{newY, newX});
                }
            }
        }
    }
}
