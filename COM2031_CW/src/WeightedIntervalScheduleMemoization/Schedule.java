package WeightedIntervalScheduleMemoization;

import java.awt.List;
import java.util.ArrayList;

public class Schedule {
	private Job[] jobs;
	private int[] M;
	private ArrayList<Job> j = new ArrayList<Job>();
	public Schedule(Job[] jobs) {
		this.jobs = sortJobByFinish(jobs);
		this.M = new int[jobs.length + 1];
	}
	public Job[] sortJobByFinish(Job[] jobs) {
		Job[] jobs2 = jobs;
		for(int i = 0; i<jobs2.length;i++) {
			for(int j = 0; j<jobs2.length;j++) {
				if(jobs2[i].getEnd() < jobs2[j].getEnd()) {
					Job temp = jobs2[i];
					jobs2[i] = jobs2[j];
					jobs2[j]= temp;
				}
			}
		}
		return jobs2;
	}
	
	public void display() {
		for(int i = 0; i<this.jobs.length;i++) {
			System.out.print(this.jobs[i].getName() + " ");
		}
		System.out.println();
	}
	public int p(int x) {
		int jobVal = x -1;
		if( x == 0 ){
			jobVal = 0;
		}
	
		Job selected = this.jobs[jobVal];
		for(int i = jobVal; i<this.jobs.length;i--) {
			if(i == -1){
				break;
			}
			//System.out.println("SSSS");
			//System.out.println(jobs[i].getEnd()  + " " + selected.getStart());
			if(jobs[i].getEnd() <= selected.getStart()) {
				return i + 1;
			}
		}
		return 0;
	}
	public Job[] getJobs() {
		return jobs;
	}
	public int OPT(int x) {
//		for (int i = 0; i< this.jobs.length;i++) {
//			if(arr[i + 1] == 0) {
//				arr[i + 1] = max(this.jobs[i].getValue() + OPT(p(i)), OPT(i - 1) );
//			}
//		}
		String cont = "";
		int jobVal = x - 1;
		M[0] = 0;
		//System.out.println("C: " + x);
		if(x <= 0) {
			return M[0];
		}else {

			if(x == 8){
				System.out.println(this.jobs[jobVal].getName() + " " + p(x));
				
			}
			M[x] = max(this.jobs[jobVal].getValue() + OPT(p(x)), OPT(x - 1) );	
			
		}
//		if(M[x] == 0) {
//			if (x <= 0) {
//				M[x] = this.jobs[0].getValue();
//			}else {
//				
//			}
//		}
		return M[x];

	
//		System.out.println(arr[1]);
		
	}
	public int[] getM() {
		return M;
	}
	public int max(int a, int b) {
		return (a<b)?b:a;
	}
	public void post(){
		int z = this.jobs.length;
		while (z > 0){
			if(this.M[z] > this.M[z-1]){
				this.j.add(this.jobs[z - 1]);
				z = p(z);
			}else{
				z--;
			}
		}
		for(Job q : this.j){
			System.out.print(q.getName() + " ");
		}
		System.out.println();
	}
	public static void main(String[] args) {
		Schedule t = new Schedule(new Job[] {new Job("A",9,12,4),new Job("B",11,14,8),new Job("C",2,8,6),new Job("D",9,11,5),new Job("E",4,10,4),new Job("F",9,15,7),new Job("G",15,17,3),new Job("H",15,18,4)});
//		Schedule t = new Schedule(new Job[] {new Job("A",3,10,20), new Job("B",1,2,50), new Job("C",6,19,100),new Job("D",2,100,200)});
		t.display();
		System.out.println("Hi : " + t.p(8));
		System.out.println(t.OPT(t.getJobs().length));
		System.out.println("M");
		for(int i = 0; i<t.getM().length; i ++) {
			System.out.println(i + " " + t.getM()[i]);
		}
		System.out.println();
		System.out.println("P");
		for(int i = 0; i<t.getM().length; i ++) {
			System.out.println(i + " " + t.p(i));
		}
//		System.out.println(t.p(t.getJobs().length - 1).getName());
//		System.out.println(t.p(t.getJobs().length - 3).getName());
//		System.out.println(max(10,3));]
		t.post();
	}


}
