
public class Plate {
	private static int h,w;
	private static int[][] loc;
	
	public static int getH() {
		return h;
	}
	
	public static int getW() {
		return w;
	}

	public static void set(int h, int w)
	{
		Plate.h= h;
		Plate.w= w;
		Plate.loc = new int[h][w];
	}
	
	public static void put(Stick s)
	{
		int[][] stick = s.getLoc(); 
		
		for(int i=0; i<s.getL(); i++)
		{
			loc[stick[i][0]-1][stick[i][1]-1] =1;
		}
	}
	
	public static void print()
	{
		for(int i =0; i<h; i++)
		{
			for(int j=0; j<w; j++)
			{
				System.out.print(loc[i][j]+" ");
			}
			System.out.println();
		}
	}
	
}
