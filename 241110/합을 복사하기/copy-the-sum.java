public class Main {
    public static void main(String[] args) {
        int a=1;
        int b=2;
        int c=3;

        int sum=a+b+c;
        a=b=c=sum;

        System.out.print(a+" "+b+" "+c);
    }
}