/*
 * Name: Houston Martinez
 * Netid: jhmn4
 * Precept: P05
 * 
 * This program will report true if three integers are
 * presented in ascending or descending order and false
 * if they are in any other order.
 */
public class Ordered
{
    public static void main(String[] args)
    {
        int a = Integer.parseInt(args[0]);
        int b = Integer.parseInt(args[1]);
        int c = Integer.parseInt(args[2]);
        boolean isOrdered;
        isOrdered = (a < b && b < c) || (a > b && b > c);
      
        System.out.println(isOrdered);
    }
}
            