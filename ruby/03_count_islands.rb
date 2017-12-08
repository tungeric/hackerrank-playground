# Enter your code here. Read input from STDIN. Print output to STDOUT
GRID = STDIN.read.split("\n")
NUM_ROWS, NUM_COLS = GRID.shift.split(" ").map { |num| num.to_i }
GRID.map! { |row| row.split(" ").map { |num| num.to_i } }

SEEN = []


def adjacent_positions(pos)
  row, col = pos
  positions = []
  positions.push([row-1, col-1]) unless seen_or_is_water?([row-1, col-1])
  positions.push([row-1, col]) unless seen_or_is_water?([row-1, col])
  positions.push([row-1, col+1]) unless seen_or_is_water?([row-1, col+1])
  positions.push([row, col-1]) unless seen_or_is_water?([row, col-1])
  positions.push([row, col+1]) unless seen_or_is_water?([row, col+1])
  positions.push([row+1, col-1]) unless seen_or_is_water?([row+1, col-1])
  positions.push([row+1, col]) unless seen_or_is_water?([row+1, col])
  positions.push([row+1, col+1]) unless seen_or_is_water?([row+1, col+1])
  positions
end

def is_water?(pos)
  row, col = pos
  GRID[row][col] == 0
end

def off_board?(pos)
  row, col = pos
  !row.between?(0,NUM_ROWS-1) || !col.between?(0, NUM_COLS-1)
end
  
def seen_or_is_water?(pos)
  off_board?(pos) || SEEN.include?(pos) || is_water?(pos)
end

def check_adjacent_positions(pos)
  SEEN << pos
  adj_pos = adjacent_positions(pos)
  adj_pos.each { |position| check_adjacent_positions(position) }
end


num_islands = 0

row = 0
col = 0
while row < NUM_ROWS
  while col < NUM_COLS
    pos = [row, col]
    unless seen_or_is_water?(pos)
      num_islands += 1
      check_adjacent_positions(pos)
    end
    col+=1
  end
  col = 0
  row += 1
end
print num_islands