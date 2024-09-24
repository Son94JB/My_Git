import java.io.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;

public class Main {
    // 듣지 못한 사람의 수와 보지 못한 사람의 수가 주어진다.
    // 그리고 듣지 못한 사람의 이름과 보지 못한 사람의 이름이 주어진다.
    // 이 때, 듣지도 보지도 못한 사람의 수와 그 이름들을 알파벳 순으로 나열하라.

    static int N, M;  // 듣지 못한 사람의 수, 보지 못한 사람의 수
    static List<String> neverHeard;
    static HashSet<String> neverSeen;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String NM = br.readLine();

        N = Integer.parseInt(NM.split(" ")[0]);
        M = Integer.parseInt(NM.split(" ")[1]);

        neverHeard = new ArrayList<>();
        neverSeen = new HashSet<>();

        for (int i = 0; i < N; i++) {
            neverHeard.add(br.readLine());
        }

        for (int i = 0; i < M; i++) {
            neverSeen.add(br.readLine());
        }

        List<String> neverHeardAndSeen = new ArrayList<>();

        for (String name : neverHeard) {
            if (neverSeen.contains(name)) {
                neverHeardAndSeen.add(name);
            }
        }

        Collections.sort(neverHeardAndSeen);
        int size = neverHeardAndSeen.size();

        System.out.println(size);

        for (String name : neverHeardAndSeen) {
            System.out.println(name);
        }

    }

}
