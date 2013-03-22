public class week2{

	public static final int DEF_GRD = -1;
	private int name;
	private int grd;

	public week2 ( int name, int grd ){
		this.name = name;
		this.grd = grd;		
	}

        public week2( int name ){
                this.name = name;
		grd = DEF_GRD;
        }

	public int getGrd(){
		return grd;
	}

	public int getAN(){
		return name;
	}

	public void setGrd(int g){
		if (g > 100){			
			grd = 100;
		} else if (g < 0){
			grd = 0;
		}else{
			grd = g;
		}
	}
}
