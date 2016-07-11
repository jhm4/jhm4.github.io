/* 
 * Names: Sarah McGuire, Houston Martinez
 * NetIDs: sarahem, jhm4
 * Precept: P05
 * 
 * Dependencies: StdRandom, StringBuilder, ST
 */

public class MarkovModel {
    
    private ST<String, int[]> st = new ST<String, int[]>();
    private int order; 
    
    public MarkovModel(String text, int k) {
        order = k; 
        String circle = text.substring(0, k); 
        text = text + circle; 
        int N = text.length(); 
        int array = 128;
        
        for (int i = 0; i < N-k; i++) {
            String s = text.substring(i, i+k);
            if (!st.contains(s)) {
                int[] val = new int[array];
                char next = text.charAt(i+k);
                val[next] += 1;
                st.put(s, val);
            }
            else {
                char next = text.charAt(i+k);
                int[] val = st.get(s);
                val[next] += 1;
                st.put(s, val);
            }       
        }   
    }
    
    public int order() {
        return order;  
    }    
    
    public int freq(String kgram) {
        int N = kgram.length();
        if (N < order()) {
        throw new RuntimeException("Length of string less than "
                                           + "value of k.");
                                       }
        int[] sum = st.get(kgram);
        int total = 0;
        for (int i = 0; i < sum.length; i++) {
            int v = sum[i];
            total += v;
        }
        return total;
    }
    public int freq(String kgram, char c) {
        if (kgram.length() < order()) {
            throw new RuntimeException("Length of string less than "
                                           + "value of k.");
                                       }
        int[] sum = st.get(kgram);
        int index = sum[c];
        return index;
    }
    public char rand(String kgram) { 
     if (kgram.length() < order()) {
            throw new RuntimeException("Length of string less than "
                                           + "value of k.");
                                       }
     if (!st.contains(kgram)) {
            throw new RuntimeException("No such kgram.");
                                       }
            double frequency = freq(kgram)*1.0;
            int[] val = st.get(kgram);
            int N = val.length;
            double[] a = new double[N];
            for (int i = 0; i < N; i++) {
                a[i] = val[i]/frequency; 
            }
            char f = (char) StdRandom.discrete(a);
            return f;
    }
    
    public String gen(String kgram, int T) {
        StringBuilder s1 = new StringBuilder(kgram);
        for (int i = 0; i < T - kgram.length(); i++) {
        String holder = s1.substring(i, i + order());
        char c = rand(holder);
        s1.append(c);
    }
        kgram = s1.toString();
        return kgram;
    }
  

        public static void main(String[] args) {
//        MarkovModel mod1 = new MarkovModel("i am sam. sam i am", 3);
//        StdOut.println("freq(\"sam\", ' ')    = " + mod1.freq("sam", ' '));
//        StdOut.println("freq(\"sam\", '.')    = " + mod1.freq("sam", '.'));
//        StdOut.println("freq(\"mi \")         = " + mod1.freq("mi "));
//        StdOut.println("freq(\"sam\")         = " + mod1.freq("sam"));
//        StdOut.println();
//
//        String text = "now is the time. now is the time to eat. " 
//                    + "now is the time to live.";
//        MarkovModel mod2 = new MarkovModel(text, 7);
//        StdOut.println("freq(\"now is \", ' ') = " + mod2.freq("now is ", ' '));
//        StdOut.println("freq(\"now is \", 't') = " + mod2.freq("now is ", 't'));
//        StdOut.println("freq(\"now is \")      = " + mod2.freq("now is "));
            
//            MarkovModel mod1 = new MarkovModel("abca", 1);
//            String test = mod1.gen("c", 1);
//            StdOut.println(test);
            
//              MarkovModel mod1 = new MarkovModel("abc", 1);
//              String test = mod1.gen("a", 1);
//              StdOut.println(test);
            
            
        }
} 