/*
 * Name: Houston Martinez
 * NetID: jhm4
 * Precept: P05
 * 
 * This program uses a recursive function to print out
 * a recursive serpinski triangle and a couple other static
 * methods required to complete the shape.
 */
public class Sierpinski {
    private static double ALTITUDE = Math.sqrt(3)/2;
    public static void sierpinski(int N, double x, double y, double s) {
        if (N == 0) return;
        filledTriangle(x, y, s);
        sierpinski(N-1, (x-s/2), y, s/2);
        sierpinski(N-1, (x+s/2), y, s/2);
        sierpinski(N-1, x, (y+ALTITUDE*s), s/2);
    }
    
    public static void filledTriangle(double x1, double y1, double s) {
        //int N = Integer.parseInt(args[0]);
        double[] x2 = {x1, x1+(s/2), x1-(s/2)};
        double[] y2 = {y1, y1+ALTITUDE*s, y1+ALTITUDE*s};
        StdDraw.filledPolygon(x2, y2);
    }
    
    public static void main(String[]args) {
        int N = Integer.parseInt(args[0]);
        double[] x = {0, 1, 0.5};
        double[] y = {0, 0, ALTITUDE};
        double x1 = .5;       
        double y1 = 0.0;
        double s = .5;
        
        StdDraw.polygon(x, y);
        sierpinski(N, x1, y1, s);
        
    }
}  