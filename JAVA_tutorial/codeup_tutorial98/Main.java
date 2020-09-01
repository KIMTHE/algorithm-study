import java.util.Scanner;


public class Main {

	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int h = sc.nextInt();
		int w = sc.nextInt();
		Plate.set(h, w);

		int n = sc.nextInt();
		Stick[] s = new Stick[n]; 
		for(int i=0; i<n; i++)
		{
			int l = sc.nextInt();
			int d = sc.nextInt();
			int x = sc.nextInt();
			int y = sc.nextInt();
			
			s[i] = new Stick(l,d,x,y);
			//s[i].print();
			Plate.put(s[i]);
			//Plate.print();
		}
		
		Plate.print();
		
		
	}

}
