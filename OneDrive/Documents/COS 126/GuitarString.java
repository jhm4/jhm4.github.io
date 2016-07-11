/*************************************************************************
 * Names     : Sarah McGuire, Housten Martinez
 * NetID(s)     : 
 * Precept(s)   :
 *
 * Dependencies :
 * Description  : 
 *  
 *  This is a template file for GuitarString.java. It lists the constructors
 *  and methods you need, along with descriptions of what they're supposed
 *  to do.
 *  
 *  Note: it won't compile until you fill in the constructors and methods
 *        (or at least commment out the ones whose return type is non-void).
 *
 *****************************************************************************/

public class GuitarString {

    private RingBuffer buffer; // ring buffer
    private int call; //counting number of times tic is called
    //private int capacity; //capacity of buffer
    
    // create guitar string of given frequency, using sampling rate of 44,100
    public GuitarString(double frequency) {
        call = 0;
 
        int rate = 44100; 
        int N = (int)Math.ceil(rate/frequency); 
        buffer = new RingBuffer(N); 
        for (int i = 0; i < N; i++) {
            buffer.enqueue(0.0);
        }
    }

    // create a guitar string with size & initial values given by the array
    public GuitarString(double[] init) {
        call = 0;
        
        int c = init.length; 
        buffer = new RingBuffer(c);
        for (int i = 0; i < c; i++) {
            buffer.enqueue(init[i]);
        }
    }

    // pluck the guitar string by replacing the buffer with white noise
    public void pluck() {
        for (int i = 0; i < buffer.size(); i++) { //N replace buffer.size()
           double p = buffer.dequeue();   
          buffer.enqueue(Math.random() - 0.5);
        }     
    }

    // advance the simulation one time step
    public void tic() {
        double decay = .996;
        double avg = ((buffer.dequeue() + buffer.peek())/2.0)*decay;
        buffer.enqueue(avg);
        call++;
        
    }

    // return the current sample
    public double sample() {
        // YOUR CODE HERE
        double front = buffer.peek();
        return front;
    }

    // return number of times tic was called
    public int time() {
        // YOUR CODE HERE
        return call;
        
    }

    public static void main(String[] args) {
//        int N = Integer.parseInt(args[0]);
//        double[] samples = { .2, .4, .5, .3, -.2, .4, .3, .0, -.1, -.3 };  
//        GuitarString testString = new GuitarString(samples);
//        for (int i = 0; i < N; i++) {
//            int t = testString.time();
//            double sample = testString.sample();
//            System.out.printf("%6d %8.4f\n", t, sample);
//            testString.tic();
//        }
    }

}