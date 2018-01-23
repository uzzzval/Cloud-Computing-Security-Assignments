/* Created by Sean Futch, Josh Ciocco
   and Ujjawal Sharma for the Covert Channel 2 Assignment.
   Here we are doing the review of the work done by group 5.
   Group 5 had members Aurin Chakravarty and Avijit Kumar.
   This programme has been created to work as the Sender
   programme on one of the VMs. */ 

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.RandomAccessFile;
import java.util.Random;
import java.util.Scanner;
import java.util.Arrays;

public class Sender {

	public static void main(String[] args) throws IOException, InterruptedException {
                //Getting the input through console
		System.out.println("Please provide the input string:");
		Scanner scanner = new Scanner(System.in);
		String inputString = scanner.nextLine();
		char[] inputStringArray=new char[inputString.length()];
		inputStringArray=inputString.toCharArray();
		String filepath="/home/ujjawalsharma/Desktop/Sender Programme/the-file-name.txt";
                //Iterating over all the bits to get the time required to read each bit
		for(int i=0;i<inputStringArray.length;i++) {
			Thread.sleep(1000);
			long startTime = System.nanoTime();
                        //Generating the random number
			Random rand = new Random();
			int  position = rand.nextInt(20000000) + 1;
			if(inputStringArray[i]=='1') {
				readFile(filepath,position);
			}
			long stopTime = System.nanoTime();
			float elapsedTime =(stopTime-startTime)/10000;
			System.out.println("Time taken to read the current bit = "+elapsedTime);
		}
	}
	
	public static void readFile(String filepath,int position) throws IOException {
                //Helper method used to read the file at the random location
		File file = new File(filepath); 
		RandomAccessFile randomFile = new RandomAccessFile(file,"rw"); 
		byte[] readArray=new byte[20000000];
        int returnNumber=randomFile.read(readArray,0,position);
        randomFile.close();
	}
}
