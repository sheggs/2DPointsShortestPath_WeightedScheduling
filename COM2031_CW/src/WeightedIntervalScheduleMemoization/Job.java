package WeightedIntervalScheduleMemoization;

public class Job {
	private String name;
	private int start;
	private int end;
	private int value;
	public Job(String name, int start, int end, int value) {
		this.name = name;
		this.start = start;
		this.end = end;
		this.value = value;
	}
	public String getName() {
		return name;
	}
	public int getEnd() {
		return end;
	} 
	public int getStart() {
		return start;
	}
	public int getValue() {
		return value;
	}


	

}
