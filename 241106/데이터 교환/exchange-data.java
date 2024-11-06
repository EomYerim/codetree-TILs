public class Main {
    public static void main(String[] args) {
        int a=5,b=6,c=7;
        int tempA;
        int tempC;
        tempA=a;
        tempC=c;

        c=b;
        b=tempA;
        a=tempC;
        System.out.println(a);
        System.out.println(b);
        System.out.println(c);
    }
}