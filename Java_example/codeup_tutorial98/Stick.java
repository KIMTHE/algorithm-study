
public class Stick {
	private int d,l;
	private int sx,sy;
	private int[][] loc;
	
	public int getD() {
		return d;
	}
	public void setD(int d) {
		this.d = d;
	}
	public int getL() {
		return l;
	}
	public void setL(int l) {
		this.l = l;
	}
	public int getSx() {
		return sx;
	}
	public void setSx(int sx) {
		this.sx = sx;
	}
	public int getSy() {
		return sy;
	}
	public void setSy(int sy) {
		this.sy = sy;
	}
	
	public int[][] getLoc() {
		return loc;
	}
	public void setLoc(int sx, int sy,int d,int l) {
		if(d==0)
		{
			for(int i=0; i<l; i++)
			{
				loc[i][0] = sx;
				loc[i][1] = sy+i;
			}
		}
		
		else if(d==1)
		{
			for(int i=0; i<l; i++)
			{
				loc[i][0] = sx+i;
				loc[i][1] = sy;
			}
		}
	}
	
	public Stick(int l, int d, int sx, int sy) {
		super();
		this.d = d;
		this.l = l;
		this.sx = sx;
		this.sy = sy;
		
		loc = new int[l][2];
		setLoc(sx,sy,d,l);
	}
	
	public void print()
	{
		for(int i = 0; i<this.getL(); i++)
		{
			System.out.print("("+this.loc[i][0]+","+this.loc[i][1]+") ");
		}
		System.out.println();
	}
	
	

}
