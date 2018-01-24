# GRID = [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0], [1, 0, 0, 0]]
GRID = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
SEEN = []
NUM_ROWS = GRID.length
NUM_COLS = GRID[0].length

def adjacent_positions(pos)
  row, col = pos
  positions = []
  i = -1
  j = -1
  while i < 2
    while j < 2
      positions.push([row+i, col+j]) unless seen_or_is_zero?([row+i, col+j])
      j += 1
    end
    i += 1
    j = -1
  end
  positions
end

def is_zero?(pos)
  row, col = pos
  GRID[row][col] == 0
end

def off_board?(pos)
  row, col = pos
  !row.between?(0, NUM_ROWS-1) || !col.between?(0, NUM_COLS-1)
end

def seen_or_is_zero?(pos)
  off_board?(pos) || SEEN.include?(pos) || is_zero?(pos)
end
    
def get_size(pos)
  SEEN << pos
  adj_pos = adjacent_positions(pos)
  return 1 if adj_pos.empty?
  # adj_pos.each { |position| SEEN << position }
  count = 1
  adj_pos.each do |position|
    count += get_size(position) unless SEEN.include?(position)
  end
  count
end

#
#
row = 0
col = 0
max = 0
while row < NUM_ROWS
  while col < NUM_COLS
    pos = [row, col]
    unless seen_or_is_zero?(pos)
      count = get_size(pos)
      max = count if count > max
    end
    col += 1
  end
  row += 1
  col = 0
end
puts max

# puts get_size([2,2])
# print SEEN