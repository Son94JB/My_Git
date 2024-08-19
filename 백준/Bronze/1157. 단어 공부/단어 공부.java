import java.io.*;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Main {

    public static void main(String[] args) throws IOException {
        // 대소문자를 구분하지 않고 가장 많이 사용된 알파벳을 대문자로 출력
        // 만약 가장 많이 사용된 문자가 여러개 라면 ? 를 출력
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String word = br.readLine();
        word = word.toUpperCase();

        HashMap<Character, Integer> alphabet = new HashMap<>();

        for (int i = 0; i < word.length(); i++) {
            if (alphabet.containsKey(word.charAt(i))) {
                alphabet.put(word.charAt(i), alphabet.get(word.charAt(i)) + 1);
            }
            else {
                alphabet.put(word.charAt(i), 1);
            }
        }

        List<Character> keyWithMaxValue = new ArrayList<>();
        int maxValue = Integer.MIN_VALUE;

        for (Map.Entry<Character, Integer> entry : alphabet.entrySet()) {
            if (entry.getValue() > maxValue) {
                maxValue = entry.getValue();
                keyWithMaxValue.clear();
                keyWithMaxValue.add(entry.getKey());
            } else if (entry.getValue() == maxValue) {
                keyWithMaxValue.add(entry.getKey());
            }
        }
        if (keyWithMaxValue.size() == 1) System.out.println(keyWithMaxValue.get(0));
        else System.out.println("?");
    }
}