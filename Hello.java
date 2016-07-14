public class Hello {
	public static int calculate(int variable){
		return (variable + 2);
	}
public static void main(String[] args) {
	int i = 0;
	int b = calculate(++i);
	System.out.println(b);
	System.out.println(i);
	}
}