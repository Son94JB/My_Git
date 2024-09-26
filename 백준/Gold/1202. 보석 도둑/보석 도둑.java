import java.io.*;
import java.util.*;

public class Main {
    static int N, K;  // 보석 개수, 가방 개수
    static List<int[]> jewels; // 보석의 무게와 가치를 저장할 리스트
    static List<Integer> bagWeight; // 가방의 최대 무게 리스트

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String NK = br.readLine();

        N = Integer.parseInt(NK.split(" ")[0]);
        K = Integer.parseInt(NK.split(" ")[1]);

        jewels = new ArrayList<>();
        bagWeight = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            String temp = br.readLine();
            int w = Integer.parseInt(temp.split(" ")[0]);
            int v = Integer.parseInt(temp.split(" ")[1]);
            jewels.add(new int[]{w, v}); // 무게와 가치를 배열로 저장
        }

        for (int i = 0; i < K; i++) {
            int weight = Integer.parseInt(br.readLine());
            bagWeight.add(weight); // 가방의 최대 무게 리스트에 추가
        }

        // 보석을 무게에 대해 오름차순 정렬하고, 무게가 같을 경우 가격에 대해 내림차순 정렬
        jewels.sort((a, b) -> {
            if (a[0] == b[0]) {
                return Integer.compare(b[1], a[1]); // 가격 내림차순
            }
            return Integer.compare(a[0], b[0]); // 무게 오름차순
        });

        // 가방을 오름차순 정렬
        Collections.sort(bagWeight);

        // 우선순위 큐 (가격에 대해 내림차순 정렬)
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        long ans = 0;
        int idx = 0;

        for (int bag : bagWeight) {
            // 현재 가방의 무게보다 작은 보석의 가격을 우선순위 큐에 추가
            while (idx < N && jewels.get(idx)[0] <= bag) {
                pq.offer(jewels.get(idx)[1]);
                idx++;
            }

            // 우선순위 큐가 비어있지 않다면, 가장 비싼 보석을 꺼내서 ans에 더함
            if (!pq.isEmpty()) {
                ans += pq.poll();
            }
        }

        System.out.println(ans);
    }
}
