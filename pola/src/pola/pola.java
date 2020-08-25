/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package pola;

/**
 *
 * @author userMM
 */
public class pola {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        int i, j;
        for (i = 0; i<=5; i++){
            for (j = 0; j<i; j++){
                System.out.print("*");
            }
            System.out.println();
        }
        
        for (i = 0; i<=5; i++){
            for (j = 5; j>i; j--){
                System.out.print("*");
            }
            System.out.println();
        }
        System.out.println();
        for (i = 0; i<=5; i++){
            for (j = 0; j<i; j++){
                System.out.print(i);
            }
            System.out.println();
        }
        System.out.println();
        for (i = 0; i<=5; i++){
          for (j = 0; j<i; j++){
              System.out.print(j);
           }
          System.out.println();
        }
    }
    
}
