import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        double a,b;
        String c;

        c=sc.next();
        a=sc.nextDouble();
        b=sc.nextDouble();

        System.out.println(c);
        System.out.printf("%.2f",a);
        System.out.print("\n");
        System.out.printf("%.2f",b);
    }
}