class Solution {
    public int areaOfMaxDiagonal(int[][] dimensions) {
        HashMap<Integer, ArrayList<Integer>> map = new HashMap<>();
        for (int i=0; i<dimensions.length; i++) {
            int val = dimensions[i][0] * dimensions[i][0] + dimensions[i][1] * dimensions[i][1];
            
            if (!map.containsKey(val)) map.put(val, new ArrayList<Integer>());    
            map.get(val).add(dimensions[i][0] * dimensions[i][1]);
        }
        Integer max = 0;
        for (Integer i : map.keySet()) if (max < i) max = i;
        ArrayList<Integer> result = map.get(max);
        max = 0;
        for (Integer i : result) if (max < i) max = i;
        return max;
    }
}

