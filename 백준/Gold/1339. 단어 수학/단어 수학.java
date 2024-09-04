import java.io.*;
import java.util.*;

public class Main {
    // N개의 알파벳이 주어질 때, 해당 알파벳에 0~9까지의 숫자를 할당하고 모두 더했을 때,
    // 얻을 수 있는 최대값을 구하라
    static int N;
    static List<String> data = new ArrayList<>();
    static Map<Character, Integer> weightMap = new HashMap<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String n = br.readLine();
        
        N = Integer.parseInt(n);

        // 가장 큰 자리 수 순서대로 9에서 역순으로 넣어주면 되지 않을까
        // 가장 큰 자리 수를 우선 순위, 같은 자리 수라면 개수로 결정
        for (int i = 0; i < N; i++) {
            String input = br.readLine();
            data.add(input);
            calculateWeight(input);
        }

        // 가중치가 높은 순으로 알파벳 정렬
        List<Map.Entry<Character, Integer>> sortedWeights = new ArrayList<>(weightMap.entrySet());
        sortedWeights.sort((a, b) -> b.getValue().compareTo(a.getValue()));

        // 숫자 할당
        int[] numberAssign = new int[26];  // 알파벳 A-Z에 대한 숫자 할당
        int num = 9;
        for (Map.Entry<Character, Integer> entry : sortedWeights) {
            numberAssign[entry.getKey() - 'A'] = num--;  // 9부터 줄여가며 할당
        }

        // 알파벳 합을 계산
        int maxValue = 0;
        for (String str : data) {
            int curValue = 0;
            for (char c : str.toCharArray()) {
                curValue = curValue * 10 + numberAssign[c - 'A'];
            }
            maxValue += curValue;
        }

        System.out.println(maxValue);

    }

    static void calculateWeight(String str) {
        int length = str.length();
        for (int i = 0; i < length; i++) {
            char c = str.charAt(i);
            int weight = (int) Math.pow(10, length - i - 1);  // 자리수 가중치
            weightMap.put(c, weightMap.getOrDefault(c, 0) + weight);
        }
    }


}
