import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;


public class Main {
    // 전체 사람의 수 N개가 주어지고 촌수를 구해야 하는 두 사람의 번호가 주어진다. 그리고 관계의 개수 M이 주어진다.
    // 밑으로는 부모 자식 관계가 N개 주어진다. 이 때, 두 사람의 촌수를 구하자.

    static int N, M, A, B;
    static int[] familyTree;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        familyTree = new int[N+1];
        String AB = br.readLine();

        A = Integer.parseInt(AB.split(" ")[0]);
        B = Integer.parseInt(AB.split(" ")[1]);

        M = Integer.parseInt(br.readLine());

        // 인덱스가 노드 번호이자 사람의 번호로 두고
        // 부모 노드의 번호를 값으로 가진다면 되지 않을까?
        for (int i = 0; i < M; i++) {
            String parentAndChild = br.readLine();
            int parent = Integer.parseInt(parentAndChild.split(" ")[0]);
            int child = Integer.parseInt(parentAndChild.split(" ")[1]);
            familyTree[child] = parent;
        }

        int result = FindFamilyLink(A, B);
        System.out.println(result);

    }

    static int FindFamilyLink(int A, int B) {
        // A의 조상들 찾기
        List<Integer> ancestorsA = new ArrayList<>();
        while (A != 0) {
            ancestorsA.add(A);
            A = familyTree[A];
        }

        // B의 조상들 찾기 및 촌수 계산
        int count = 0;
        while (B != 0) {
            if (ancestorsA.contains(B)) {
                return count + ancestorsA.indexOf(B);
            }
            B = familyTree[B];
            count++;
        }

        return -1; // 공통 조상이 없는 경우
    }

}
