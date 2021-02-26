
public class Ant {
	private static int[] loc;

	public static int[] getLoc() {
		return loc;
	}

	public static void setLoc() {
		loc = new int[2];
		loc[0] = 1;
		loc[1] = 1;
	}
	
	public static void move(int x, int y)
	{
		loc[0] = x;
		loc[1] = y;
	}

}
