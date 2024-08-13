import java.io.FileReader;
import java.io.FileWriter;
import java.util.Scanner;

public class SubTask4 {
    public static void main(String[] args) {
        FileReader reader = new FileReader("input.txt");
        Scanner fileScanner = new Scanner(reader);
        int rows = fileScanner.nextInt();
        fileScanner.close();

        FileWriter writer = new FileWriter("output.txt");

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < rows - i - 1; j++) {
                writer.write(" ");
            }
            for (int j = 0; j <= i; j++) {
                writer.write("* ");
            }
            writer.write("\n");
        }
        for (int i = 0; i < rows - 1; i++) {
            for (int j = 0; j <= i; j++) {
                writer.write(" ");
            }
            for (int j = 0; j < rows - i - 1; j++) {
                writer.write("* ");
            }
            writer.write("\n");
        }

        writer.close();
    }
}
