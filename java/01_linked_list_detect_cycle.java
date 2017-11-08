boolean hasCycle(Node head) {
  Node node = head;
  Integer arr[] = {};
  HashMap<Integer, Integer> counter = new HashMap<Integer, Integer>();
  while(node != null) {
    if (counter.containsKey(node.data)) {
      return true;
    } else {
      counter.put(node.data, 1);
    }
    node = node.next;
  }
  return false;
}
