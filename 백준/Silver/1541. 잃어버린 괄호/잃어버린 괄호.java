import java.io.*;

public class Main {
    // +, - 로 이루어진 식이 주어질 때, 해당 식에 괄호를 추가하여 계산 값이 최소가 되도록하고 그 최소값을 출력
    // - 이후의 식이 가장 길게 되도록 괄호를 쳐주면 될 듯

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String equation = br.readLine();

        String[] minusNum = equation.split("-");

        int result = 0;
        String[] firstPart = minusNum[0].split("\\+");
        for (String num : firstPart) {
            result += Integer.parseInt(num);
        }

        for (int i = 1; i < minusNum.length; i++) {
            String[] addPart = minusNum[i].split("\\+");
            int sum = 0;
            for (String num : addPart) {
                sum += Integer.parseInt(num);
            }
            result -= sum;
        }

        System.out.println(result);
    }

}
