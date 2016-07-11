
/*************************************************************************
  * Name         :Houston Martinez 
  * NetID        :jhm4
  * Precept      :P05
  *
  * Dependencies :StdOut for testing
  * Description  :LSFR creates a linear feedback shift register. 
  * In one step it exclusive or's the end bit with the bit at a tap
  * position, shifts the bits down one and places this XOR bit at the
  * empty place. 
  *  
  *************************************************************************/

public class LFSR {
    // declare instance variables
    private int N;       // number of bits in the LFSR
    private int[] reg;   // reg[i] = ith bit of LFSR, reg[0] is rightmost bit
    private int tap;     // index of the tap bit
    
    /*
     * to create LFSR with the given initial seed and tap
     * instance variable N is used to store the length of the string
     * tap reverses the position of the tap in order to match the
     * array representation.
     * reg[] is initialized to hold the string in an int array
     * This constructor saves represents the LSFR in an int array.
     */
    public LFSR(String seed, int t) {
        // PUT YOUR CODE HERE
        
        N = seed.length();
        tap = N-t-1;
        reg = new int[N];
        int c = 48;
        for (int i = 0; i < N; i++) {
            reg[i] = (int) seed.charAt(i)-c;
        }
        //LSFR lsfr = new LSFR(seed, tap);
    }
    
    // simulate one step and return the new bit as 0 or 1
    /*
     *step() method  XORs the first value in the array with
     * the tap position of the array. It slides the values
     * down one position and places the XOR'd bit at the end.
     */ 
    public int step() {
        // PUT YOUR CODE HERE
        int c = reg[0] ^ reg[tap];
        for (int i = 0; i < N-1; i++) {
            reg[i] = reg[i+1]; }
        //array index error
        reg[N-1] = c;
        return c;
        
    }
    
    //simulate k steps and return k-bit integer
    public int generate(int k) {
        // PUT YOUR CODE HERE
        int t = 0;
        for (int i = 0; i < k; i++) {
            t = t*2 + step();
        }
        return t;
    }
    
//    // return a string representation of the LFSR
    /* Since my array already has the seed in the correct order
     * the toString method just needs to convert the int values 
     * into characters.
     */
    public String toString()  {
        // PUT YOUR CODE HERE
        String s = "";
        for (int i = 0; i < N; i++) {
            s = s + reg[i];
        }
        return s;
    }
    
    
    
    // test all of the methods in LFSR
    public static void main(String[] args)  {
        // PUT YOUR TEST CODE HERE
//        LFSR lfsr = new LFSR("01101000010", 8);
//        for (int i = 0; i < 10; i++) {
//            int r = lfsr.generate(5);
//            StdOut.println(lfsr + " " + r);
//        LFSR lfsr; // (delete this line if lfsr is already declared!)
//        lfsr = new LFSR("01101000010100010000", 16);
//        for (int i = 0; i < 10; i++) {
//            int r = lfsr.generate(8);
//            StdOut.println(lfsr + " " + r);
//        }
        
    }
}



