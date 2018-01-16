# Input: percent: 0.4
#        download: [["a",30],["b",30],["c",40]]
# Output: "b"

def show_by_percentage(percent, download)
  percent *=100
  download.each do |message|
    string = message[0]
    value = message[1]
    if percent - value <= 0
      return string
    else
      percent -= value
    end
  end
end