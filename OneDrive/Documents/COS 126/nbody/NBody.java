/*
 * Name: Houston Martinez
 * Netid: jhm4
 * Precept: P05
 * 
 * Dependencies: planets.txt, 2001.mid, starfield.jpg
 * This program is able to simulate N number of bodies
 * under their mutual Newtonian gravitational forces.
 */
public class NBody
{
    public static void main(String[] args)
    { //read in command line arguments T and tc (change in t)
        double T = Double.parseDouble(args[0]);
        double tc = Double.parseDouble(args[1]);
        int N = StdIn.readInt();
        double G = 6.67e-11;
        double r = StdIn.readDouble();
        
        double[] px = new double[N];
        double[] py = new double[N];
        double[] vx = new double[N];
        double[] vy = new double[N];
        double[] mass = new double[N];
        String[] image = new String[N];
        
        //Set scale for x and y coordinate system
        StdDraw.setXscale(-r, r);
        StdDraw.setYscale(-r, r);
        
        //play music
        StdAudio.play("2001.mid");
        
        
        //load in planet data
        for (int i = 0; i < N; i++) {
            px[i] = StdIn.readDouble();
            py[i] = StdIn.readDouble();
            vx[i] = StdIn.readDouble();
            vy[i] = StdIn.readDouble();
            mass[i] = StdIn.readDouble();
            image[i] = StdIn.readString();
            
        }
        
        // big time loop
        for (int t = 0; t < T; t += tc) {
            
            //initalize force arrays
            double[] fx = new double[N];
            double[] fy = new double[N];
            double[] ax = new double[N];
            double[] ay = new double[N];
            
            for (int i = 0; i < N; i++) {
                fx[i] = 0.0;
                fy[i] = 0.0;
                for (int j = 0; j < N; j++) {
                    if (i != j) {
                        double radius = Math.sqrt((py[i] - py[j])
                                                      *(py[i] - py[j])
                                                      + (px[i] - px[j])
                                                      *(px[i] - px[j]));
                        double F = G*mass[i]*mass[j]/(radius*radius);
                        fy[i] += F*(py[j]-py[i])/radius;
                        fx[i] += F*(px[j] - px[i])/radius;
                    }
                }
                //calculate new position and velocity
                ax[i] = fx[i]/mass[i];
                ay[i] = fy[i]/mass[i];
            }
            for (int i = 0; i < N; i++) {
                vx[i] = vx[i] + tc*ax[i];
                vy[i] = vy[i] + tc*ay[i];
                
                px[i] = px[i] + tc*vx[i];
                py[i] = py[i] + tc*vy[i];
            }
            StdDraw.picture(0, 0, "starfield.jpg");
            for (int i = 0; i < N; i++)
                StdDraw.picture(px[i], py[i], image[i]);
            StdDraw.show(40);
            
        }
        StdOut.printf("%d\n", N);
        StdOut.printf("%.2e\n", r);
        for (int i = 0; i < N; i++) {
            StdOut.printf("%11.4e %11.4e %11.4e %11.4e %11.4e %12s\n",
                          px[i], py[i], vx[i], vy[i], mass[i], image[i]);
        }
    }
}