class Solution {
    // Helper method to find the maximum sum of values in 3 rows with no common columns
    private long helper(int[][] matrix) {
        int rows = matrix.length;
        int cols = matrix[0].length;
        long maxSum = Long.MIN_VALUE;

        // Initialize arrays to store top 3 values and their columns
        long[][] topValues = new long[rows][3];
        int[][] topColumns = new int[rows][3];
        for (int i = 0; i < rows; i++) {
            Arrays.fill(topValues[i], Long.MIN_VALUE);
            Arrays.fill(topColumns[i], -1);
        }

        // Process each row to find top 3 values and their columns
        for (int row = 0; row < rows; row++) {
            List<Pair<Long, Integer>> columnValues = new ArrayList<>();
            for (int col = 0; col < cols; col++) {
                columnValues.add(new Pair<>((long) matrix[row][col], col));
            }
            columnValues.sort((a, b) -> Long.compare(b.getKey(), a.getKey()));

            for (int rank = 0; rank < 3 && rank < cols; rank++) {
                topColumns[row][rank] = columnValues.get(rank).getValue();
                topValues[row][rank] = columnValues.get(rank).getKey();
            }
        }

        // Check all combinations of rows and columns
        for (int row1 = 0; row1 < rows; row1++) {
            for (int row2 = row1 + 1; row2 < rows; row2++) {
                for (int row3 = row2 + 1; row3 < rows; row3++) {
                    for (int col1 = 0; col1 < 3; col1++) {
                        for (int col2 = 0; col2 < 3; col2++) {
                            if (topColumns[row2][col2] == topColumns[row1][col1]) continue;
                            for (int col3 = 0; col3 < 3; col3++) {
                                if (topColumns[row3][col3] == topColumns[row1][col1] || topColumns[row3][col3] == topColumns[row2][col2]) continue;

                                long currentSum = topValues[row1][col1] + topValues[row2][col2] + topValues[row3][col3];
                                maxSum = Math.max(maxSum, currentSum);
                            }
                        }
                    }
                }
            }
        }
        return maxSum;
    }

    // Method to call the helper method
    public long maximumValueSum(int[][] matrix) {
        return helper(matrix);
    }
}