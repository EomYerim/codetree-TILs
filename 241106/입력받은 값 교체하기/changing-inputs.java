import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int a,b,tempA;
        a=sc.nextInt();
        b=sc.nextInt();
        tempA=a;
        a=b;
        b=tempA;
        System.out.print(a+" "+b);

    }
}