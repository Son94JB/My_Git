import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String word = br.readLine();
        int N = word.length();
        boolean tri = true;

        for (int i = 0; i < N/2; i++) {
            if (word.charAt(i) != word.charAt(N - i - 1)) {
                tri = false;
                break;
            }
        }

        if (tri) System.out.println(1);
        else System.out.println(0);
    }
}