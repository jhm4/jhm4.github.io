/*************************************************************************
  * Names      : Sarah McGuire, Housten Marinez
  * NetIDs    : sarahem, jhm4
  * Precept   : P05
  *
  * Dependencies : StdDraw, StdAudio, GuitarString, 
  * Description  : This program uses an array of frequencies
  * and a GuitarString array along with GuitarString methods
  * to simulate the sound of a guitar from keyboard input.
  * 
  * */
public class GuitarHero {
    public static void main(String[] args) {
        
        //create an array of strings
        double CONCERT_A = 440.0;
        int strings = 37;
        double[] notes = new double[strings];
        GuitarString[] guitar = new GuitarString[strings];
        for (int i = 0; i < strings; i++) {
            double frequency = CONCERT_A*Math.pow(2.0, (i-24)/(12.0)); 
            notes[i] = frequency; 
        }
        for (int i = 0; i < strings; i++) {
            guitar[i] =  new GuitarString(notes[i]);
        }
        String keyboard = "q2we4r5ty7u8i9op-[=zxdcfvgbnjmk,.;/' ";
        while (true) {
            // check if the user has typed a key; if so, process it   
            if (StdDraw.hasNextKeyTyped()) {
                char key = StdDraw.nextKeyTyped();
                int index = keyboard.indexOf(key);
                
                if (index >= 0) {
                    guitar[index].pluck();
                }
            }
                double sample = 0.0;
                for (int i = 0; i < strings; i++) {
                    sample += guitar[i].sample();
                }
            
                StdAudio.play(sample);
                
                for (int i = 0; i < strings; i++) {
                    guitar[i].tic(); 
                }
            
        }
    }
}