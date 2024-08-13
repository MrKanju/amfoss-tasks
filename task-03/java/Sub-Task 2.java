import java.io.FileReader;
import java.io.FileWriter;

public class SubTask2 {
    public static void main(String[] args) {
        FileReader reader = new FileReader("input.txt");
        FileWriter writer = new FileWriter("output.txt");

        int c;
        while ((c = reader.read()) != -1) {
            writer.write(c);
        }

        reader.close();
        writer.close();
    }
}
