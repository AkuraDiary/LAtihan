/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
/**
 *
 * @author userMM
 */
import java.util.Scanner;
public class halo {

    /**
     * @param args the command line arguments
     */
    static String x;
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner coba = new Scanner(System.in);
        String text = "Input nama : ";
        System.out.print(text);
        x = coba.nextLine();
        System.out.println("\n" + "Hai " +x);
    }
    
}
