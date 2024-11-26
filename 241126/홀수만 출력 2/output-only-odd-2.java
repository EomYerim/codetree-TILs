import java.util.Scanner;
import java.util.ArrayList;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int b=sc.nextInt();
        int a=sc.nextInt();
        ArrayList<Integer> arr = new ArrayList<>();

        for(int i=a; i<=b; i++){
            if(i%2!=0){
                arr.add(i);
            }
        }
        for(int i=arr.size()-1; i>=0; i--){
            System.out.print(arr.get(i)+" ");
        }


    }
}