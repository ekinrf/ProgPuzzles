import java.util.PriorityQueue;

public class WaterTrapper {

    static class Block implements Comparable<Block> {

        int x;
        int y;
        int height;

        Block(int x, int y, int height) {
            this.x = x;
            this.y = y;
            this.height = height;
        }

        @Override
        public int compareTo(Block another) {
            return this.height - another.height;
        }
    }

    public static int trapRainWater(int[][] heightMap) {

        int xLen = heightMap.length;
        if(xLen <= 0) return 0;
        int yLen = heightMap[0].length;
        boolean[][] visitedMatrix = new boolean[xLen][yLen]; // default to false
        PriorityQueue<Block> priorityQueue = new PriorityQueue<>(xLen * yLen); // probably too big
        for (int x = 0; x < xLen; x++)
            for (int y = 0; y < yLen; y++) {
                if (x == 0 || y == 0 || y == (yLen - 1) || x == (xLen - 1)) {
                    priorityQueue.add(new Block(x, y, heightMap[x][y]));
                    visitedMatrix[x][y] = true;
                }
            }

        int waterLevel = 0, waterFilled = 0;
        while (priorityQueue.size() > 0) {
            Block block = priorityQueue.poll();
            if(waterLevel < block.height)
                waterLevel = block.height;
            waterFilled += waterLevel- block.height;
            int[][] neighbours = {{block.x - 1, block.y}, {block.x + 1, block.y}, {block.x, block.y - 1}, {block.x, block.y + 1}};
            for(int x = 0; x < 4; ++x){
                int nX = neighbours[x][0];
                int nY = neighbours[x][1];
                if(nX < xLen && nX >= 0 && nY < yLen && nY >= 0){
                    if(!visitedMatrix[nX][nY]) {
                        visitedMatrix[nX][nY] = true;
                        priorityQueue.add(new Block(nX, nY, heightMap[nX][nY]));
                    }
                }
            }
        }
        return waterFilled;
    }

    public static void main(String[] args) {

        int[][] heightMap = {
                {1, 4, 3, 1, 3, 2},
                {3, 2, 1, 3, 2, 4},
                {2, 3, 3, 2, 3, 1}
        };
        System.out.println(trapRainWater(heightMap));
    }
}
