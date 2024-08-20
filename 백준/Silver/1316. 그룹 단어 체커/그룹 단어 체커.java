    import java.io.*;
    import java.util.ArrayList;
    import java.util.List;

    public class Main {
        // 같은 문자는 연속해서 나오는 단어가 그룹 단어이다.
        // 주어진 단어들 중 그룹 단어가 몇 개인지 반환
        static int N;
        static int count;

        public static void main(String[] args) throws IOException {

            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

            String n = br.readLine();
            N = Integer.parseInt(n);

            for (int i = 0; i < N; i++) {
                String word = br.readLine();
                List<Character> alp = new ArrayList<>();

                for (int j = 0; j < word.length(); j++) {
                    if (!alp.contains(word.charAt(j))) {
                        alp.add(word.charAt(j));
                        if (j == word.length() - 1) {
                            count++;
                        }
                    } else if (word.charAt(j) != word.charAt(j - 1)) {
                        break;
                    } else {
                        if (j == word.length() - 1) {
                            count++;
                        }
                    }
                }

            }
            System.out.println(count);
        }
    }