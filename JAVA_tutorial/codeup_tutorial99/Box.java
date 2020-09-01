
public class Box {
	
	private static int[][] loc;

	public static void getLoc() {
		for(int i = 0; i<10; i++)
		{
			for(int j=0; j<10; j++)
			{
				System.out.print(loc[i][j]+" ");
			}
			System.out.println();
		}
	}

	public static void setLoc(int[][] loc) {
		Box.loc = loc;
	}
	
	public static void find()
	{
		int[] now = new int[2];
		
		while(true)
		{
			now = Ant.getLoc();
			
			if(Box.loc[now[0]][now[1]]==2)
				break;
			
			Box.loc[now[0]][now[1]] = 9;
			if(Box.loc[now[0]][now[1]+1] != 1)
			{
				Ant.move(now[0], now[1]+1);
			}
			
			else if(Box.loc[now[0]][now[1]+1] == 1)
			{
				if(Box.loc[now[0]+1][now[1]] == 1)
				{
					//System.out.println("ant can't food");
					break;
				}
				else 
				{
					Ant.move(now[0]+1, now[1]);
				}
			}
		}
		Box.loc[now[0]][now[1]] = 9;	
	}
}
