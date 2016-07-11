/*
 * 
 * 
 * 
 * 
 */
public class CA {
    private int[] rules;
    private int[] cells;
    private int capacity;
    
    public CA(int N, String string) {
        int RNUM = string.length();
        rules = new int[RNUM];
        for (int i = 0; i <rules.length; i++) {
            rules[i] = Integer.parseInt(string.substring(i, i+1));
        }
        capacity = 2*N + 3;
        cells = new int[capacity];
        cells[capacity/2] = 1;
    }
    public String toString() {
        String state = "";
        String off = "0";
        String on = "1";
        for (int i = 1; i < cells.length-1; i++) {
            if (cells[i] == 0) {
            state = state + off;
        }
            else state = state + on;
        }
        return state;
    }
    public void step() {
    int[] temp = new [capacity];
    for (int i = 1; i<capacity-1; i++) {
        temp[i] = cells[i];
    }
    
    }

    public static void main(String[]args) {
        int N = Integer.parseInt(args[0]);
        String string = args[1];
        CA automat = new CA(N, string);
    
    StdOut.println(automat);
    for (int i = 0; i < N; i++){
        automat.step();
    StdOut.println(automat);
    }
    }
    } 