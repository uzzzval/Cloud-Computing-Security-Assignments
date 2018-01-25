/* Created by Sean Futch, Josh Ciocco
   and Ujjawal Sharma for the Covert Channel 2 Assignment.
   Here we are doing the review of the work done by group 5.
   Group 5 had members Aurin Chakravarty and Avijit Kumar.
   This programme has been created to work as the Receiver
   programme on one of the VMs. */ 


import java.io.File;
import java.io.IOException;
import java.io.RandomAccessFile;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import static java.lang.Math.*;

public class Receiver {

	public static void main(String[] args) throws IOException, InterruptedException {
		ArrayList timeList=new ArrayList();
		String filepath="/root/Desktop/Receiver Programme/the-file-name.txt";
                //The iteration is currently for an 8-bit string
		for(int i=0;i<8;i++) {
			Thread.sleep(900);
			long startTime = System.nanoTime();
			readFile(filepath,156134);
			long stopTime = System.nanoTime();
			float elapsedTime =(stopTime-startTime)/10000;
			timeList.add(elapsedTime);
                        System.out.println("Time taken to read the current bit = "+elapsedTime);
		}
		Iterator timeListIterator=timeList.iterator();
		float sum=0;
                //Getting the sum of all the values in the List.
		while(timeListIterator.hasNext()) {
			sum=sum+(float)timeListIterator.next();
		}
                //Calculating the Standard Deviation
		float standardDeviation=calculatingSD(timeList);
		String finalOutputString="";
		Iterator timeListIteratorforCalibration=timeList.iterator();
		while(timeListIteratorforCalibration.hasNext()) {
			if((float)timeListIteratorforCalibration.next()>standardDeviation) {
				finalOutputString=finalOutputString+"1";
			}else {
				finalOutputString=finalOutputString+"0";
			}
		}
		System.out.println("Final Output String"+finalOutputString);
	}
	
	public static void readFile(String filepath,int position) throws IOException {
                //Helper Method for reading the file at a particular location, hard-coded at 156134
		File file = new File(filepath); 
		RandomAccessFile randomFile = new RandomAccessFile(file,"rw"); 
		byte[] readArray=new byte[200000];
                int returnNumber=randomFile.read(readArray,0,position);
                randomFile.close();
	}

        public static float calculatingSD(List timeList) {
		Iterator timeListIterator=timeList.iterator();
		float sum=0f;
		while(timeListIterator.hasNext()) {
			sum=sum+(float)timeListIterator.next();
		}
                //Calculating Average
		float average=sum/timeList.size();
                System.out.println("Average Latency"+average);
		Iterator timeListIterator2=timeList.iterator();
		List listTwo=new ArrayList();
		while(timeListIterator2.hasNext()) {
			float value=(float)timeListIterator2.next();
			listTwo.add((value-average)*(value-average));
		}
		Iterator listTwoIterator=listTwo.iterator();
		float summation=0;
		while(listTwoIterator.hasNext()) {
			summation=summation+(float)listTwoIterator.next();
		}
		float perRecord=summation/timeList.size();
                //finalValue holds standard deviation
		float finalValue=(float) sqrt(perRecord);
		return finalValue;
		
	}
}
