import java.util.Scanner;
import java.util.ArrayList;
public class Main {
    public static void main(String[] args) {
       Scanner sc = new Scanner(System.in);
       int b=sc.nextInt();
       int a=sc.nextInt();
       ArrayList<Integer> list = new ArrayList<>();
       for(int i=a; i<=b; i++){
            if(i%2==0){
                list.add(i);
            }
       }
       for(int i=list.size()-1; i>=0; i--){
            System.out.print(list.get(i)+" ");
       }

    }
}