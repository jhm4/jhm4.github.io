/*************************************************************************
 * Names      : Sarah McGuire, Housten Marinez
 * NetIDs    : sarahem, jhm4
 * Precept   : P05
 *
 * Dependencies :
 * Description  : 
 *  
 *  This is a template file for RingBuffer.java. It lists the constructors and
 *  methods you need, along with descriptions of what they're supposed to do.
 *  
 *  Note: it won't compile until you fill in the constructors and methods
 *        (or at least commment out the ones whose return type is non-void).
 *
 *****************************************************************************/

public class RingBuffer {
    private double[] rb;          // items in the buffer
    private int first;            // index for the next dequeue or peek
    private int last;             // index for the next enqueue
    private int size;             // number of items in the buffer

    // create an empty ring buffer, with given max capacity
    public RingBuffer(int capacity) {
        rb = new double[capacity];
        size = 0; 
        first = 0;
        last = 0; 
    }

    // return number of items currently in the buffer
    public int size() {
        return size; 
    }

    // is the buffer empty (size equals zero)?
    public boolean isEmpty() {
        if (size == 0) {
            return true;
        }
        else {
            return false;
        }
    }

    // is the buffer full (size equals array capacity)?
    public boolean isFull() {
        if (size == rb.length) {
            return true;
        }
        else {
            return false;
        }
    }

    // add item x to the end
    public void enqueue(double x) {
        if (isFull()) {
            throw new RuntimeException("Ring buffer overflow");
        }
        rb[last] = x; 
        last++;
        if(last == rb.length) {
            last = 0;
        }
        size++; 
    }

    // delete and return item from the front
    public double dequeue() {
        if (isEmpty()) {
            throw new RuntimeException("Ring buffer underflow");
        }
        double c = rb[first];
        first++; 
        if (first == rb.length) {
            first = 0;
        }   
        size--;
        return c; 
    }

    // return (but do not delete) item from the front
    public double peek() {
        if (isEmpty()) {
            throw new RuntimeException("Ring buffer underflow");
        }
        double c = rb[first];
        return c;
    }

    // a simple test of the constructor and methods in RingBuffer
    public static void main(String[] args) {
        int N = Integer.parseInt(args[0]);
        RingBuffer buffer = new RingBuffer(N);
        for (int i = 1; i <= N; i++) {
            buffer.enqueue(i);
        }
        double t = buffer.dequeue();
        buffer.enqueue(t);
        System.out.println("Size after wrap-around is " + buffer.size());
        while (buffer.size() >= 2) {
            double x = buffer.dequeue();
            double y = buffer.dequeue();
            buffer.enqueue(x + y);
        }
        System.out.println(buffer.peek());
    }

}