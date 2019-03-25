
// package whatever; // don't place package name!

import java.io.*;
import java.util.*;
import java.lang.Object;

class MyCode {

  public static List<String> prioritizedOrders(int numOrders, List<String> orderList) {
    // WRITE YOUR CODE HERE
    Comparator<String> orderComparator = new Comparator<String>() {
      @Override
      public int compare(String s1, String s2) {
        String[] s1Data = s1.split(" ");
        String[] s2Data = s2.split(" ");
        for (int i = 1; i < s1Data.length; i++) {
          int compare = s1Data[i].compareTo(s2Data[i]);
          if (compare != 0) {
            return compare;
          }
        }

        // if you get here that means the data is the same! now compare the Ids
        return s1Data[0].compareTo(s2Data[0]);
      }
    };

    PriorityQueue<String> prime = new PriorityQueue<>(orderComparator);
    PriorityQueue<String> regular = new PriorityQueue<>(orderComparator);

    for (int i = 0; i < numOrders; i++) {
      List<String> orderDetails = Arrays.asList(orderList.get(i).split(" "));
      boolean isPrime = !isNumeric(orderDetails.get(orderDetails.size() - 1));
      if (isPrime) {
        prime.add(orderList.get(i));
      } else {
        regular.add(orderList.get(i));
      }
      System.out.println("----");

    }
    List<String> result = new ArrayList<>();
    while (prime.peek() != null) {
      result.add(prime.poll());
    }
    while (regular.peek() != null) {
      result.add(regular.poll());
    }
    return result;
  }

  // METHOD SIGNATURE ENDS
  public static boolean isNumeric(String str) {
    try {
      int d = Integer.parseInt(str);
    } catch (NumberFormatException | NullPointerException e) {
      return false;
    }
    return true;
  }

  public static void main(String[] args) {
    // HashMap<ArrayList<Integer>, Integer> test = new HashMap<>();
    // ArrayList<Integer> test2 = new ArrayList<>();
    // test2.add(5);
    // test.put(test2, 5);
    // ArrayList<Integer> test3 = new ArrayList<>();
    // // test3.add(4);
    // String s1 = "has uni gry";
    // String s2 = "eat nim did";
    // System.out.println(s1.compareTo(s2));
    List<String> orderList = new ArrayList<>();
    // orderList.add("t2 13 121 98");
    // orderList.add("f3 52 34 31");
    // orderList.add("b4 xi me nu");
    // orderList.add("w1 has uni gry");
    // orderList.add("br8 eat nim did");
    // orderList.add("br9 eat nim did");
    // orderList.add("r1 box ape bit");
    System.out.println(prioritizedOrders(0, orderList));
  }
}
