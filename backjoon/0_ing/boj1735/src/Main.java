import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int ax = Integer.parseInt(st.nextToken());
        int ay = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int bx = Integer.parseInt(st.nextToken());
        int by = Integer.parseInt(st.nextToken());

        // 분모 구하기
        int denominator = ay * by;
        int tmpA = ay;
        int tmpB = by;

        // 큰수 구하기
        int tmp;
        if (tmpA > tmpB) {
            tmp = tmpA;
            tmpA = tmpB;
            tmpB = tmp;
        }

        while (tmpA != 0 && tmpB % tmpA != 0) {
            tmp = tmpB % tmpA;
            tmpB = tmpA;
            tmpA = tmp;
        }

        if (tmpA != 0) denominator /= tmpA;

//        System.out.println(denominator + " " + by + " " + bx);
//        System.out.println(denominator + " " + ay + " " + ax);
        int molecule = denominator / by * bx + denominator / ay * ax;

        tmpA = molecule;
        tmpB = denominator;
        if (tmpA > tmpB) {
            tmp = tmpA;
            tmpA = tmpB;
            tmpB = tmp;
        }

        while (tmpA != 0 && tmpB % tmpA != 0) {
            tmp = tmpB % tmpA;
            tmpB = tmpA;
            tmpA = tmp;
        }

        molecule /= tmpA;
        denominator /= tmpA;

        System.out.println(molecule + " " + denominator);

    }
}