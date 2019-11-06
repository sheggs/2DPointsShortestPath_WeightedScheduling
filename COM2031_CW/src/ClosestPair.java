import java.util.Arrays;

public class ClosestPair {
	
	private Point[] points;
	public ClosestPair(Point[] points) {
		this.points = sortPointsByX(points);
		
	}
	private Point[] sortPointsByX(Point[] points) {
		for(int i = 0; i<points.length;i++) {
			for(int j = 0; j<points.length;j++) {
				if(points[i].getX() <= points[j].getX()) {
					Point temp = points[i];
					points[i] = points[j];
					points[j] = temp;
				}
			}
		}
		return points;
	}
	private Point[] sortPointsByY(Point[] points) {
		for(int i = 0; i<points.length;i++) {
			for(int j = 0; j<points.length;j++) {
				if(points[i].getY() <= points[j].getY()) {
					Point temp = points[i];
					points[i] = points[j];
					points[j] = temp;
				}
			}
		}
		return points;
	}
	public Point[] getPoints() {
		return points;
	}
	public double abs(double a) { return Math.abs(a);}
	public double calculateDistance(Point a, Point b) {
		System.out.println("( " + a.getX() + "- "+ b.getX() + ") ^ 2 + " + " ( " + a.getY() + " - " + b.getY() + ") ^ 2");
		//Math.sqrt(((abs(a.getX()) - abs(b.getX()))*(abs(a.getX()) - abs(b.getX()))) - ((abs(a.getY()) - abs(b.getY()))*(abs(a.getY()) - abs(b.getY()))));
		double calculation = ((a.X() - b.X())*(a.X() - b.X())) + ((a.Y() - b.Y())*(a.Y() - b.Y()));
		return Math.sqrt(calculation);
	}
	public double forceCalculate(Point[] points, int d) {
		double min = Double.MAX_VALUE;
		for(int i = 0; i<points.length;i++) {
			for(int j = 1; j<points.length;j++) {
				double dist = calculateDistance(points[i], points[j]);
				if(dist == 0) {
					break;
				}
				min = min(min, dist);
			}
		}
		return min;
	}
	public double calcClosestPair(Point[] points) {
		int middle = points.length/2;
		System.out.println("mid" + middle + "len " + points.length);
		if(points.length <= 3) {
			return forceCalculate(points, points.length);
		}
		Point[] aux = Arrays.copyOfRange(points, 0, middle - 1);
		Point[] aux2 = Arrays.copyOfRange(points, middle, points.length - 1);

		double d1 = calcClosestPair(aux);
		double d2 = calcClosestPair(aux2);
		System.out.println(d1 + " " + d2);
		double d = min(d1,d2);
		// Only gets Delta
		return d;
	}
	public double min(double d1, double d2) {
		return (d1<d2) ? d1:d2;
	}
	public static void main(String args[]) {
		ClosestPair p = new ClosestPair(new Point[] {new Point(-3.0, -6.0), new Point(-6.0, -5.0),new Point(-5.0, 3.0),new Point (1.0, 5.0),new Point(-4.0, -1.0),new Point(5.0, 6.0),new Point(-1.0, 4.0),new Point (6.0, -7.0)} );
		for(int i = 0; i< p.getPoints().length;i++) {
			System.out.print("(" + p.getPoints()[i].getX() + "," + p.getPoints()[i].getY() + ")");
		}
		System.out.println(p.calcClosestPair(p.getPoints()));
		//System.out.println("hi");
	}

}
