/*
 * Names: Sarah McGuire, Houston Martinez
 * Net IDs: sarahem, jhm4
 * Precepts: P05
 * Dependencies: StdIn, StdOut, 
 * Description: We used a linked list of points and ran two heuristics-- one
 * which inserted the point after the point is was closest to; the other was 
 * inserted after the point (which added the least distance to the total tour
 * length). (A lot of the debugging/testing methods are commentented out)
 */

public class Tour {
    private Node first; //saves the node address of the first point (node)
    private int listlength; //keeps track of points in the list 
    //nested node class- constructor for a node 
    private class Node {
        private Point p;
        private Node next;
    }
    //constructor for a tour 
    public Tour() {
        Node first = null; 
    }
    //debugging constructor for tour
    public Tour(Point a, Point b, Point c, Point d) {
        listlength = 0;
        first = new Node();
        first.p = a;
        listlength++;
//    first.next = first; <-- testing
        Node bNode = new Node();
        bNode.p = b;
        first.next = bNode;
        listlength++;
//    bNode.next = first; <-- testing
        Node cNode = new Node();
        cNode.p = c;
        bNode.next = cNode;
        listlength++;
//    cNode.next = first; <-- testing
        Node dNode = new Node();
        dNode.p = d;
        cNode.next = dNode;
        dNode.next = first; 
        listlength++;
    }
    //prints out all of the points in linked list
    public void show() { 
//      Point test = first.p;
//      StdOut.println(test);
        if (first == null) return;
        Node x = first; //x denotes node name to be incremented throughout program
        do {
            Point shown = x.p;
            StdOut.println(shown);
            x = x.next;
        }
        while(x != first); 
    }
    //draws lines connecting each point in the linked list 
    public void draw() {
        Node x = first;
        if (first == null) return;
        do {
            Point here = x.p;
            Point there = x.next.p;
            here.drawTo(there);
            x = x.next;
        }
        while(x != first);
    }
    //returns list length (number of points in linked list) 
    public int size() {
        return listlength;   
    }
    //calculates the full length of the tour/ distance betweens all points
    public double distance() {
        double length = 0.0;
        if (first == null) return 0.0;
        Node here = first; 
        Node there = first.next; 
        do { 
            double locallength =  here.p.distanceTo(there.p); 
            length += locallength; 
            here = here.next;
            there = there.next;    
        }
        while (here != first);
        return length;   
    }
    //compares distance between Point p and every point in the list 
    //and inserts it behind the one it's closest to 
    public void insertNearest(Point p) {
        if (first == null) {
            first = new Node();
            first.p = p;
            first.next = first;
            listlength++;
        }
        else {
            Node x = first;
            Node best = null;
            double max = Double.POSITIVE_INFINITY;
            do {
                double distance = x.p.distanceTo(p);
                if (distance < max) {
                    max = distance;
                    best = x;
                }
                x = x.next;
            }
            while (x != first);
            Node toinsert = new Node();
            toinsert.next = best.next;
            best.next = toinsert;
            toinsert.p = p;
            listlength++;
        }  
    }
    //compares distance between Point p and every pair of points 
    //and inserts it between the pair that adds the least distance to the tour 
    public void insertSmallest(Point p) {
        if (first == null) {
            first = new Node();
            first.p = p;
            first.next = first;
            listlength++;
        }
        else {
            Node x = first;
            //test is used to calculate distance w/o insertion
            Node test = new Node(); 
            //holds node after which point p has the least distance
            Node best = null; 
            double max = Double.POSITIVE_INFINITY; 
            Node toinsert = new Node(); //node that will be inserting with point p
            test.p = p;
            do { 
                //distance between pair of points
                double original = x.p.distanceTo(x.next.p); 
                //distance between first point and p + p and the second point
                double possible = x.p.distanceTo(test.p) 
                    + test.p.distanceTo(x.next.p);
                //difference between possible and original (distance added to tour)
                double addeddistance = possible - original;
                if (addeddistance < max) {
                    best = x;
                    max = addeddistance;
                }
                x = x.next;
            }
            while (x != first);
            toinsert.next = best.next;
            best.next = toinsert;
            toinsert.p = test.p;
            listlength++;  
        }
    }
    
//    // main method for testing
    public static void main(String[] args) { 
//        // define 4 points forming a square
//        Point a = new Point(100.0, 100.0);
//        Point b = new Point(500.0, 100.0);
//        Point c = new Point(500.0, 500.0);
//        Point d = new Point(100.0, 500.0);
//        
//        // Set up a Tour with those four points
//        // The constructor should link a->b->c->d->a
//        Tour squareTour = new Tour(a, b, c, d);
//        squareTour.distance();
//        
//        //draws a square
//        StdDraw.setXscale(0, 600);
//        StdDraw.setYscale(0, 600);
//        squareTour.draw();
//        squareTour.show();
        
    }
}