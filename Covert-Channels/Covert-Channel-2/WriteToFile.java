import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.PrintWriter;
import java.io.RandomAccessFile;
import java.io.UnsupportedEncodingException;

public class WriteToFile {

	public static void main(String[] args) throws IOException {
		RandomAccessFile file = new RandomAccessFile("/home/ujjawalsharma/Desktop/Sender Programme/the-file-name.txt", "rw");
		for(int i=0;i<65000000;i++) {
			file.write("I want to make this file of size 2GB".getBytes());
		}
		file.close();
	}
}
