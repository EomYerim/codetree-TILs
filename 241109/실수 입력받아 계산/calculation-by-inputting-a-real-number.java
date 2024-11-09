import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        float a,b,c;

        a=sc.nextFloat();
        b=sc.nextFloat();
        c=a+b;

        System.out.printf("%.2f",c);
    }
}