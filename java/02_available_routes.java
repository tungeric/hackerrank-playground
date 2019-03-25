
// package whatever; // don't place package name!

import java.io.*;
import java.util.*;
import java.lang.Object;

class MyCode2 {

  static int minimumCostIncurred(int numTotalEdgeNodes, int numTotalAvailableNetworkRoutes,
      List<List<Integer>> networkRoutesAvailable, int numNewNetworkRoutesConstruct,
      List<List<Integer>> costNewNetworkRoutesConstruct) {
    // WRITE YOUR CODE HERE
    // go through network routes available and construct networks
    // --> should end up with List<Set<Integer>> where each set is a networks
    Set<Integer> lonelyNodes = new HashSet<>();
    for (int i = 1; i <= numTotalEdgeNodes; i++) {
      lonelyNodes.add(i);
    }
    List<Set<Integer>> networkList = new ArrayList<>();
    for (int i = 0; i < networkRoutesAvailable.size(); i++) {
      List<Integer> route = networkRoutesAvailable.get(i);
      Set<Integer> nodes = new HashSet<>();
      for (int x = 0; x < route.size(); x++) {
        lonelyNodes.remove(route.get(x));
        nodes.add(route.get(x));
      }
      if (networkList.size() > 0) {
        boolean hasCommon = false;
        for (int j = 0; j < networkList.size(); j++) {
          if (hasCommonNodes(networkList.get(j), nodes)) {
            networkList.get(j).addAll(nodes);
            hasCommon = true;
          }
        }
        if (!hasCommon) {
          networkList.add(nodes);
        }
      } else {
        networkList.add(nodes);
      }
    }
    for (int node : lonelyNodes) {
      Set<Integer> lonelySet = new HashSet<>();
      lonelySet.add(node);
      networkList.add(lonelySet);
    }
    System.out.println(networkList);
    // if numTotalEdgeNodes - List.size() > numNewNetworkRoutesConstruct return fail
    // case :
    // otherwise...
    // go through costNewNetworkRoutesConstruct
    Map<String, Integer> minCostMap = new HashMap<>();
    for (int i = 0; i < costNewNetworkRoutesConstruct.size(); i++) {
      List<Integer> current = costNewNetworkRoutesConstruct.get(i);
      // System.out.println(current);
      List<Integer> networksTouched = new ArrayList<>();
      for (int node = 0; node < 2; node++) {
        for (int networkIdx = 0; networkIdx < networkList.size(); networkIdx++) {
          if (networkList.get(networkIdx).contains(current.get(node))) {
            // System.out.println(networkList.get(networkIdx));
            // System.out.println(current.get(node));
            networksTouched.add(networkIdx);
            break;
          }
        }
      }
      System.out.println(networksTouched);
      if (minCostMap.containsKey(networksTouched.toString())) {
        if (minCostMap.get(networksTouched.toString()) > current.get(2)) {
          minCostMap.put(networksTouched.toString(), current.get(2));
        }
      } else {
        minCostMap.put(networksTouched.toString(), current.get(2));
      }
    }
    System.out.println(minCostMap);
    return 5;
  }

  static boolean hasCommonNodes(Set<Integer> set1, Set<Integer> set2) {
    Set<Integer> result = new HashSet<Integer>(set1);
    result.retainAll(set2);
    return result.size() > 0;
  }

  public static void main(String[] args) {
    List<Integer> route1 = new ArrayList<>();
    route1.add(1);
    route1.add(4);
    List<Integer> route2 = new ArrayList<>();
    route2.add(4);
    route2.add(5);
    List<Integer> route3 = new ArrayList<>();
    route3.add(3);
    route3.add(2);
    List<List<Integer>> routes = new ArrayList<>();
    routes.add(route1);
    routes.add(route2);
    routes.add(route3);
    List<Integer> cost1 = new ArrayList<>();
    cost1.add(1);
    cost1.add(2);
    cost1.add(5);
    List<Integer> cost2 = new ArrayList<>();
    cost2.add(1);
    cost2.add(3);
    cost2.add(10);
    List<Integer> cost3 = new ArrayList<>();
    cost3.add(1);
    cost3.add(6);
    cost3.add(2);
    List<Integer> cost4 = new ArrayList<>();
    cost4.add(5);
    cost4.add(6);
    cost4.add(5);
    List<List<Integer>> stuff = new ArrayList<>();
    stuff.add(cost1);
    stuff.add(cost2);
    stuff.add(cost3);
    stuff.add(cost4);
    System.out.println(minimumCostIncurred(6, 3, routes, 4, stuff));
  }
}
