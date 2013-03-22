/*
*Author: Zachary Richardson
*Assignment: PizzaRun.java
*Date: March 10, 2013
*/

import java.lang.Math;

public class PizzaRun{
	public static final int SLICE_PER_PIE = 8;
	public static float price;
	public static int nSlices;
        public static void main(java.lang.String args[]){
                String s = new String();
		float a = new Float(args[0]);
                price = a;
                for (int i = 1 ; i < args.length ; i++){
                        nSlices += Integer.parseInt(args[i]);
               }
		calcWholePies(nSlices);
	}
               public static int calcWholePies(double x){
			/*
			*This function calculates the total number of
			*pizzas needed based on the args that are entered
			* and calculates the total price and leftover
			*slices.
			*/
                        double pizza = (x / SLICE_PER_PIE);
                        int pizza1 = ((int)Math.ceil(pizza));
			float total;
			total = pizza1 * price;
                        System.out.println("Buy "+ pizza1 + " for $" + total);
			int extra = (SLICE_PER_PIE*pizza1) -(int) x;
			System.out.println("There will be " + extra + " extra slices."); 
			return pizza1;
                }                      
}

