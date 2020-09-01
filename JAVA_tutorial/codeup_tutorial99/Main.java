import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[][] loc = new int[10][10];
		
		for(int i = 0; i<10; i++)
		{
			for(int j=0; j<10; j++)
			{
				loc[i][j] = sc.nextInt();
			}
		}
		Box.setLoc(loc);
		Ant.setLoc();
		
		Box.find();
		Box.getLoc();

	}

}
