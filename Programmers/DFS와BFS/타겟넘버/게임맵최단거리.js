function solution(maps) {
    let answer = -1;
    const n = maps.length;
    const m = maps[0].length;
    let visited = Array.from(Array(n), ()=> Array(m).fill(false));
    const dx = [0, 0, 1, -1];
    const dy = [1, -1, 0, 0];
    let queue = [[0, 0, 1]];
    let queueIdx = 0;
    
    while (queue.length > queueIdx) {
        let [x, y, count] = queue[queueIdx];
        queueIdx += 1;
        
        if (x == n - 1 && y == m - 1) {
            answer = count;
            return answer;
        }
        
        if (!visited[x][y]) {
            visited[x][y] = true;
            
            for (let i=0; i<4; i++) {
                const nx = x + dx[i];
                const ny = y + dy[i];
                
                if (nx >= 0 && nx < n && ny >= 0 && ny < m && !visited[nx][ny] && maps[nx][ny] === 1) {
                    queue.push([nx, ny, count + 1]);
                }
            }
        }
    }
    return answer;
}
