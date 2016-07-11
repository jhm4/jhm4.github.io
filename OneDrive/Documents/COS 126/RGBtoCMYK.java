/*
 * Name: Houston Martinez
 * Netid: jhm4
 * Precept: P05
 * 
 * This program converts the three values of the color code RGB
 * to four values of the color code CMYK.
 */
public class RGBtoCMYK
{
    public static void main(String args[])
    {
        int r = Integer.parseInt(args[0]);
        int g = Integer.parseInt(args[1]);
        int b = Integer.parseInt(args[2]);
        double w = Math.max(Math.max((r*1.0 / 255.0), (g*1.0 / 255.0)),
                            (b*1.0 / 255));
        double c = ((w - (r*1.0 / 255)) / w);
        double m = ((w - (g*1.0 / 255)) / w);
        double y = ((w - (b*1.0 / 255)) / w);
        double bk = (1 - w);
        System.out.println("red" + " = " + r);
        System.out.println("green" + " = " + g);
        System.out.println("blue" + " = " + b);
        if (w == 0) System.out.println("cyan" + " = " + 0.0);
        else System.out.println("cyan" + " = " + c);
        if (w == 0) System.out.println("magenta" + " = " + 0.0);
        else System.out.println("magenta" + " = " + m);
        if (w == 0) System.out.println("yellow" + " = " + 0.0);
        else System.out.println("yellow" + " = " + y);
        System.out.println("black" + " = " + bk);
        
    }
}
