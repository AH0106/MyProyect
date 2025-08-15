package Algorithms_Excercises;

import java.util.*;
import java.lang.*;
import java.util.Arrays;
import edu.princeton.cs.algs4.MinPQ;
import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;

public class main1 {

  public static int abs(int x) {
    if (x < 0) {
      return -x;
    } else {
      return x;
    }
  }

  public static boolean isPrime(long n) {
    if (n < 2) return false;
    for (long i = 2; i * i <= n; i++) {
        if (n % i == 0) return false;
    }
    return true;
}


  public static void main(String[] args) {

    StdOut.println("Ingrese números (Ctrl+D para terminar):");
    double sum = 0.0;

    // Leer todos los doubles del input estándar y sumarlos
    while (!StdIn.isEmpty()) {
      double value = StdIn.readDouble();
      sum += value;
    }

    // Mostrar el resultado
    StdOut.printf("La suma total es: %.2f\n", sum);
  }

}

